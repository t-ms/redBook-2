---
name: generate-xhs-cover
description: Generate or prompt an image-generation tool for a Xiaohongshu cover based on ecommerce product-selection analysis. Use when the user asks for image2, image generation, cover art, poster, thumbnail, or a Xiaohongshu-style visual for Coupang data analysis, and ensure generated cover images contain no "云瞰数据" text.
---

# Generate XHS Cover

Use the available image generation tool to create a Xiaohongshu-friendly cover image from the product-selection analysis.

## Hard Brand Rule

- Do not put "云瞰数据" anywhere in the image prompt, visible poster text, title, subtitle, badge, watermark, or filename recommendation.
- Do not use a replacement brand alias. The cover should look like an operator's data recap, not a branded ad.

## Cover Direction

Create a vertical 3:4 cover suitable for Xiaohongshu feed promotion:

- Subject: cross-border ecommerce seller reviewing a product-selection data dashboard.
- Visuals: clean dashboard, product cards, trend chart, SKU table, price band, rating, reviews, clicks, sales, and conversion signals.
- Text style: short human headline such as "别只看热度", "销量转化一起看", or "这个品先别急冲".
- Style: bright, practical, clean, high-information Chinese social commerce poster.
- Avoid: fake platform logos, real marketplace logos, brand names, exaggerated money imagery, prohibited claims, or text that promises outcomes.

## Suggested Prompt Template

Use this as the base prompt and adapt it to the actual note:

```text
竖版3:4小红书封面，主题是跨境电商选品复盘。画面中心是一位运营者在查看现代数据看板，看板包含商品卡片、价格区间、评分、评论数、点击量、销量、转化率和趋势折线图。整体风格明亮、干净、专业、高信息密度，像真实运营复盘而不是广告海报。主标题文字："{cover_text}"。副标题文字："销量和转化一起看"。不出现任何品牌名，不出现“云瞰数据”字样，不出现真实平台 logo，不承诺暴利，不使用夸张现金元素。
```

## After Generation

Show the generated image path or markdown image preview when available. If the tool only returns a prompt, provide the final prompt and ask the user to run it in their preferred image generator.
