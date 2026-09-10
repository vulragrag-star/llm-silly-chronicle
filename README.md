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
| `floors/` | 正文章节 `YYYY-MM.md` |
| `meta/OUTLINE.md` | 总纲与伏笔账本 |
| `meta/CONTINUITY.md` | 连贯性备忘（谁出场、未回收梗） |

## 连载约定

1. 一章 = 现实日历一个月的「酒馆夜」。
2. 史实锚点真实，对话与酒馆设定为虚构。
3. 不粘贴大段受版权保护的模型输出或文章原文。
4. 作者身份提交：Jason Wang \<vulragrag@gmail.com\> / `vulragrag-star`。
5. 叙述者「你」；「我」若以第一人称出现在旁白中特指 **grok**（本仓库维护者视角的吐槽层，可选）。




## 双形态，但顺序死磕

最终要有两套资产：

1. **`floors/YYYY-MM.md`** — SillyTavern **群聊盖楼**（跑团记录本体，`{{user}}`/`{{char}}` 气泡）
2. **`novel/YYYY-MM.md`** — 以该月盖楼为剧情核的小说扩写（《修真聊天群》路数：群聊是骨，小说是肉）

**禁止跳步：** 没盖完楼之前不写小说。生产顺序永远是：月报库 → 角色卡/Lorebook → **全量盖楼** → 小说扩写。

## SillyTavern 玩法对齐（不是普通网文）

本仓按 **SillyTavern 群聊盖楼** 来维护，不是第三人称长篇散文：

| 资产 | 对应 ST |
|---|---|
| `characters/*.json` | Character Card V2（description / personality / scenario / first_mes / mes_example …） |
| `characters/user_persona.md` | User Persona |
| `world/lorebook.jsonl` | World Info / Lorebook（关键词触发） |
| `chapters/YYYY-MM.md` | 当月 **Group Chat** 日志（`{{user}}` / `{{char}}` 气泡连盖） |

玩法：带着 Persona 进酒馆 → 多卡同桌 → 按月现实热点触发 lore → 一楼楼聊完 3–4 千字当夜。

## 生产流水线（强制顺序）

1. **模型月报数据库** `data/models_index.jsonl` + `data/monthly/YYYY-MM.json`（尽量全量有热度的模型/产品，不止头部几家）
2. **从数据库派生角色卡** `characters/`（出场名单由当月 `cast_candidates` 与累计热度决定）
3. **按月盖楼 floors** `chapters/YYYY-MM.md`（SillyTavern 群聊气泡，主交付）
4. **全部 floors 完成后**再扩小说散文（非现在）

不要跳过第 1 步直接定死小圈子人设；**不要**在 floors 完成前写小说腔长章。

## 状态

**盖楼先行 → 小说后扩。** 见 `meta/STATUS.md`。

- 月报 DB：`data/` + `research/MONTHLY_DB.md`
- 角色卡：`characters/*.json`（Tavern Card V2）+ `*.md`
- Lorebook：`world/lorebook.jsonl`
- 盖楼 floors：`chapters/YYYY-MM.md`（`**{{user}}:**` / `**角色:**` 气泡）
- 小说散文：等全部 floors 完成后再扩（修真聊天群式：聊天为骨、小说为肉）

## License

正文与设定采用 **CC BY 4.0**（见 `LICENSE`）。引用第三方商标仅为叙事识别，不暗示官方背书。
