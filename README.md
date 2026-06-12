# YunKan XHS Growth Codex Plugin

This plugin helps Codex analyze Coupang product Excel data and create Xiaohongshu-ready product-selection content.

## What It Provides

- Excel/CSV analysis for Coupang product fields: id, sku, main image, product name, delivery type, price, reviews, rating, clicks, and sales.
- Xiaohongshu note generation from product data, written like a practical operator recap instead of a hard-sell AI draft.
- Cover image generation guidance for Xiaohongshu-style product-selection posts.
- Browser-assisted Xiaohongshu draft filling or publishing through an already logged-in account.
- A clear Playwright dependency warning when automated browser publishing is requested but Playwright is not installed.

## Content Rules

- Generated public-facing titles, body text, hashtags, cover text, and image prompts must not contain `云瞰数据`.
- Copy should feel human: specific observations, modest claims, fewer slogans, and no obvious AI-flavored wording.
- Avoid absolute or risky claims such as guaranteed sales, easy profit, or platform endorsement.

## Skills

- `$xhs-yunkan-campaign`: end-to-end workflow.
- `$analyze-coupang-excel`: spreadsheet analysis.
- `$write-xhs-yunkan-note`: Xiaohongshu note writing.
- `$generate-xhs-cover`: cover image generation.
- `$publish-xhs-note`: browser-based Xiaohongshu posting workflow.

## Install From Git

Install this plugin from:

```text
https://github.com/t-ms/redBook-2.git
```

For local testing, keep this folder as the plugin root. The required manifest is at:

```text
.codex-plugin/plugin.json
```

## Usage Example

```text
Use $xhs-yunkan-campaign to analyze this Coupang Excel file, write a natural Xiaohongshu note, generate a cover image, and prepare it in my logged-in Xiaohongshu account.
```

The publishing skill prepares a draft by default and only clicks the final publish button after explicit approval or a direct-publish request.

## Browser Automation Dependency

If Playwright is not installed in the active environment, the publishing skill should tell the user to install it before attempting browser automation:

```text
npm i -D playwright
npx playwright install chromium
```
