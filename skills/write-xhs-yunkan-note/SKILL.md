---
name: write-xhs-yunkan-note
description: Write Xiaohongshu promotion notes for YunKan Data based on ecommerce product data analysis. Use when the user wants a seed-style, high-conversion Xiaohongshu note focused on AI intelligent product selection, data visualization, decision shortcuts, Coupang crawler data, or avoiding sensitive/platform-banned wording.
---

# Write XHS YunKan Note

Write a Xiaohongshu note that promotes "云瞰数据" as a practical AI product-selection and Coupang data analysis tool.

## Required Prompt Intent

Follow this product-content prompt:

> 请根据我每次上传的爬虫数据(excel)，帮我写种草型的爆款转化笔记。聚焦 "AI智能选品" 核心卖点，采用 "数据可视化+决策捷径" 的种草逻辑，符合小红书高信息密度+强实用性的内容特性，笔记中要规避敏感词平台禁用词。

## Product Facts To Use

"云瞰数据" can capture Coupang product base data:

- id, sku, main image, product name
- delivery type
- price
- review count
- rating
- clicks
- sales

It uses AI to analyze market trends and help sellers shorten product-selection decisions.

## Writing Rules

- Write in simplified Chinese.
- Lead with a concrete pain point for cross-border sellers.
- Use "数据可视化 + 决策捷径" logic: show what the data reveals, then explain the action it enables.
- Keep the tone practical, dense, and useful, not exaggerated.
- Avoid absolute or risky claims such as "稳赚", "暴富", "最强", "第一", "百分百", "躺赚", "官方认证", "保证出单".
- Avoid promising unauthorized scraping, platform bypassing, or violating third-party rules.
- Do not fabricate exact metrics. If the analysis has exact numbers, cite them; otherwise use qualitative wording.
- Include a title, body, and hashtags.

## Output Format

Return:

1. `标题`: 2-3 options, each under 20 Chinese characters when possible.
2. `正文`: one polished Xiaohongshu note.
3. `封面文字`: 6-12 Chinese characters, strong but compliant.
4. `标签`: 8-12 hashtags.
5. `合规检查`: list any wording softened or avoided.

