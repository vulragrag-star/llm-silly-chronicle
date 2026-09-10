# Monthly Model Report Database

Research substrate for *LLM Silly Chronicle* (Chinese long-form humorous multi-persona novel).
**Character cards are NOT finalized here** — derive cast from coverage/heat after this DB.

## Layout

| Path | Purpose |
|------|---------|
| [`data/models_index.jsonl`](../data/models_index.jsonl) | One row per model/product/tool |
| [`data/monthly/YYYY-MM.json`](../data/monthly/) | Per-month releases, events, memes, cast candidates |
| `scripts/build_monthly_db.py` / `build_months_rest.py` | Generators used this run |

## Coverage stats (this run)

- **Months:** 57 complete (`2022-01` … `2026-09`)
- **Models/products indexed:** 180
- **Kinds:** agent=16, app=29, audio=5, ide=9, image=6, llm=104, other=5, video=6
- **Vendors (top):** OpenAI (32), Anthropic (22), Google (16), Meta (12), xAI (10), DeepSeek (9), Microsoft (7), Mistral AI (5), Anysphere (3), Cohere (2), Inflection (2), GitHub/Microsoft (2)
- **Avg update heat:** 3.87
- **Months with ≥1 heat-5 drop:** 43

### Schema reminders

**models_index.jsonl fields:** `id`, `name`, `vendor`, `kind` (`llm|image|video|audio|agent|ide|app|other`), `first_seen_month`, `aliases`, `notes`

**monthly JSON fields:** `month`, `headline`, `models_released_or_updated[{id,what_changed,heat:1-5}]`, `events[{date?,title,summary,links[]}]`, `memes_and_discourse[{tag,note}]`, `community_sentiment`, `cast_candidates[]`

Heat rubric (fiction utility, not benchmark score): 1=niche, 3=notable, 5=era-defining / high meme potential.

Uncertain items are flagged in `notes` / event summaries with wording like *verify* / *approx* / *reports*.

## Provisional cast ranking (by DB heat×presence — NOT final CHARACTERS.md)

Use this only as a shortlist for later persona cards. Broad cast intentional.

| Rank | id | score |
|------|----|-------|
| 1 | `chatgpt` | 109 |
| 2 | `cursor` | 64 |
| 3 | `midjourney` | 31 |
| 4 | `doubao` | 28 |
| 5 | `codex-agent` | 24 |
| 6 | `kimi` | 22 |
| 7 | `openclaw` | 20 |
| 8 | `github-copilot` | 19 |
| 9 | `qwen` | 19 |
| 10 | `sora` | 18 |
| 11 | `claude-3.5-sonnet` | 18 |
| 12 | `bard` | 17 |
| 13 | `gpt-5.6` | 16 |
| 14 | `grok-1` | 15 |
| 15 | `composer-model` | 15 |
| 16 | `dalle-2` | 14 |
| 17 | `claude-1` | 14 |
| 18 | `o1` | 14 |
| 19 | `deepseek-r1` | 14 |
| 20 | `gemini-1` | 13 |
| 21 | `claude-code` | 13 |
| 22 | `ernie-bot` | 12 |
| 23 | `gpts-custom` | 12 |
| 24 | `gpt-5` | 12 |
| 25 | `stable-diffusion` | 11 |
| 26 | `character-ai` | 11 |
| 27 | `dalle-3` | 11 |
| 28 | `o3` | 11 |
| 29 | `spark` | 10 |
| 30 | `mcp` | 10 |
| 31 | `gpt-3.5` | 9 |
| 32 | `gpt-4` | 9 |
| 33 | `gpt-4o` | 9 |
| 34 | `claude-4` | 9 |
| 35 | `claude-2` | 8 |
| 36 | `gemini-app` | 8 |
| 37 | `claude-3` | 8 |
| 38 | `operator` | 8 |
| 39 | `deepseek-v4` | 8 |
| 40 | `claude-opus-5` | 8 |

## Month index

| Month | Headline | #models | #events | #memes | #cast | max heat | File |
|-------|----------|---------|---------|--------|-------|----------|------|
| 2022-01 | InstructGPT ships; RLHF quietly becomes the new default | 2 | 1 | 2 | 5 | 4 | [`2022-01.json`](../data/monthly/2022-01.json) |
| 2022-02 | Midjourney V1 era begins in Discord | 1 | 1 | 1 | 4 | 3 | [`2022-02.json`](../data/monthly/2022-02.json) |
| 2022-03 | GPT-3.5 lineage; ChatGLM research; Copilot expands | 3 | 1 | 1 | 4 | 3 | [`2022-03.json`](../data/monthly/2022-03.json) |
| 2022-04 | PaLM 540B + DALL·E 2 + Midjourney V2 | 3 | 2 | 2 | 5 | 5 | [`2022-04.json`](../data/monthly/2022-04.json) |
| 2022-05 | OPT-175B and Imagen; open-ish LLM discourse | 2 | 1 | 1 | 5 | 3 | [`2022-05.json`](../data/monthly/2022-05.json) |
| 2022-06 | GitHub Copilot GA — AI pair programmer goes paid | 2 | 1 | 2 | 5 | 5 | [`2022-06.json`](../data/monthly/2022-06.json) |
| 2022-07 | Midjourney open beta + BLOOM 176B | 3 | 2 | 2 | 4 | 5 | [`2022-07.json`](../data/monthly/2022-07.json) |
| 2022-08 | Stable Diffusion goes public — local image gen explosion | 1 | 1 | 3 | 4 | 5 | [`2022-08.json`](../data/monthly/2022-08.json) |
| 2022-09 | Whisper + Character.AI beta — speech and personas | 3 | 2 | 2 | 5 | 5 | [`2022-09.json`](../data/monthly/2022-09.json) |
| 2022-10 | LangChain era starts; tooling for LLM apps | 2 | 1 | 2 | 5 | 4 | [`2022-10.json`](../data/monthly/2022-10.json) |
| 2022-11 | ChatGPT launches; Galactica rises and falls; MJ V4 | 5 | 2 | 3 | 6 | 5 | [`2022-11.json`](../data/monthly/2022-11.json) |
| 2022-12 | ChatGPT viral; Perplexity; Niji; DAN jailbreak born | 4 | 2 | 3 | 5 | 5 | [`2022-12.json`](../data/monthly/2022-12.json) |
| 2023-01 | 100M race; MusicLM; exams panic; local RP frontends | 3 | 2 | 3 | 6 | 5 | [`2023-01.json`](../data/monthly/2023-01.json) |
| 2023-02 | Plus, Bard flop, Bing Sydney, Poe, LLaMA — February chaos | 6 | 4 | 4 | 8 | 5 | [`2023-02.json`](../data/monthly/2023-02.json) |
| 2023-03 | GPT-4 + Claude + 文心一言 + AutoGPT + Cursor — Pi Day singularity | 11 | 4 | 4 | 13 | 5 | [`2023-03.json`](../data/monthly/2023-03.json) |
| 2023-04 | 通义千问; BabyAGI; Italy ban; agent spring | 5 | 3 | 3 | 8 | 4 | [`2023-04.json`](../data/monthly/2023-04.json) |
| 2023-05 | I/O PaLM 2 + Bard public; Claude 100K; Pi; Falcon; 讯飞星火 | 9 | 3 | 3 | 9 | 5 | [`2023-05.json`](../data/monthly/2023-05.json) |
| 2023-06 | Code Interpreter hype; Phi-1; 百川; midyear hangover | 7 | 2 | 3 | 10 | 4 | [`2023-06.json`](../data/monthly/2023-06.json) |
| 2023-07 | Claude 2 + Llama 2 commercial open weights | 5 | 3 | 3 | 9 | 5 | [`2023-07.json`](../data/monthly/2023-07.json) |
| 2023-08 | CN备案潮: 智谱清言/百川/豆包/MiniMax; Code Llama; Enterprise | 8 | 3 | 3 | 9 | 5 | [`2023-08.json`](../data/monthly/2023-08.json) |
| 2023-09 | Mistral 7B shock; 通义/星火公众开放; DALL·E 3; AutoGen; Meta AI | 7 | 3 | 3 | 9 | 5 | [`2023-09.json`](../data/monthly/2023-09.json) |
| 2023-10 | Kimi长文本; DALL·E 3; Cursor seed; Voice mode seeds | 4 | 2 | 3 | 8 | 5 | [`2023-10.json`](../data/monthly/2023-10.json) |
| 2023-11 | DevDay GPTs; Altman drama; Grok; Amazon Q; Yi; Inflection-2 | 9 | 3 | 4 | 10 | 5 | [`2023-11.json`](../data/monthly/2023-11.json) |
| 2023-12 | Gemini 1.0; Mixtral; Phi-2; MJ V6; Suno; ChatGPT birthday | 6 | 3 | 4 | 9 | 5 | [`2023-12.json`](../data/monthly/2023-12.json) |
| 2024-01 | GPT Store; Team plan; CN price-war foreshadow | 3 | 1 | 2 | 8 | 5 | [`2024-01.json`](../data/monthly/2024-01.json) |
| 2024-02 | Sora; Bard→Gemini; Gemini Ultra; Gemma; Grok-1 OSS; Mistral Large | 7 | 3 | 3 | 9 | 5 | [`2024-02.json`](../data/monthly/2024-02.json) |
| 2024-03 | Claude 3 Opus/Sonnet/Haiku; Devin; Command R; Grok open; Kimi 200万字 | 7 | 3 | 4 | 9 | 5 | [`2024-03.json`](../data/monthly/2024-03.json) |
| 2024-04 | Llama 3; Phi-3; Memory; Udio; ChatGPT no-login | 5 | 2 | 3 | 9 | 5 | [`2024-04.json`](../data/monthly/2024-04.json) |
| 2024-05 | GPT-4o + Sky voice drama; Copilot Workspace; 豆包降价战 | 4 | 3 | 4 | 8 | 5 | [`2024-05.json`](../data/monthly/2024-05.json) |
| 2024-06 | Claude 3.5 Sonnet; Apple Intelligence; Qwen2; Dream Machine; Kling | 5 | 2 | 3 | 8 | 5 | [`2024-06.json`](../data/monthly/2024-06.json) |
| 2024-07 | Llama 3.1 405B; GPT-4o mini; SearchGPT tease; Mistral Large 2 | 5 | 2 | 3 | 7 | 5 | [`2024-07.json`](../data/monthly/2024-07.json) |
| 2024-08 | Grok-2; Cursor Composer; Structured Outputs | 4 | 2 | 3 | 7 | 5 | [`2024-08.json`](../data/monthly/2024-08.json) |
| 2024-09 | o1-preview reasoning; Llama 3.2; Pixtral; Advanced Voice | 4 | 2 | 3 | 8 | 5 | [`2024-09.json`](../data/monthly/2024-09.json) |
| 2024-10 | Claude 3.5 upgrade + Computer Use; Canvas; DeepSeek V2.5 | 6 | 2 | 3 | 7 | 5 | [`2024-10.json`](../data/monthly/2024-10.json) |
| 2024-11 | MCP; 豆包生吃文心; election AI discourse | 3 | 2 | 3 | 7 | 4 | [`2024-11.json`](../data/monthly/2024-11.json) |
| 2024-12 | DeepSeek-V3; o1 full; Sora public; Gemini 2.0; Llama 3.3; ChatGPT Pro $200 | 7 | 3 | 3 | 9 | 5 | [`2024-12.json`](../data/monthly/2024-12.json) |
| 2025-01 | DeepSeek-R1 + Nvidia shock; Operator; o3-mini | 3 | 3 | 5 | 10 | 5 | [`2025-01.json`](../data/monthly/2025-01.json) |
| 2025-02 | Grok 3; Claude 3.7 + Claude Code; GPT-4.5 | 4 | 2 | 3 | 8 | 5 | [`2025-02.json`](../data/monthly/2025-02.json) |
| 2025-03 | Gemini 2.5; Manus viral agent; GPT-4o image gen | 3 | 2 | 3 | 8 | 5 | [`2025-03.json`](../data/monthly/2025-03.json) |
| 2025-04 | Llama 4; o3/o4-mini; GPT-4.1; Udio/Suno legal shadows | 3 | 2 | 3 | 9 | 5 | [`2025-04.json`](../data/monthly/2025-04.json) |
| 2025-05 | Claude 4; Codex agent relaunch; Cursor $9.9B | 3 | 2 | 3 | 8 | 5 | [`2025-05.json`](../data/monthly/2025-05.json) |
| 2025-06 | ChatGPT connectors/MCP; study mode; midyear agent plumbing | 2 | 2 | 2 | 6 | 4 | [`2025-06.json`](../data/monthly/2025-06.json) |
| 2025-07 | Grok 4; ChatGPT Agent; GPT-5 eve; Llama open-weights turn chatter | 3 | 2 | 3 | 8 | 5 | [`2025-07.json`](../data/monthly/2025-07.json) |
| 2025-08 | GPT-5 ships; gpt-oss; Claude Opus 4.1; DeepSeek V3.1 | 4 | 2 | 3 | 8 | 5 | [`2025-08.json`](../data/monthly/2025-08.json) |
| 2025-09 | Sora 2; Claude Sonnet 4.5; DevDay eve; Pulse | 3 | 2 | 2 | 8 | 5 | [`2025-09.json`](../data/monthly/2025-09.json) |
| 2025-10 | DevDay Apps/AgentKit; Cursor 2.0 Composer model; Claude Haiku 4.5 | 5 | 2 | 3 | 8 | 5 | [`2025-10.json`](../data/monthly/2025-10.json) |
| 2025-11 | Gemini 3; GPT-5.1; Claude Opus 4.5; Grok 4.1; OpenClaw/Warelay born | 6 | 2 | 3 | 8 | 5 | [`2025-11.json`](../data/monthly/2025-11.json) |
| 2025-12 | GPT-5.2; DeepSeek V3.2; year-end agent fatigue/hope | 3 | 1 | 2 | 7 | 4 | [`2025-12.json`](../data/monthly/2025-12.json) |
| 2026-01 | OpenClaw rebrands (Clawdbot→Moltbot→OpenClaw); ChatGPT Health/Go | 2 | 1 | 3 | 8 | 5 | [`2026-01.json`](../data/monthly/2026-01.json) |
| 2026-02 | Claude 4.6; GPT-5.3-Codex; Gemini 3.1; Steinberger→OpenAI reports | 5 | 2 | 3 | 7 | 4 | [`2026-02.json`](../data/monthly/2026-02.json) |
| 2026-03 | GPT-5.4; Composer 2; Claude Code #1 tool narratives | 3 | 2 | 2 | 7 | 5 | [`2026-03.json`](../data/monthly/2026-03.json) |
| 2026-04 | GPT-5.5; Claude Opus 4.7; DeepSeek-V4; Muse Spark; Mythos preview | 5 | 2 | 3 | 7 | 4 | [`2026-04.json`](../data/monthly/2026-04.json) |
| 2026-05 | Claude Opus 4.8; Daybreak cyber program seeds; Composer 2.5 chatter | 3 | 2 | 2 | 6 | 4 | [`2026-05.json`](../data/monthly/2026-05.json) |
| 2026-06 | GPT-5.6 Sol/Terra/Luna; Claude Sonnet 5; SpaceX–Cursor deal chatter | 4 | 3 | 3 | 8 | 5 | [`2026-06.json`](../data/monthly/2026-06.json) |
| 2026-07 | Claude Opus 5; Grok 4.5; ChatGPT Work; GPT-5.6 rollout | 4 | 2 | 3 | 8 | 5 | [`2026-07.json`](../data/monthly/2026-07.json) |
| 2026-08 | Grok 4.6; GPT-5.6 Sol/Luna consumer; OpenAI↔Cursor contract tension reports | 4 | 2 | 3 | 7 | 4 | [`2026-08.json`](../data/monthly/2026-08.json) |
| 2026-09 | GPT-6 Astra + Daybreak; Images 2.5 — present edge of chronicle | 2 | 3 | 3 | 10 | 5 | [`2026-09.json`](../data/monthly/2026-09.json) |

## Source policy

- Prefer public launch blogs, Wikipedia, vendor changelogs, reputable timelines.
- No copyrighted verbatim dumps.
- Primary link hubs used this run include:
  - https://www.scriptbyai.com/timeline-of-chatgpt/
  - https://en.wikipedia.org/wiki/Claude_(language_model)
  - https://en.wikipedia.org/wiki/Gemini_(Google)
  - https://en.wikipedia.org/wiki/Llama_(language_model)
  - https://en.wikipedia.org/wiki/OpenClaw
  - https://api-docs.deepseek.com/updates/
  - https://x.ai/news
  - https://openai.com / Anthropic / Google / Meta blogs
  - CN: 通义/Kimi Wikipedia, Sina/Tencent news on 备案 & 豆包
- Per-month `events[].links` carry concrete citations where available.

## Next steps (for parent / later agents)

1. Spot-check sparse months (early 2022, mid-2025 plumbing months) with more WebSearch.
2. Expand CN-only months (MiniMax Hailuo, StepFun, Skywork, SenseNova point releases).
3. **Only then** derive `CHARACTERS.md` from heat ranking + narrative needs.
4. TIMELINE.md / CRAFT.md can be generated as views over this DB.

_Generated for CHAOS Library research workspace. Stats snapshot from 57 month files + 180 index rows._
