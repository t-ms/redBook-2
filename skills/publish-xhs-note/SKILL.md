---
name: publish-xhs-note
description: Publish or prepare a Xiaohongshu note through the Codex Chrome plugin when the user asks to post, publish, upload, automate Xiaohongshu, use Chrome login state, attach a cover image, or fill Xiaohongshu note title/body/tags.
---

# Publish XHS Note

Use the Codex Chrome plugin for browser operations. This workflow depends on the user's real Chrome login state, so do not use the Playwright MCP server, the in-app browser, or a freshly launched unauthenticated browser for Xiaohongshu publishing.

## Required Browser Surface

- Use the `chrome:control-chrome` skill before browser work.
- Control Chrome through the Codex Chrome plugin and its `browser-client` runtime.
- It is acceptable that the Chrome plugin exposes a `tab.playwright` API internally; that is still Chrome plugin control, not Playwright MCP.
- If the Chrome plugin is unavailable, disconnected, or cannot see a logged-in Xiaohongshu tab/session, stop and tell the user what is missing.
- Do not ask the user to install Playwright for this plugin's publishing flow.
- If file upload fails with a permission error such as `Not allowed`, tell the user exactly: `To enable file upload, go to chrome://extensions in Chrome, click Details under the Codex extension, and enable "Allow access to file URLs." See https://developers.openai.com/codex/app/chrome-extension#upload-files for details.`

## Safety Gate

Before clicking the final publish button, ensure one of these is true:

- The user explicitly asked for direct publishing in the current turn.
- The user reviewed the final title, body, tags, and cover and approved publishing.

If neither is true, fill the draft and stop before the final publish action.

## Workflow

1. Connect to the user's Chrome session with the Codex Chrome plugin.
2. Reuse an existing Xiaohongshu creator tab when available; otherwise open the Xiaohongshu creator/publishing page in Chrome.
3. Confirm the page is logged in. If login, captcha, or verification is required, pause for the user.
4. Upload the generated cover image if available. On Xiaohongshu, prefer clicking the visible `上传图片` button to open the file chooser; clicking the hidden `input[type="file"]` may not trigger the chooser.
5. Fill:
   - title from the selected note title
   - body from the polished note
   - hashtags from the generated tag list
6. Check whether the page reports upload, content, or policy errors.
7. If direct publishing is approved, click publish and report the visible result. Otherwise, leave the draft ready for manual review.
8. Finalize Chrome tabs according to the `chrome:control-chrome` guidance: keep the publishing tab only when it is a deliverable or handoff.

## Xiaohongshu Layout Shortcuts

Use these shortcuts while the Xiaohongshu creator layout remains compatible.

### Switch From Video To Image-Text

The publish page may default to `上传视频`. To switch to image-text:

1. Take a fresh DOM snapshot.
2. Look for `上传图文` in the header tab area.
3. If multiple `上传图文` text matches exist, ignore offscreen matches with large negative coordinates.
4. Click the visible header tab near the top of the publish panel. In the observed layout it was the `.creator-tab` whose text is `上传图文`, around `x=385, y=81` in a 1912 px wide Chrome viewport.
5. Verify the upload area now says `上传图片，或写文字生成图片` and exposes the visible `上传图片` button.

### Upload Image

1. Click the visible button with accessible name `上传图片`.
2. Start `waitForEvent("filechooser")` before the click.
3. Use the returned chooser's `setFiles([...])` with an absolute local image path.
4. After upload, verify the page has entered edit mode by checking for:
   - `图片编辑`
   - title input placeholder `填写标题会有更多赞哦`
   - a `[contenteditable="true"]` body editor

### Click Final Publish

The final button is a custom element:

```html
<xhs-publish-btn
  is-publish="true"
  is-save-draft="true"
  submit-text="发布"
  save-text="暂存离开"
  submit-disabled="false"
  save-disabled="false">
</xhs-publish-btn>
```

This element uses a closed shadow DOM. Normal DOM snapshots and `locator('xhs-publish-btn').click()` may not click the internal `发布` button.

Use the component rectangle and the known internal layout:

- Host height: `90`
- Internal buttons: two `120 x 40` buttons
- Gap between buttons: `24`
- Left button: `暂存离开`
- Right red button: `发布`
- Publish button center:

```text
x = hostRect.x + (hostRect.width / 2) + 72
y = hostRect.y + 45
```

Before clicking, verify:

- `submit-disabled="false"`
- `submit-text="发布"`
- No visible upload/content/policy error text

After clicking, verify success by checking for either:

- URL containing `/publish/success`
- visible text `发布成功`

## Constraints

- Do not bypass login, captcha, rate limits, or platform review.
- Do not create or rotate accounts.
- Do not mass-post the same content.
- Do not hide the fact that content is promotional.
- Do not inspect cookies, local storage, passwords, or Chrome profile files.
- If browser automation cannot access the logged-in account, tell the user what state is missing.


