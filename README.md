# YunKan XHS Growth Codex Plugin

This plugin helps Codex analyze Coupang product Excel data and create a Xiaohongshu promotion workflow for "云瞰数据".

## What It Provides

- Excel/CSV analysis for Coupang product fields: id, sku, main image, product name, delivery type, price, reviews, rating, clicks, and sales.
- Xiaohongshu note generation focused on "AI智能选品", "数据可视化", and "决策捷径".
- Xiaohongshu cover image generation guidance for image-generation tools.
- Browser-assisted Xiaohongshu draft filling or publishing through an already logged-in account.
- A clear Playwright dependency warning when automated browser publishing is requested but Playwright is not installed.

## Skills

- `$xhs-yunkan-campaign`: end-to-end workflow.
- `$analyze-coupang-excel`: spreadsheet analysis.
- `$write-xhs-yunkan-note`: promotional note writing.
- `$generate-xhs-cover`: cover image generation.
- `$publish-xhs-note`: browser-based Xiaohongshu posting workflow.

## Install From Git

Publish this repository to GitHub, then install the plugin from the repository URL in Codex's plugin flow.

For local testing, keep this folder as the plugin root. The required manifest is at:

```text
.codex-plugin/plugin.json
```

## Usage Example

```text
Use $xhs-yunkan-campaign to analyze this Coupang Excel file, write a Xiaohongshu note for 云瞰数据, generate a cover image, and prepare it in my logged-in Xiaohongshu account.
```

The publishing skill prepares a draft by default and only clicks the final publish button after explicit approval or a direct-publish request.

## Browser Automation Dependency

If Playwright is not installed in the active environment, the publishing skill should tell the user to install it before attempting browser automation:

```text
npm i -D playwright
npx playwright install chromium
```
