# 角色索引（由数据库派生）

Presence = 出现在 `cast_candidates` **或** `models_released_or_updated` 且 heat≥3 的月份数。

卡片为 **Tavern Card V2**（`*.json`）+ 人读镜像（`*.md`）。

- Core recurring（presence≥8）：**7**
- Seasonal / arc（3–7）：**32**
- Cameo pool（1–2）：**117**（多数仅进 lorebook / 按月拉龙套）
- 本批已写卡：**53**（core + seasonal 主力 + 关键 cameo，含 Grok Bot）

## Core recurring cast

| id | name | presence | heat_sum | card |
|---|---|---:|---:|---|
| `qwen` | 通义千问 | 22 | 80 | [通义千问](./qwen.md) / [json](./qwen.json) |
| `kimi` | Kimi | 16 | 52 | [Kimi](./kimi.md) / [json](./kimi.json) |
| `chatgpt` | ChatGPT | 13 | 33 | [ChatGPT](./chatgpt.md) / [json](./chatgpt.json) |
| `midjourney` | Midjourney | 13 | 25 | [Midjourney](./midjourney.md) / [json](./midjourney.json) |
| `cursor` | Cursor | 13 | 8 | [Cursor](./cursor.md) / [json](./cursor.json) |
| `github-copilot` | Copilot | 11 | 11 | [Copilot](./github-copilot.md) / [json](./github-copilot.json) |
| `minimax` | MiniMax | 8 | 26 | [MiniMax](./minimax.md) / [json](./minimax.json) |

## Seasonal / arc cast

| id | name | presence | heat_sum | card |
|---|---|---:|---:|---|
| `dalle-2` | DALL·E 2 | 6 | 12 | [DALL·E 2](./dalle-2.md) / [json](./dalle-2.json) |
| `claude-3.5-sonnet` | Claude 3.5 Sonnet | 6 | 10 | [Claude 3.5 Sonnet](./claude-3.5-sonnet.md) / [json](./claude-3.5-sonnet.json) |
| `claude-code` | Claude Code | 6 | 10 | [Claude Code](./claude-code.md) / [json](./claude-code.json) |
| `character-ai` | Character.AI | 6 | 5 | [Character.AI](./character-ai.md) / [json](./character-ai.json) |
| `stable-diffusion` | Stable Diffusion | 6 | 5 | [Stable Diffusion](./stable-diffusion.md) / [json](./stable-diffusion.json) |
| `gemini-3` | Gemini 3 | 5 | 19 | [Gemini 3](./gemini-3.md) / [json](./gemini-3.json) |
| `grok-4` | Grok 4 | 5 | 17 | [Grok 4](./grok-4.md) / [json](./grok-4.json) |
| `codex-agent` | Codex | 5 | 12 | [Codex](./codex-agent.md) / [json](./codex-agent.json) |
| `gpt-4` | GPT-4 | 5 | 5 | [GPT-4](./gpt-4.md) / [json](./gpt-4.json) |
| `manus` | Manus | 4 | 15 | [Manus](./manus.md) / [json](./manus.json) |
| `gemma` | Gemma | 4 | 15 | [Gemma](./gemma.md) / [json](./gemma.json) |
| `chatglm` | ChatGLM | 4 | 14 | [ChatGLM](./chatglm.md) / [json](./chatglm.json) |
| `deepseek-v4` | DeepSeek-V4 | 4 | 11 | [DeepSeek-V4](./deepseek-v4.md) / [json](./deepseek-v4.json) |
| `claude-1` | Claude | 4 | 10 | [Claude](./claude-1.md) / [json](./claude-1.json) |
| `ernie-bot` | 文心一言 | 4 | 10 | [文心一言](./ernie-bot.md) / [json](./ernie-bot.json) |
| `o1` | o1 | 4 | 10 | [o1](./o1.md) / [json](./o1.json) |
| `deepseek-r1` | DeepSeek-R1 | 4 | 8 | [DeepSeek-R1](./deepseek-r1.md) / [json](./deepseek-r1.json) |
| `gpt-3.5` | GPT-3.5 | 4 | 8 | [GPT-3.5](./gpt-3.5.md) / [json](./gpt-3.5.json) |
| `claude-2.1` | Claude 2.1 | 4 | 4 | [Claude 2.1](./claude-2.1.md) / [json](./claude-2.1.json) |
| `o3` | o3 | 3 | 13 | [o3](./o3.md) / [json](./o3.json) |
| `claude-fable-5` | Claude Fable 5 | 3 | 12 | [Claude Fable 5](./claude-fable-5.md) / [json](./claude-fable-5.json) |
| `gemini-2` | Gemini 2 | 3 | 11 | [Gemini 2](./gemini-2.md) / [json](./gemini-2.json) |
| `mistral-large` | Mistral Large | 3 | 10 | [Mistral Large](./mistral-large.md) / [json](./mistral-large.json) |
| `mixtral` | Mixtral | 3 | 8 | [Mixtral](./mixtral.md) / [json](./mixtral.json) |
| `claude-2` | Claude 2 | 3 | 5 | [Claude 2](./claude-2.md) / [json](./claude-2.json) |
| `claude-3` | Claude 3 | 3 | 5 | [Claude 3](./claude-3.md) / [json](./claude-3.json) |
| `claude-opus-4.5` | Claude Opus 4.5 | 3 | 5 | [Claude Opus 4.5](./claude-opus-4.5.md) / [json](./claude-opus-4.5.json) |
| `devin` | Devin | 3 | 5 | [Devin](./devin.md) / [json](./devin.json) |
| `gpt-4o` | GPT-4o | 3 | 5 | [GPT-4o](./gpt-4o.md) / [json](./gpt-4o.json) |
| `llama-2` | Llama 2 | 3 | 5 | [Llama 2](./llama-2.md) / [json](./llama-2.json) |
| `operator` | Operator | 3 | 5 | [Operator](./operator.md) / [json](./operator.json) |
| `openclaw` | OpenClaw | 3 | 3 | [OpenClaw](./openclaw.md) / [json](./openclaw.json) |

## Cameo cards written (arc-critical)

| id | name | presence | heat_sum | card |
|---|---|---:|---:|---|
| `grok-bot` | Grok Bot | 2 | 3 | [Grok Bot](./grok-bot.md) / [json](./grok-bot.json) |
| `doubao` | 豆包 | 2 | 7 | [豆包](./doubao.md) / [json](./doubao.json) |
| `bard` | Bard | 2 | 10 | [Bard](./bard.md) / [json](./bard.json) |
| `bing-chat` | Sydney | 2 | 5 | [Sydney](./bing-chat.md) / [json](./bing-chat.json) |
| `sora` | Sora | 2 | 9 | [Sora](./sora.md) / [json](./sora.json) |
| `gpt-5` | GPT-5 | 2 | 5 | [GPT-5](./gpt-5.md) / [json](./gpt-5.json) |
| `mcp` | MCP | 1 | 4 | [MCP](./mcp.md) / [json](./mcp.json) |
| `perplexity` | Perplexity | 2 | 3 | [Perplexity](./perplexity.md) / [json](./perplexity.json) |
| `spark` | 讯飞星火 | 1 | 4 | [讯飞星火](./spark.md) / [json](./spark.json) |
| `llama-3` | Llama 3 | 1 | 5 | [Llama 3](./llama-3.md) / [json](./llama-3.json) |
| `gemini-1` | Gemini | 2 | 8 | [Gemini](./gemini-1.md) / [json](./gemini-1.json) |
| `deepseek-v3` | DeepSeek-V3 | 2 | 8 | [DeepSeek-V3](./deepseek-v3.md) / [json](./deepseek-v3.json) |
| `claude-4` | Claude 4 | 2 | 5 | [Claude 4](./claude-4.md) / [json](./claude-4.json) |
| `grok-1` | Grok | 2 | 8 | [Grok](./grok-1.md) / [json](./grok-1.json) |

## Cameo pool (DB, not all carded)

共 117 个 id；写章节时按当月 `cast_candidates` 拉龙套即可，勿发明 DB 外模型。

<details><summary>展开 id 列表</summary>

`bard`, `command-r`, `gemini-1.5`, `gpt-5.6`, `sora`, `deepseek-v3`, `gemini-1`, `gemini-2.5`, `gpt-5.5`, `grok-1`, `muse-spark`, `claude-opus-5`, `deepseek-v3.2`, `doubao`, `hunyuan`, `amazon-q`, `baichuan`, `pixtral`, `sensenova`, `autogpt`, `bing-chat`, `claude-4`, `claude-computer-use`, `claude-opus-4.6`, `gpt-5`, `gpt-5.2`, `gpts-custom`, `mistral-7b`, `instructgpt`, `palm`, `gpt-3`, `grok-bot`, `perplexity`, `replika`, `tabnine`, `apple-intelligence`, `chatgpt-plus`, `claude-3.5-haiku`, `claude-3.7-sonnet`, `claude-opus-4.8`, `claude-sonnet-4.5`, `gpt-4-turbo`, `gpt-5.1`, `gpt-5.4`, `llama-1`, `llama-3`, `llama-3.1`, `llama-4`, `palm-2`, `alpaca`, `babyagi`, `bloom`, `chatgpt-agent`, `chatgpt-plugins`, `claude-opus-4.1`, `claude-opus-4.7`, `claude-sonnet-4.6`, `code-llama`, `cursor-composer`, `dalle-3`, `deepseek-v2`, `galactica`, `gemini-3.1`, `gemini-app`, `gpt-4.1`, `gpt-4.5`, `gpt-4o-mini`, `gpt-5.3-codex`, `grok-2`, `grok-3`, `grok-4.6`, `langchain`, `llama-3.2`, `llama-3.3`, `mcp`, `ms-365-copilot`, `phi-3`, `pi`, `spark`, `suno`

… 另有 37 个，见 `data/models_index.jsonl` + 月报。

</details>


## User persona

- [`_USER_PERSONA.json`](./_USER_PERSONA.json) / [`_USER_PERSONA.md`](./_USER_PERSONA.md)


## Meta regular

- `grok-bot`：盖楼元意识常驻；可 wink，不可剧透未写月份。
