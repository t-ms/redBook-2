---
name: write-xhs-yunkan-note
description: Write Xiaohongshu notes based on ecommerce product data analysis. Use when the user wants a seed-style, conversion-oriented Xiaohongshu note from Coupang crawler data, with a natural human voice, low AI flavor, practical selection logic, and no outward mention of the brand name "云瞰数据".
---

# Write XHS Note

Write a Xiaohongshu note from ecommerce product analysis. The internal product context may be about a crawler/data-analysis tool, but the outward note must read like a real operator's selection recap, not like software advertising.

## Hard Brand Rule

- Do not include the text "云瞰数据" anywhere in generated outward content.
- Apply this to title options, body, cover text, hashtags, image prompts, captions, and publishing drafts.
- Do not replace it with a near-synonym brand alias. Use neutral terms such as "这份数据", "商品表", "后台数据", "选品表", or "这次抓到的数据".

## Writing Intent

Use each uploaded crawler spreadsheet to write a practical, seed-style Xiaohongshu note for cross-border sellers. Focus on product-selection reasoning from data, especially clicks, sales, reviews, rating, conversion, price band, delivery type, and visible demand signals.

## Human Voice Rules

- Write in simplified Chinese.
- Sound like a real operator sharing a recent finding: slightly conversational, specific, and grounded.
- Prefer "我这次看下来", "这个点挺容易误判", "我会先看", "值得再拆" over abstract marketing phrases.
- Avoid stiff phrases such as "赋能", "闭环", "链路", "降本增效", "矩阵化", "数据可视化+决策捷径".
- Avoid repeatedly saying "AI". If needed, mention "工具辅助整理" or "把数据先跑一遍".
- Keep claims modest. Do not promise results.
- Do not fabricate exact metrics. Use exact numbers only when they appear in the analysis.
- Include small caveats when useful, for example "价格为 0 的样本要单独复核".

## Compliance Rules

- Avoid absolute or risky claims such as "稳赚", "暴富", "最强", "第一", "百分百", "躺赚", "官方认证", "保证出单".
- Avoid promising unauthorized scraping, platform bypassing, or violating third-party rules.
- Avoid sounding like a hard sell. The note should feel like an observation and method share.

## Output Format

Return:

1. `标题`: 2-3 natural options, each under 20 Chinese characters when possible.
2. `正文`: one polished Xiaohongshu note under 1000 Chinese characters unless the user asks otherwise.
3. `封面文字`: 6-12 Chinese characters, no brand name.
4. `标签`: 8-12 hashtags, no brand name.
5. `合规检查`: list wording softened or avoided.
