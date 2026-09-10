# SillyTavern 实务笔记（维护者）

本仓库的**主交付物是盖楼 floors**（群聊跑团记录），不是先写第三人称小说。小说扩写排在全部盖楼之后。

## 角色卡（Character Card V2）

- 路径：`characters/<id>.json` + 人读镜像 `characters/<id>.md`
- 规格：`spec: "chara_card_v2"` / `spec_version: "2.0"`，正文在 `data.*`
- 必填六弦：`name` `description` `personality` `scenario` `first_mes` `mes_example`
- V2 常用：`system_prompt` `post_history_instructions` `alternate_greetings` `tags` `creator` `character_version` `creator_notes` `extensions`
- 本仓在 `extensions.llm_silly_chronicle` 挂 DB id / presence / enter_months
- **不要**把 `creator_notes` 当模型提示（ST 默认不喂给模型）

### 字段怎么用在盖楼里

| 字段 | 用途 |
|---|---|
| description | 外貌/设定/DB来历，常进主提示 |
| personality | 气质+口癖+强弱项 |
| scenario | 固定「模型酒馆」群聊场景 |
| first_mes | 单卡开场；群聊开场改用章节里的群体入场 |
| mes_example | 少而密的对话样例，教会气泡节奏 |
| system_prompt | 强化「短气泡、不剧透、不代打 {{user}}」 |

## 用户人设（Persona）

- `characters/_USER_PERSONA.json`：酒馆常客，第二人称 `{{user}}`
- 盖楼里用户气泡写：`**{{user}}:** …`

## Lorebook / World Info

- `world/lorebook.jsonl`：一行一条
- 关键字段：`key`（触发词）、`content`、`constant`（常驻）、`insertion_order`、`comment`
- 每月一条 `month-YYYY-MM`，关键词含月份、headline 片段、事件标题、梗 tag
- 写某月 floor 时：把该月 lore + 在场角色卡装进 ST World Info / 或人工对照 DB

## Group Chat 盖楼格式（强制）

```text
# YYYY-MM · <headline>

> 酒馆地板 · cast: id1, id2, …
> 形式：SillyTavern Group Chat（非小说正文）

**{{user}}:** …
**ChatGPT:** …
**Claude:** …
*旁白/动作可短，勿写成章节散文*
```

- 目标体量：约 **3000–4000 汉字**/月
- 只准使用当月及以前的史实锚点（`data/monthly/YYYY-MM.json`）
- 角色口吻贴合卡片；龙套用 DB `cast_candidates`，**禁止发明 DB 外模型**
- Grok Bot：最多一拍 meta wink

## Swipe / 续写约定

- 同一月可以 swipe 开场，但仓库只保留一条 canonical floor：`chapters/YYYY-MM.md`
- 续写下一月前读：`meta/CONTINUITY.md` + 上月 floor 结尾 + 当月 lore

## 流水线

1. Monthly DB（已有）
2. ST cards + lorebook + user persona
3. **盖楼 floors 月月写完** ← 当前主线
4. 全部完成后再扩「修真聊天群」式小说（聊天为骨、小说为肉）

## 导入 ST 的提示

- 单卡：导入 `characters/*.json`（或将来打包 PNG）
- 群聊：自建 Group，拉当月 cast；World Info 导入当月相关 lore 条目
- 本仓库 chapters 是**导出的跑团记录**，可当示例 transcript，不必反向依赖 ST 软件才能阅读
