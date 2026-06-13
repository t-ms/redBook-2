# YunKan XHS Growth Codex Plugin

This plugin helps Codex analyze Coupang product Excel data and create Xiaohongshu-ready product-selection content.

## What It Provides

- Excel/CSV analysis for Coupang product fields: id, sku, main image, product name, delivery type, price, reviews, rating, clicks, sales, and conversion.
- Xiaohongshu note generation from product data, written like a practical operator recap instead of a hard-sell AI draft.
- Cover image generation guidance for Xiaohongshu-style product-selection posts.
- Chrome-assisted Xiaohongshu draft filling or publishing through an already logged-in account.

## Content Rules

- Generated public-facing titles, body text, hashtags, cover text, and image prompts must not contain `云瞰数据`.
- Copy should feel human: specific observations, modest claims, fewer slogans, and no obvious AI-flavored wording.
- Avoid absolute or risky claims such as guaranteed sales, easy profit, or platform endorsement.

## Skills

- `$xhs-yunkan-campaign`: end-to-end workflow.
- `$analyze-coupang-excel`: spreadsheet analysis.
- `$write-xhs-yunkan-note`: Xiaohongshu note writing.
- `$generate-xhs-cover`: cover image generation.
- `$publish-xhs-note`: Chrome-based Xiaohongshu posting workflow.

## Install From Git

Install this plugin from:

```text
https://github.com/t-ms/redBook-2.git
```

For local testing, keep this folder as the plugin root. The required manifest is at:

```text
.codex-plugin/plugin.json
```

## Usage And Triggering

The most reliable trigger is to name the end-to-end skill:

```text
Use $xhs-yunkan-campaign to analyze this Coupang Excel file, write a natural Xiaohongshu note, generate a cover image, and prepare it in my logged-in Xiaohongshu account.
```

Natural-language requests can also trigger the plugin when they match the skill descriptions, for example:

```text
帮我分析这个 Coupang 商品 Excel，写一篇小红书选品笔记，生成封面，并用我已登录的小红书账号发布。
```

## Chrome Publishing

Publishing uses the Codex Chrome plugin so it can work with the user's real logged-in Xiaohongshu session. The publishing skill must not use the Playwright MCP server or a newly launched unauthenticated browser.

If Chrome is not connected, the Xiaohongshu account is not logged in, or a captcha/verification page appears, the skill should pause and tell the user what is missing.

If image upload fails with a Chrome extension permission error, open `chrome://extensions`, click Details under the Codex extension, and enable "Allow access to file URLs." See https://developers.openai.com/codex/app/chrome-extension#upload-files for details.

The publishing skill prepares a draft by default and only clicks the final publish button after explicit approval or a direct-publish request.

## Repository Hygiene

Do not commit browser runtime artifacts such as `.playwright-mcp/`, screenshots created only for debugging, Chrome profile files, cookies, or session data.


