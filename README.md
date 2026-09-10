# 模型酒馆编年史 · LLM Silly Chronicle

一部以**用户视角**连载的趣味长篇：把 GPT、Claude、Gemini、DeepSeek、Cursor、Codex、OpenClaw、Grok Bot 等写成可互动的电子形象，在「酒馆」里盖楼。

- **体裁**：SillyTavern / 盖楼式互动小说（中文）
- **时间轴**：自 2022 年起，**每月一章**（约 3000–4000 字），剧情连续
- **叙事**：第二人称用户带入；角色口吻贴合当时社区风评与梗
- **开源维护**：大纲、人设、章节正文均在本仓；欢迎纠错史实/补梗（请开 Issue）

## 目录

| 路径 | 说明 |
|---|---|
| `research/` | 时间线、人设调研、写作技法 |
| `characters/` | 角色卡（ST 风格） |
| `chapters/` | 正文章节 `YYYY-MM.md` |
| `meta/OUTLINE.md` | 总纲与伏笔账本 |
| `meta/CONTINUITY.md` | 连贯性备忘（谁出场、未回收梗） |

## 连载约定

1. 一章 = 现实日历一个月的「酒馆夜」。
2. 史实锚点真实，对话与酒馆设定为虚构。
3. 不粘贴大段受版权保护的模型输出或文章原文。
4. 作者身份提交：Jason Wang \<vulragrag@gmail.com\> / `vulragrag-star`。
5. 叙述者「你」；「我」若以第一人称出现在旁白中特指 **grok**（本仓库维护者视角的吐槽层，可选）。


## 生产流水线（强制顺序）

1. **模型月报数据库** `data/models_index.jsonl` + `data/monthly/YYYY-MM.json`（尽量全量有热度的模型/产品，不止头部几家）
2. **从数据库派生角色卡** `characters/`（出场名单由当月 `cast_candidates` 与累计热度决定）
3. **按月连载正文** `chapters/YYYY-MM.md`

不要跳过第 1 步直接定死小圈子人设。

## 状态

脚手架搭建中；调研与前几章并行生产。见 `meta/STATUS.md`。

## License

正文与设定采用 **CC BY 4.0**（见 `LICENSE`）。引用第三方商标仅为叙事识别，不暗示官方背书。
