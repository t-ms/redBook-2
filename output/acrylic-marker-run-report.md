# 丙烯马克笔完整流程验证记录

## 输入文件

`C:\Users\Administrator\Desktop\erp\丙烯马克笔_아크릴 마카펜_basic_20260508_163908.xlsx`

## 已完成

- 读取 Excel：254 行，22 个字段。
- 生成分析 JSON：`output/acrylic-marker-analysis.json`。
- 生成小红书文案：`output/yunkan-xhs-note.md`。
- 生成本地封面图：`output/acrylic-marker-cover.png`。
- 使用 Chrome 插件接管已登录的小红书创作页。
- 成功从“上传视频”切换到“上传图文”。

## 核心数据

- 价格：中位数 11650 韩元，最高 98500 韩元。
- 销量：中位数 35.5，最高 3031。
- 点击量：中位数 757.5，最高 32831。
- 评论数：中位数 10，最高 4223。
- 配送：韩国国内配送 252 条，海外配送 2 条。
- 火箭类型：橙火箭 178 条。

## 发现并修复的问题

- 原技能和脚本存在 UTF-8 乱码：已重写中文说明、列名别名和输出标签，并保存为 Windows 友好的 UTF-8。
- 原发布流程仍提示安装 Playwright：已改为使用 Codex Chrome 插件，不再要求 Playwright MCP。
- 仓库跟踪了 `.playwright-mcp` 运行产物：已移除并加入 `.gitignore`。
- 分析脚本原来依赖 `openpyxl`：已增加标准库 `.xlsx` 读取降级逻辑。
- Xiaohongshu 图文入口需要点可见 `上传图片` 按钮：已写入发布技能，避免点击隐藏 file input 后无响应。
- Chrome 插件上传图片时报 `Not allowed`：已在 README 和发布技能中加入明确修复提示，需要用户给 Codex Chrome 扩展开启文件 URL 访问权限。

## 当前阻塞

发布页已经登录且能操作，但封面上传被 Chrome 扩展权限阻止，无法继续填充并发布图文笔记。

修复方式：打开 `chrome://extensions`，进入 Codex 扩展 Details，开启 `Allow access to file URLs`，然后重新运行 `$publish-xhs-note`。

