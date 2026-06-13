---
name: xhs-yunkan-campaign
description: End-to-end Xiaohongshu campaign workflow for Coupang product data. Use when the user wants to upload Coupang Excel data, analyze cross-border ecommerce trends, generate a natural Xiaohongshu note, create an image2/AI cover image with no "云瞰数据" text, and optionally publish through a logged-in Chrome Xiaohongshu account.
---

# XHS Campaign

Coordinate the full workflow by invoking the plugin's focused skills as needed.

## Workflow

1. Analyze the uploaded product spreadsheet with `$analyze-coupang-excel`.
2. Draft the Xiaohongshu note with `$write-xhs-yunkan-note`.
3. Generate the cover image with `$generate-xhs-cover`.
4. Prepare or publish the note with `$publish-xhs-note` when the user asks for browser posting.

## Defaults

- Language: simplified Chinese.
- Audience: Coupang and cross-border ecommerce sellers who need faster product-selection decisions.
- Outward content: do not include "云瞰数据" in generated images, titles, body text, tags, or publishing drafts.
- Voice: use a natural operator recap style; avoid obvious AI-generated or hard-sell wording.
- Publishing browser: use the Codex Chrome plugin, because Xiaohongshu publishing depends on the user's logged-in Chrome session.
- Publishing behavior: prepare draft by default; click final publish only after explicit approval or an explicit direct-publish request.

## Final Response

Summarize:

- top data insight
- selected title
- generated cover path or prompt
- whether the Xiaohongshu post is drafted or published
- any missing Chrome, login, upload, or compliance issue


