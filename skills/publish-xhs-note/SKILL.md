---
name: publish-xhs-note
description: Publish or prepare a Xiaohongshu note through a browser session that is already logged into Xiaohongshu. Use when the user asks to post, publish, upload, automate Xiaohongshu, use Chrome/browser login state, attach a cover image, or fill Xiaohongshu note title/body/tags.
---

# Publish XHS Note

Use a browser tool that can access the user's logged-in Xiaohongshu session. Prefer Chrome automation when login cookies matter; use the in-app browser only if the user is already logged in there.

## Browser Automation Dependency

When browser publishing requires Playwright and the current environment does not have Playwright installed or importable:

- Tell the user that Playwright is missing before attempting browser automation.
- Ask the user to install it with the environment-appropriate command, usually `npm i -D playwright` for a project dependency or `npm i -g playwright` for a global CLI-style setup.
- If browser binaries are also missing, tell the user to run `npx playwright install chromium`.
- Continue with a manual publishing package instead of pretending automation can proceed.
- Do not silently fall back to an unauthenticated browser if the task depends on the user's logged-in Xiaohongshu session.

## Safety Gate

Before clicking the final publish button, ensure one of these is true:

- The user explicitly asked for direct publishing in the current turn.
- The user reviewed the final title, body, tags, and cover and approved publishing.

If neither is true, fill the draft and stop before the final publish action.

## Workflow

1. Open Xiaohongshu creator/publishing page in the logged-in browser.
2. Upload the generated cover image if available.
3. Fill:
   - title from the selected note title
   - body from the polished note
   - hashtags from the generated tag list
4. Check whether the page reports upload, content, or policy errors.
5. If direct publishing is approved, click publish and report the result. Otherwise, leave the draft ready for manual review.

## Constraints

- Do not bypass login, captcha, rate limits, or platform review.
- Do not create or rotate accounts.
- Do not mass-post the same content.
- Do not hide the fact that content is promotional.
- If browser automation cannot access the logged-in account, tell the user what state is missing.
