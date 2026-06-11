---
name: xhs-yunkan-campaign
description: End-to-end YunKan Data Xiaohongshu campaign workflow. Use when the user wants to upload Coupang Excel data, analyze cross-border ecommerce product trends, generate a Xiaohongshu promotional note, create an image2/AI cover image, and optionally publish through a logged-in Xiaohongshu browser account.
---

# XHS YunKan Campaign

Coordinate the full workflow by invoking the plugin's focused skills as needed.

## Workflow

1. Analyze the uploaded product spreadsheet with `$analyze-coupang-excel`.
2. Draft the Xiaohongshu note with `$write-xhs-yunkan-note`.
3. Generate the cover image with `$generate-xhs-cover`.
4. Prepare or publish the note with `$publish-xhs-note` when the user asks for browser posting.

## Defaults

- Language: simplified Chinese.
- Audience: Coupang and cross-border ecommerce sellers who need faster product-selection decisions.
- Positioning: "云瞰数据" is a crawler/data-analysis assistant for AI intelligent product selection.
- Publishing behavior: prepare draft by default; click final publish only after explicit approval or an explicit direct-publish request.

## Final Response

Summarize:

- top data insight
- selected title
- generated cover path or prompt
- whether the Xiaohongshu post is drafted or published
- any missing dependency, login, or compliance issue

