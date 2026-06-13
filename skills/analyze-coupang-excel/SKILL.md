---
name: analyze-coupang-excel
description: Analyze Coupang product export spreadsheets for cross-border ecommerce selection. Use when the user uploads or references Excel/CSV product data containing fields such as id, sku, image, product name, delivery type, price, reviews, rating, clicks, sales, or wants market trend, opportunity, competitor, and SKU prioritization insights.
---

# Analyze Coupang Excel

Use this skill to turn a Coupang product data spreadsheet into structured market insights for content or decision support.

## Workflow

1. Locate the uploaded `.xlsx` or `.csv` file.
2. Run `scripts/analyze_coupang_excel.py` from the plugin root when Python is available:
   - `python scripts/analyze_coupang_excel.py <input-file> --out <analysis-json>`
   - If `python` is unavailable, try `py`, `python3`, or the environment's available Python runtime.
3. The script can read `.xlsx` with `openpyxl` when installed, and falls back to Python standard-library `.xlsx` parsing when `openpyxl` is missing.
4. If no Python runtime is available, inspect the spreadsheet with any available workbook library or XML reader and produce the same analysis fields manually.
5. Report the insights in Chinese unless the user asks otherwise.

## Analysis Requirements

Prioritize:

- Market heat: sales, click volume, review volume, and rating distribution.
- Conversion signal: high sales with moderate clicks, high rating with rising reviews, or low review count with meaningful sales.
- Price bands: median price, low/high price clusters, and outliers.
- Fulfillment signal: delivery type differences and whether delivery correlates with sales or rating.
- Opportunity SKUs: products with strong sales/rating but weaker content saturation.
- Risk SKUs: low rating, many negative proxy signals, extreme price, or abnormal clicks without sales.

## Output Shape

Return a compact Chinese summary with:

- `数据概览`: row count, detected columns, price/sales/review/rating ranges.
- `趋势洞察`: 3-5 market trend bullets.
- `机会商品`: 3-8 product or SKU candidates with why they matter.
- `内容卖点`: data-backed angles that can feed Xiaohongshu content.
- `注意事项`: missing columns, suspicious data, and confidence limits.


