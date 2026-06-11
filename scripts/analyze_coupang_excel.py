#!/usr/bin/env python3
"""Analyze Coupang product spreadsheet exports for YunKan XHS content."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from statistics import median
from typing import Any


COLUMN_ALIASES = {
    "id": ["id", "商品id", "商品ID", "product_id", "product id"],
    "sku": ["sku", "SKU", "货号"],
    "image": ["主图", "main_image", "image", "图片", "商品主图"],
    "name": ["商品名称", "名称", "product_name", "name", "标题"],
    "delivery": ["配送类型", "delivery", "delivery_type", "物流", "配送"],
    "price": ["价格", "price", "售价"],
    "reviews": ["评论数", "review_count", "reviews", "评价数"],
    "rating": ["评分", "rating", "score"],
    "clicks": ["点击量", "clicks", "click_count"],
    "sales": ["销量", "sales", "sold", "销售量"],
}


def normalize_header(value: Any) -> str:
    return str(value or "").strip()


def to_number(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip().replace(",", "").replace("￥", "").replace("₩", "")
    if not text:
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    if math.isnan(number) or math.isinf(number):
        return None
    return number


def read_rows(path: Path) -> list[dict[str, Any]]:
    if path.suffix.lower() == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return list(csv.DictReader(handle))

    try:
        import openpyxl  # type: ignore
    except ImportError as exc:
        raise SystemExit("Reading Excel requires openpyxl. Install it or export CSV.") from exc

    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    sheet = workbook.active
    headers = [normalize_header(cell.value) for cell in next(sheet.iter_rows(min_row=1, max_row=1))]
    rows: list[dict[str, Any]] = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        rows.append({headers[index]: value for index, value in enumerate(row) if index < len(headers)})
    return rows


def detect_columns(headers: list[str]) -> dict[str, str | None]:
    lookup = {header.lower(): header for header in headers}
    detected: dict[str, str | None] = {}
    for field, aliases in COLUMN_ALIASES.items():
        detected[field] = None
        for alias in aliases:
            hit = lookup.get(alias.lower())
            if hit:
                detected[field] = hit
                break
    return detected


def values(rows: list[dict[str, Any]], column: str | None) -> list[float]:
    if not column:
        return []
    return [num for row in rows if (num := to_number(row.get(column))) is not None]


def stats(numbers: list[float]) -> dict[str, float] | None:
    if not numbers:
        return None
    ordered = sorted(numbers)
    return {
        "min": ordered[0],
        "median": median(ordered),
        "max": ordered[-1],
        "avg": sum(ordered) / len(ordered),
    }


def top_rows(rows: list[dict[str, Any]], detected: dict[str, str | None], key: str, limit: int = 8) -> list[dict[str, Any]]:
    column = detected.get(key)
    if not column:
        return []
    scored = [(to_number(row.get(column)) or 0, row) for row in rows]
    scored.sort(key=lambda item: item[0], reverse=True)
    output = []
    for _, row in scored[:limit]:
        output.append({
            "id": row.get(detected.get("id") or "", ""),
            "sku": row.get(detected.get("sku") or "", ""),
            "name": row.get(detected.get("name") or "", ""),
            "delivery": row.get(detected.get("delivery") or "", ""),
            "price": row.get(detected.get("price") or "", ""),
            "reviews": row.get(detected.get("reviews") or "", ""),
            "rating": row.get(detected.get("rating") or "", ""),
            "clicks": row.get(detected.get("clicks") or "", ""),
            "sales": row.get(detected.get("sales") or "", ""),
        })
    return output


def analyze(path: Path) -> dict[str, Any]:
    rows = read_rows(path)
    headers = list(rows[0].keys()) if rows else []
    detected = detect_columns(headers)
    numeric = {
        key: stats(values(rows, detected.get(key)))
        for key in ["price", "reviews", "rating", "clicks", "sales"]
    }

    delivery_column = detected.get("delivery")
    delivery_counts: dict[str, int] = {}
    if delivery_column:
        for row in rows:
            delivery = str(row.get(delivery_column) or "未知").strip() or "未知"
            delivery_counts[delivery] = delivery_counts.get(delivery, 0) + 1

    return {
        "file": str(path),
        "row_count": len(rows),
        "detected_columns": detected,
        "missing_fields": [key for key, column in detected.items() if column is None],
        "numeric_stats": numeric,
        "delivery_counts": delivery_counts,
        "top_by_sales": top_rows(rows, detected, "sales"),
        "top_by_clicks": top_rows(rows, detected, "clicks"),
        "top_by_reviews": top_rows(rows, detected, "reviews"),
        "top_by_rating": top_rows(rows, detected, "rating"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("--out", help="Write JSON analysis to this path.")
    args = parser.parse_args()

    result = analyze(Path(args.input_file))
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
