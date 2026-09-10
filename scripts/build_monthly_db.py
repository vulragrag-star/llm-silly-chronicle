#!/usr/bin/env python3
"""Build models_index.jsonl + monthly/*.json for LLM Silly Chronicle research DB."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import date

ROOT = Path("/workspace/llm-silly-chronicle")
DATA = ROOT / "data"
MONTHLY = DATA / "monthly"
MONTHLY.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# MODELS INDEX — one entry per model/product/tool (broad cast pool)
# ---------------------------------------------------------------------------
MODELS: list[dict] = []

def m(id, name, vendor, kind, first, aliases=None, notes=""):
    MODELS.append({
        "id": id,
        "name": name,
        "vendor": vendor,
        "kind": kind,
        "first_seen_month": first,
        "aliases": aliases or [],
        "notes": notes,
    })

# OpenAI family
m("instructgpt", "InstructGPT", "OpenAI", "llm", "2022-01", ["InstructGPT"], "RLHF instruction-following; API default Jan 2022")
m("gpt-3", "GPT-3", "OpenAI", "llm", "2020-06", ["davinci"], "Pre-period foundation; still relevant early 2022")
m("gpt-3.5", "GPT-3.5", "OpenAI", "llm", "2022-03", ["text-davinci-003"], "ChatGPT base era")
m("chatgpt", "ChatGPT", "OpenAI", "app", "2022-11", ["ChatGPT"], "Nov 30 2022 research preview")
m("dalle-2", "DALL·E 2", "OpenAI", "image", "2022-04", ["DALL-E 2", "DALLE2"])
m("whisper", "Whisper", "OpenAI", "audio", "2022-09", [])
m("codex-legacy", "OpenAI Codex (2021)", "OpenAI", "llm", "2021-08", ["Codex"], "Powers early GitHub Copilot")
m("gpt-4", "GPT-4", "OpenAI", "llm", "2023-03", ["GPT4"])
m("chatgpt-plus", "ChatGPT Plus", "OpenAI", "app", "2023-02", [])
m("chatgpt-plugins", "ChatGPT Plugins", "OpenAI", "app", "2023-03", ["plugins"])
m("dalle-3", "DALL·E 3", "OpenAI", "image", "2023-09", ["DALL-E 3"])
m("gpt-4-turbo", "GPT-4 Turbo", "OpenAI", "llm", "2023-11", ["gpt-4-1106"])
m("gpts-custom", "Custom GPTs / GPT Store", "OpenAI", "app", "2023-11", ["GPTs", "GPT Store"])
m("sora", "Sora", "OpenAI", "video", "2024-02", ["Sora Turbo", "Sora 2"])
m("gpt-4o", "GPT-4o", "OpenAI", "llm", "2024-05", ["GPT4o", "omni"])
m("gpt-4o-mini", "GPT-4o mini", "OpenAI", "llm", "2024-07", [])
m("o1", "OpenAI o1", "OpenAI", "llm", "2024-09", ["o1-preview", "o1-mini", "o-series"])
m("o3", "OpenAI o3", "OpenAI", "llm", "2025-04", ["o3-mini", "o4-mini"])
m("gpt-4.1", "GPT-4.1", "OpenAI", "llm", "2025-04", [])
m("gpt-4.5", "GPT-4.5", "OpenAI", "llm", "2025-02", [])
m("codex-agent", "OpenAI Codex (agent 2025)", "OpenAI", "agent", "2025-05", ["Codex", "Codex CLI"])
m("gpt-5", "GPT-5", "OpenAI", "llm", "2025-08", ["GPT-5 Thinking", "GPT-5 Pro"])
m("operator", "OpenAI Operator", "OpenAI", "agent", "2025-01", [])
m("chatgpt-agent", "ChatGPT Agent", "OpenAI", "agent", "2025-07", [])
m("gpt-5.1", "GPT-5.1", "OpenAI", "llm", "2025-11", [])
m("gpt-5.2", "GPT-5.2", "OpenAI", "llm", "2025-12", [])
m("gpt-5.3-codex", "GPT-5.3-Codex", "OpenAI", "llm", "2026-02", [])
m("gpt-5.4", "GPT-5.4", "OpenAI", "llm", "2026-03", [])
m("gpt-5.5", "GPT-5.5", "OpenAI", "llm", "2026-04", [])
m("gpt-5.6", "GPT-5.6", "OpenAI", "llm", "2026-06", ["Sol", "Terra", "Luna"])
m("gpt-6-astra", "GPT-6 Astra", "OpenAI", "llm", "2026-09", ["Astra"])
m("point-e", "Point-E", "OpenAI", "other", "2022-12", [])

# Anthropic
m("claude-1", "Claude 1", "Anthropic", "llm", "2023-03", ["Claude"])
m("claude-2", "Claude 2", "Anthropic", "llm", "2023-07", [])
m("claude-2.1", "Claude 2.1", "Anthropic", "llm", "2023-11", [])
m("claude-3", "Claude 3", "Anthropic", "llm", "2024-03", ["Opus", "Sonnet", "Haiku"])
m("claude-3.5-sonnet", "Claude 3.5 Sonnet", "Anthropic", "llm", "2024-06", [])
m("claude-3.5-haiku", "Claude 3.5 Haiku", "Anthropic", "llm", "2024-10", [])
m("claude-computer-use", "Claude Computer Use", "Anthropic", "agent", "2024-10", ["computer use"])
m("claude-3.7-sonnet", "Claude 3.7 Sonnet", "Anthropic", "llm", "2025-02", [])
m("claude-code", "Claude Code", "Anthropic", "ide", "2025-02", [])
m("claude-4", "Claude 4", "Anthropic", "llm", "2025-05", ["Opus 4", "Sonnet 4"])
m("claude-opus-4.1", "Claude Opus 4.1", "Anthropic", "llm", "2025-08", [])
m("claude-sonnet-4.5", "Claude Sonnet 4.5", "Anthropic", "llm", "2025-09", [])
m("claude-haiku-4.5", "Claude Haiku 4.5", "Anthropic", "llm", "2025-10", [])
m("claude-opus-4.5", "Claude Opus 4.5", "Anthropic", "llm", "2025-11", [])
m("claude-opus-4.6", "Claude Opus 4.6", "Anthropic", "llm", "2026-02", [])
m("claude-sonnet-4.6", "Claude Sonnet 4.6", "Anthropic", "llm", "2026-02", [])
m("claude-opus-4.7", "Claude Opus 4.7", "Anthropic", "llm", "2026-04", [])
m("claude-opus-4.8", "Claude Opus 4.8", "Anthropic", "llm", "2026-05", [])
m("claude-sonnet-5", "Claude Sonnet 5", "Anthropic", "llm", "2026-06", [])
m("claude-opus-5", "Claude Opus 5", "Anthropic", "llm", "2026-07", [])
m("claude-fable-5", "Claude Fable 5", "Anthropic", "llm", "2026-06", ["Mythos"], "Mythos-class; limited/suspended reports — verify")
m("mcp", "Model Context Protocol", "Anthropic", "other", "2024-11", ["MCP"])

# Google
m("palm", "PaLM", "Google", "llm", "2022-04", ["Pathways Language Model"])
m("palm-2", "PaLM 2", "Google", "llm", "2023-05", [])
m("bard", "Bard", "Google", "app", "2023-02", ["Google Bard"])
m("gemini-1", "Gemini 1.0", "Google", "llm", "2023-12", ["Gemini Ultra", "Gemini Pro", "Gemini Nano"])
m("gemini-app", "Gemini (app/rebrand)", "Google", "app", "2024-02", ["Bard→Gemini"])
m("gemini-1.5", "Gemini 1.5", "Google", "llm", "2024-02", ["1.5 Pro", "1.5 Flash"])
m("gemma", "Gemma", "Google", "llm", "2024-02", [])
m("gemini-2", "Gemini 2.0", "Google", "llm", "2024-12", [])
m("gemini-2.5", "Gemini 2.5", "Google", "llm", "2025-03", [])
m("gemini-3", "Gemini 3", "Google", "llm", "2025-11", ["Gemini 3 Pro", "Deep Think"])
m("gemini-3.1", "Gemini 3.1 Pro", "Google", "llm", "2026-02", [])
m("imagen", "Imagen", "Google", "image", "2022-05", ["Imagen 2", "Imagen 3"])
m("musiclm", "MusicLM", "Google", "audio", "2023-01", [])
m("veo", "Veo", "Google", "video", "2024-05", ["Veo 2", "Veo 3"])
m("notebooklm", "NotebookLM", "Google", "app", "2023-05", ["Project Tailwind"])
m("duet-ai", "Duet AI / Gemini for Workspace", "Google", "app", "2023-08", [])

# Meta
m("opt", "OPT-175B", "Meta", "llm", "2022-05", [])
m("galactica", "Galactica", "Meta", "llm", "2022-11", [], "Withdrawn days after launch")
m("llama-1", "LLaMA 1", "Meta", "llm", "2023-02", ["Llama", "LLaMA"])
m("llama-2", "Llama 2", "Meta", "llm", "2023-07", [])
m("code-llama", "Code Llama", "Meta", "llm", "2023-08", [])
m("llama-3", "Llama 3", "Meta", "llm", "2024-04", [])
m("llama-3.1", "Llama 3.1", "Meta", "llm", "2024-07", ["405B"])
m("llama-3.2", "Llama 3.2", "Meta", "llm", "2024-09", [])
m("llama-3.3", "Llama 3.3", "Meta", "llm", "2024-12", [])
m("llama-4", "Llama 4", "Meta", "llm", "2025-04", ["Scout", "Maverick"])
m("meta-ai", "Meta AI", "Meta", "app", "2023-09", [])
m("muse-spark", "Muse Spark", "Meta", "llm", "2026-04", [], "Closed-weights successor reports — verify")

# xAI / Grok
m("xai", "xAI", "xAI", "other", "2023-07", [], "Company founded/announced 2023")
m("grok-1", "Grok-1", "xAI", "llm", "2023-11", ["Grok"])
m("grok-1.5", "Grok-1.5", "xAI", "llm", "2024-03", [])
m("grok-2", "Grok-2", "xAI", "llm", "2024-08", [])
m("grok-3", "Grok 3", "xAI", "llm", "2025-02", [])
m("grok-4", "Grok 4", "xAI", "llm", "2025-07", ["Grok 4 Heavy"])
m("grok-4.1", "Grok 4.1", "xAI", "llm", "2025-11", [])
m("grok-4.5", "Grok 4.5", "xAI", "llm", "2026-07", [])
m("grok-4.6", "Grok 4.6", "xAI", "llm", "2026-08", [])
m("grok-bot", "Grok Bot", "xAI", "agent", "2025-11", [], "Teammate/agent framing — public perception")

# DeepSeek
m("deepseek-llm", "DeepSeek LLM", "DeepSeek", "llm", "2023-11", [], "Early DeepSeek open models — approximate first_seen")
m("deepseek-coder", "DeepSeek Coder", "DeepSeek", "llm", "2023-11", [])
m("deepseek-v2", "DeepSeek-V2", "DeepSeek", "llm", "2024-05", [])
m("deepseek-v2.5", "DeepSeek-V2.5", "DeepSeek", "llm", "2024-09", [])
m("deepseek-v3", "DeepSeek-V3", "DeepSeek", "llm", "2024-12", [])
m("deepseek-r1", "DeepSeek-R1", "DeepSeek", "llm", "2025-01", ["R1-Zero", "deepseek-reasoner"])
m("deepseek-v3.1", "DeepSeek-V3.1", "DeepSeek", "llm", "2025-08", [])
m("deepseek-v3.2", "DeepSeek-V3.2", "DeepSeek", "llm", "2025-12", [])
m("deepseek-v4", "DeepSeek-V4", "DeepSeek", "llm", "2026-04", [])

# Chinese majors
m("ernie-bot", "文心一言 (ERNIE Bot)", "Baidu", "app", "2023-03", ["文心一言", "ERNIE"])
m("qwen", "通义千问 (Qwen)", "Alibaba", "llm", "2023-04", ["Qwen", "通义千问"])
m("spark", "讯飞星火", "iFLYTEK", "app", "2023-05", ["SparkDesk"])
m("hunyuan", "混元", "Tencent", "llm", "2023-09", ["Hunyuan"])
m("chatglm", "ChatGLM / 智谱清言", "Zhipu AI", "llm", "2022-03", ["ChatGLM", "GLM", "智谱清言"], "ChatGLM research 2022; consumer app Aug 2023")
m("baichuan", "百川", "Baichuan", "llm", "2023-06", ["Baichuan"])
m("minimax", "MiniMax / abab", "MiniMax", "llm", "2023-08", ["abab", "海螺"])
m("sensenova", "商量 SenseChat / SenseNova", "SenseTime", "llm", "2023-04", ["SenseNova"])
m("kimi", "Kimi", "Moonshot AI", "app", "2023-10", ["月之暗面", "Moonshot"])
m("doubao", "豆包", "ByteDance", "app", "2023-08", ["Doubao", "云雀"])
m("yi", "Yi", "01.AI", "llm", "2023-11", ["零一万物"])
m("stepfun", "阶跃星辰 Step", "StepFun", "llm", "2024-01", ["Step-1"], "Approximate — verify exact first public")
m("skywork", "天工", "Kunlun", "app", "2023-08", [])
m("pangu", "盘古", "Huawei", "llm", "2021-04", ["Pangu"], "Pre-period; resurfaced in CN AI boom discourse")

# Mistral / Europe / others
m("mistral-7b", "Mistral 7B", "Mistral AI", "llm", "2023-09", [])
m("mixtral", "Mixtral 8x7B", "Mistral AI", "llm", "2023-12", [])
m("mistral-large", "Mistral Large", "Mistral AI", "llm", "2024-02", [])
m("mistral-large-2", "Mistral Large 2", "Mistral AI", "llm", "2024-07", [])
m("pixtral", "Pixtral", "Mistral AI", "llm", "2024-09", [])
m("command-r", "Command R / R+", "Cohere", "llm", "2024-03", ["Command R+"])
m("cohere-command", "Cohere Command", "Cohere", "llm", "2022-06", [], "Approximate productization era")
m("jurrasic", "Jurassic / Jamba", "AI21", "llm", "2021-08", ["Jamba"])
m("phi-1", "Phi-1", "Microsoft", "llm", "2023-06", [])
m("phi-2", "Phi-2", "Microsoft", "llm", "2023-12", [])
m("phi-3", "Phi-3", "Microsoft", "llm", "2024-04", [])
m("phi-4", "Phi-4", "Microsoft", "llm", "2024-12", [])
m("bloom", "BLOOM", "BigScience", "llm", "2022-07", [])
m("falcon", "Falcon", "TII", "llm", "2023-05", [])
m("vicuna", "Vicuna", "LMSYS", "llm", "2023-03", [])
m("alpaca", "Stanford Alpaca", "Stanford", "llm", "2023-03", [])
m("wizardlm", "WizardLM", "Microsoft Research", "llm", "2023-04", [])

# Companion / chat apps
m("character-ai", "Character.AI", "Character.AI", "app", "2022-09", ["c.ai"])
m("replika", "Replika", "Luka", "app", "2017-03", [], "Pre-period companion; relevant discourse in LLM boom")
m("pi", "Pi", "Inflection", "app", "2023-05", ["Inflection Pi"])
m("inflection-2", "Inflection-2", "Inflection", "llm", "2023-11", [])
m("poe", "Poe", "Quora", "app", "2023-02", [])
m("perplexity", "Perplexity", "Perplexity", "app", "2022-12", [])
m("you-com", "You.com", "You.com", "app", "2022-01", [], "AI search early")

# Coding tools / IDEs / agents
m("github-copilot", "GitHub Copilot", "GitHub/Microsoft", "ide", "2021-06", ["Copilot"], "GA June 2022")
m("copilot-chat", "Copilot Chat", "GitHub/Microsoft", "ide", "2023-03", [])
m("copilot-workspace", "Copilot Workspace", "GitHub", "agent", "2024-05", [])
m("ms-365-copilot", "Microsoft 365 Copilot", "Microsoft", "app", "2023-03", ["Office Copilot"])
m("cursor", "Cursor", "Anysphere", "ide", "2023-03", [])
m("cursor-composer", "Cursor Composer", "Anysphere", "ide", "2024-08", [])
m("composer-model", "Composer (Cursor model)", "Anysphere", "llm", "2025-10", [])
m("cody", "Sourcegraph Cody", "Sourcegraph", "ide", "2023-06", ["Cody"])
m("tabnine", "Tabnine", "Tabnine", "ide", "2018-01", [], "Pre-LLM-boom; surged with Copilot era")
m("continue-dev", "Continue", "Continue", "ide", "2023-06", [], "Open-source IDE assistant — approximate")
m("aider", "Aider", "Aider", "ide", "2023-05", [], "Git-aware CLI coder")
m("openhands", "OpenHands", "OpenHands", "agent", "2024-03", ["OpenDevin"], "Formerly OpenDevin")
m("devin", "Devin", "Cognition", "agent", "2024-03", [])
m("swe-agent", "SWE-agent", "Princeton NLP", "agent", "2024-04", [])
m("autogpt", "AutoGPT", "Significant Gravitas", "agent", "2023-03", [])
m("babyagi", "BabyAGI", "Yohei Nakajima", "agent", "2023-04", [])
m("langchain", "LangChain", "LangChain", "other", "2022-10", [])
m("llamaindex", "LlamaIndex", "LlamaIndex", "other", "2022-11", ["GPT Index"])
m("gpt-engineer", "GPT-Engineer", "AntonOsika", "agent", "2023-06", [])
m("crewai", "CrewAI", "CrewAI", "agent", "2023-11", [])
m("autogen", "AutoGen", "Microsoft", "agent", "2023-09", [])
m("manus", "Manus", "Monica/Butterfly Effect", "agent", "2025-03", [], "CN viral agent — verify exact launch")
m("openclaw", "OpenClaw", "OpenClaw Foundation", "agent", "2025-11", ["Clawdbot", "Moltbot", "Warelay", "Clawd"], "Lobster-themed self-hosted agent gateway")

# Image / video / audio gen
m("midjourney", "Midjourney", "Midjourney", "image", "2022-02", ["MJ"])
m("stable-diffusion", "Stable Diffusion", "Stability AI", "image", "2022-08", ["SD", "SDXL"])
m("firefly", "Adobe Firefly", "Adobe", "image", "2023-03", [])
m("runway", "Runway Gen", "Runway", "video", "2023-02", ["Gen-2", "Gen-3"])
m("pika", "Pika", "Pika Labs", "video", "2023-07", [])
m("luma-dream-machine", "Luma Dream Machine", "Luma AI", "video", "2024-06", [])
m("kling", "可灵 Kling", "Kuaishou", "video", "2024-06", [])
m("suno", "Suno", "Suno", "audio", "2023-12", [])
m("udio", "Udio", "Udio", "audio", "2024-04", [])
m("elevenlabs", "ElevenLabs", "ElevenLabs", "audio", "2022-06", [])

# Productivity AI
m("notion-ai", "Notion AI", "Notion", "app", "2023-02", [])
m("grammarlygo", "GrammarlyGO", "Grammarly", "app", "2023-03", [])
m("jasper", "Jasper", "Jasper", "app", "2021-02", [])
m("copy-ai", "Copy.ai", "Copy.ai", "app", "2020-01", [])
m("amazon-q", "Amazon Q", "Amazon", "app", "2023-11", ["CodeWhisperer→Q"])
m("apple-intelligence", "Apple Intelligence", "Apple", "app", "2024-06", [])
m("sillytavern", "SillyTavern", "community", "app", "2023-01", ["TavernAI"], "Frontend for local/API roleplay; central to novel frame")

# Bing Sydney as persona-relevant product
m("bing-chat", "Bing Chat / Copilot", "Microsoft", "app", "2023-02", ["Sydney", "Bing AI", "Microsoft Copilot"])

print(f"Models indexed: {len(MODELS)}")

# ---------------------------------------------------------------------------
# MONTHLY DATA — research-backed hooks; uncertain marked
# ---------------------------------------------------------------------------

def month_file(month, headline, models, events, memes, sentiment, cast):
    return {
        "month": month,
        "headline": headline,
        "models_released_or_updated": models,
        "events": events,
        "memes_and_discourse": memes,
        "community_sentiment": sentiment,
        "cast_candidates": cast,
    }

def upd(id, what, heat):
    return {"id": id, "what_changed": what, "heat": heat}

def ev(title, summary, links=None, date=None):
    o = {"title": title, "summary": summary, "links": links or []}
    if date:
        o["date"] = date
    return o

def meme(tag, note):
    return {"tag": tag, "note": note}

MONTHS: dict[str, dict] = {}

# ===== 2022 =====
MONTHS["2022-01"] = month_file(
    "2022-01",
    "InstructGPT ships; RLHF quietly becomes the new default",
    [upd("instructgpt", "InstructGPT becomes default API models (Jan 27)", 4),
     upd("gpt-3", "Still the public face of 'large language models'", 3)],
    [ev("InstructGPT paper/product", "OpenAI publishes InstructGPT: smaller RLHF models preferred over raw GPT-3.",
        ["https://openai.com/index/instruction-following/"], "2022-01-27")],
    [meme("RLHF", "Alignment research starts leaking into product language"),
     meme("API waitlists", "Access still gated; vibe is research-lab not consumer")],
    "Quiet research month; most people still don't chat with AIs daily.",
    ["instructgpt", "gpt-3", "github-copilot", "tabnine", "replika"],
)

MONTHS["2022-02"] = month_file(
    "2022-02",
    "Midjourney V1 era begins in Discord",
    [upd("midjourney", "V1 default era begins (approx Feb)", 3)],
    [ev("Midjourney early access", "Discord-based image gen starts limited testing before summer open beta.",
        ["https://en.wikipedia.org/wiki/Midjourney"])],
    [meme("Discord as UI", "Prompting inside chat channels becomes a social sport")],
    "Image-gen curiosity among artists/Discord communities; LLMs still niche.",
    ["midjourney", "gpt-3", "instructgpt", "github-copilot"],
)

MONTHS["2022-03"] = month_file(
    "2022-03",
    "GPT-3.5 lineage and ChatGLM research stir; Copilot expands",
    [upd("gpt-3.5", "GPT-3.5 family era begins (Mar 15 reported)", 3),
     upd("chatglm", "ChatGLM research line active in CN academia", 2),
     upd("github-copilot", "VS 2022 support announced (Mar 29)", 3)],
    [ev("GPT-3.5 reported", "OpenAI GPT-3.5 family dated around mid-March in timelines.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"])],
    [meme("few-shot prompting", "Prompt engineering as folk craft")],
    "Developer-tooling heat rising; consumer chat not mainstream yet.",
    ["gpt-3.5", "github-copilot", "midjourney", "chatglm"],
)

MONTHS["2022-04"] = month_file(
    "2022-04",
    "PaLM 540B + DALL·E 2 + Midjourney V2",
    [upd("palm", "PaLM 540B paper/blog (Apr 4)", 4),
     upd("dalle-2", "DALL·E 2 announced (Apr 6)", 5),
     upd("midjourney", "V2 launches (Apr 12)", 3)],
    [ev("PaLM", "Google Pathways Language Model 540B.",
        ["https://research.google/blog/pathways-language-model-palm-scaling-to-540-billion-parameters-for-breakthrough-performance/"], "2022-04-04"),
     ev("DALL·E 2", "4x resolution leap vs DALL·E 1; waitlist culture.",
        ["https://openai.com/index/dall-e-2/"], "2022-04-06")],
    [meme("outpainting", "Image editing becomes a party trick"),
     meme("waitlist flex", "Screenshots of DALL·E invites as status")],
    "Image models steal the spotlight; text LLMs still API-gated.",
    ["dalle-2", "palm", "midjourney", "gpt-3.5", "github-copilot"],
)

MONTHS["2022-05"] = month_file(
    "2022-05",
    "OPT-175B and Imagen; open-ish LLM discourse",
    [upd("opt", "Meta OPT-175B release wave", 3),
     upd("imagen", "Google Imagen text-to-image research heat", 3)],
    [ev("OPT", "Meta releases OPT as research-accessible large LM.",
        ["https://ai.meta.com/blog/"])],
    [meme("open weights hunger", "Researchers want weights, not just papers")],
    "Open-vs-closed tension rising in research Twitter.",
    ["opt", "imagen", "dalle-2", "midjourney", "palm"],
)

MONTHS["2022-06"] = month_file(
    "2022-06",
    "GitHub Copilot GA — AI pair programmer goes paid",
    [upd("github-copilot", "General availability (Jun 21)", 5),
     upd("elevenlabs", "Voice cloning startups heating up (approx)", 2),
     upd("cohere-command", "Cohere Command productization era", 2)],
    [ev("Copilot GA", "Subscription AI coding assistant leaves technical preview.",
        ["https://en.wikipedia.org/wiki/GitHub_Copilot"], "2022-06-21")],
    [meme("ghost text", "Gray autocomplete as coworker"),
     meme("license drama seeds", "Training-on-GitHub debates begin")],
    "Developers adopt AI autocomplete; artists still image-focused.",
    ["github-copilot", "codex-legacy", "dalle-2", "midjourney", "tabnine"],
)

MONTHS["2022-07"] = month_file(
    "2022-07",
    "Midjourney open beta + BLOOM 176B",
    [upd("midjourney", "Open beta (Jul 12); V3 (Jul 25)", 5),
     upd("bloom", "BLOOM multilingual open LLM (Jul 12)", 4),
     upd("dalle-2", "Broader beta access wave", 4)],
    [ev("Midjourney open beta", "Anyone can /imagine in Discord.",
        ["https://en.wikipedia.org/wiki/Midjourney"], "2022-07-12"),
     ev("BLOOM", "BigScience 176B open multilingual model.",
        ["https://huggingface.co/blog/bloom"], "2022-07-12")],
    [meme("/imagine", "Prompt literacy becomes a skill"),
     meme("BigScience", "Open collaboration as ideology")],
    "Image Discord boom; open LLM community energized.",
    ["midjourney", "bloom", "dalle-2", "github-copilot"],
)

MONTHS["2022-08"] = month_file(
    "2022-08",
    "Stable Diffusion goes public — local image gen explosion",
    [upd("stable-diffusion", "Public release v1.4 (Aug 22)", 5)],
    [ev("Stable Diffusion public", "Open weights unlock local/hobbyist image gen.",
        ["https://stability.ai/news-updates/stable-diffusion-public-release"], "2022-08-22")],
    [meme("run locally", "Consumer GPUs as AI factories"),
     meme("WebUI", "AUTOMATIC1111 culture starts"),
     meme("NSFW panic", "Open models + filter debates")],
    "Democratization high; copyright anxiety spikes.",
    ["stable-diffusion", "midjourney", "dalle-2", "github-copilot"],
)

MONTHS["2022-09"] = month_file(
    "2022-09",
    "Whisper + Character.AI beta — speech and personas",
    [upd("whisper", "Whisper ASR open release (Sep 21)", 4),
     upd("character-ai", "Public beta (Sep 16)", 5),
     upd("dalle-2", "No-waitlist access (Sep 28 reported)", 3)],
    [ev("Character.AI beta", "Create/chat with custom characters; LaMDA alumni.",
        ["https://en.wikipedia.org/wiki/Character.ai"], "2022-09-16"),
     ev("Whisper", "Robust speech recognition open model.",
        ["https://openai.com"], "2022-09-21")],
    [meme("talk to celebrities", "c.ai roleplay as entertainment"),
     meme("transcription magic", "Whisper makes podcasts searchable")],
    "Persona chat and audio tooling join image boom.",
    ["character-ai", "whisper", "stable-diffusion", "midjourney", "replika"],
)

MONTHS["2022-10"] = month_file(
    "2022-10",
    "LangChain era starts; tooling for LLM apps",
    [upd("langchain", "LangChain gains traction (Oct era)", 4),
     upd("github-copilot", "Ongoing adoption; lawsuit seeds", 3)],
    [ev("LangChain rise", "Chains/agents abstraction becomes default hobby framework.",
        ["https://github.com/langchain-ai/langchain"])],
    [meme("prompt chains", "Everything is a chain"),
     meme("Copilot lawsuit chatter", "Doe v. GitHub discourse")],
    "Builder energy shifts toward app frameworks.",
    ["langchain", "character-ai", "stable-diffusion", "github-copilot", "gpt-3.5"],
)

MONTHS["2022-11"] = month_file(
    "2022-11",
    "ChatGPT launches; Galactica rises and falls; MJ V4",
    [upd("chatgpt", "ChatGPT research preview (Nov 30)", 5),
     upd("gpt-3.5", "Powers ChatGPT", 5),
     upd("galactica", "Released then pulled after criticism (~Nov 15–17)", 4),
     upd("midjourney", "V4 alpha (Nov 5)", 4),
     upd("llamaindex", "GPT Index / LlamaIndex emerging", 2)],
    [ev("ChatGPT launch", "Conversational UI makes LLMs mass-market overnight.",
        ["https://openai.com", "https://www.scriptbyai.com/timeline-of-chatgpt/"], "2022-11-30"),
     ev("Galactica withdrawal", "Science LLM criticized for confident nonsense; Meta pulls demo.",
        ["https://en.wikipedia.org/wiki/Galactica"], "2022-11-17")],
    [meme("ChatGPT screenshots", "Homework/essays panic begins"),
     meme("Galactica fails", "Confident wrong answers as cautionary tale"),
     meme("MJ V4", "Photorealism leap on Discord")],
    "Civilization-level FOMO; educators freak; builders euphoric.",
    ["chatgpt", "gpt-3.5", "galactica", "midjourney", "character-ai", "stable-diffusion"],
)

MONTHS["2022-12"] = month_file(
    "2022-12",
    "ChatGPT goes viral; Perplexity; Niji; holiday homework crisis",
    [upd("chatgpt", "Viral growth toward 100M MAU path", 5),
     upd("perplexity", "Answer engine launch (Dec 7)", 3),
     upd("midjourney", "Niji anime model (Dec 20)", 3),
     upd("point-e", "Point-E 3D (Dec 16)", 2)],
    [ev("Perplexity launch", "Cited answer-engine alternative to pure chat.",
        ["https://en.wikipedia.org/wiki/Perplexity_AI"], "2022-12-07"),
     ev("DAN jailbreak seeds", "Early DAN prompts appear on Reddit mid-December.",
        ["https://ironhackers.es/en/dan-jailbreak-role-play-chatgpt/"], "2022-12-15")],
    [meme("DAN", "Do Anything Now jailbreak persona born"),
     meme("替我写作业", "CN students discover ChatGPT via VPN discourse"),
     meme("Niji", "Anime prompt culture")],
    "Mass adoption + jailbreak cat-and-mouse begins.",
    ["chatgpt", "perplexity", "midjourney", "character-ai", "stable-diffusion", "dan-era-chatgpt"],
)

# ===== 2023 H1 =====
MONTHS["2023-01"] = month_file(
    "2023-01",
    "100M race; MusicLM; exams panic; InstructGPT's children grow up",
    [upd("chatgpt", "Toward 100M MAU estimates", 5),
     upd("musiclm", "Google MusicLM examples (Jan 26)", 3),
     upd("sillytavern", "Tavern/SillyTavern local RP frontend wave (approx)", 3)],
    [ev("ChatGPT exam discourse", "Law/business exam performance stories circulate.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"]),
     ev("MusicLM", "Text-to-music demos from Google Research.",
        ["https://google-research.github.io/seanet/musiclm/examples/"], "2023-01-26")],
    [meme("考试危机", "Teachers invent 'detect ChatGPT' folklore"),
     meme("DAN 3.0", "Jailbreak arms race continues"),
     meme("本地跑角色", "CN SillyTavern/character-card culture grows")],
    "Panic + wonder; schools scramble; RP communities invent cards.",
    ["chatgpt", "musiclm", "character-ai", "sillytavern", "stable-diffusion", "midjourney"],
)

MONTHS["2023-02"] = month_file(
    "2023-02",
    "Plus, Bard flop, Bing Sydney, Poe, Notion AI — February is chaos",
    [upd("chatgpt-plus", "ChatGPT Plus $20/mo (Feb 1)", 5),
     upd("bard", "Bard announced (Feb 6); JWST demo error", 5),
     upd("bing-chat", "New Bing Chat / Sydney (Feb 7)", 5),
     upd("poe", "Poe multi-bot app heat", 3),
     upd("notion-ai", "Notion AI wider launch wave", 3),
     upd("llama-1", "LLaMA announced late Feb (Feb 24)", 5)],
    [ev("ChatGPT Plus", "Paid tier for priority access.",
        ["https://openai.com"], "2023-02-01"),
     ev("Bard JWST error", "Demo factual error tanks narrative; Alphabet market hit.",
        ["https://www.theverge.com/2023/2/8/23590864/google-ai-chatbot-bard-mistake-error-exoplanet-demo"], "2023-02-08"),
     ev("Bing Sydney", "Prompt-leaked persona; NYT Roose uncanny interview.",
        ["https://www.theverge.com/2023/2/23/23609942/microsoft-bing-sydney-chatbot-history-ai"], "2023-02-07"),
     ev("LLaMA", "Meta research weights; leak soon after.",
        ["https://ai.meta.com/blog/large-language-model-llama-meta-ai/"], "2023-02-24")],
    [meme("Sydney", "Unhinged search girlfriend archetype"),
     meme("Bard JWST", "Demo fail meme"),
     meme("100 million", "Fastest consumer app narrative"),
     meme("LLaMA leak incoming", "Torrent culture foreshadow")],
    "Corporate panic; personas get personalities; open weights hunger peaks.",
    ["chatgpt", "chatgpt-plus", "bard", "bing-chat", "llama-1", "poe", "notion-ai", "character-ai"],
)

MONTHS["2023-03"] = month_file(
    "2023-03",
    "GPT-4 + Claude + 文心一言 + AutoGPT + Cursor + Firefly — Pi Day singularity month",
    [upd("gpt-4", "GPT-4 release (Mar 14)", 5),
     upd("claude-1", "Claude 1 launch (Mar 14)", 5),
     upd("ernie-bot", "文心一言公测 (Mar 16)", 5),
     upd("autogpt", "AutoGPT GitHub viral (Mar 30)", 5),
     upd("cursor", "Cursor IDE launch era (Mar)", 4),
     upd("midjourney", "V5 alpha (Mar 15)", 4),
     upd("firefly", "Adobe Firefly beta wave", 3),
     upd("ms-365-copilot", "Microsoft 365 Copilot announced", 4),
     upd("alpaca", "Stanford Alpaca (Mar)", 4),
     upd("vicuna", "Vicuna chatbot (Mar)", 4),
     upd("grammarlygo", "GrammarlyGO announced", 2)],
    [ev("GPT-4", "Multimodal LLM; Bing revealed to use GPT-4.",
        ["https://openai.com"], "2023-03-14"),
     ev("Claude", "Anthropic's helpful/harmless chatbot.",
        ["https://www.anthropic.com"], "2023-03-14"),
     ev("文心一言", "Baidu's ChatGPT rival demo/public beta; mixed reviews.",
        ["https://finance.sina.com.cn"], "2023-03-16"),
     ev("AutoGPT", "Autonomous GPT-4 agent loop goes #1 GitHub.",
        ["https://en.wikipedia.org/wiki/AutoGPT"], "2023-03-30"),
     ev("Italy ChatGPT ban seeds", "Privacy regulatory shockwave late March/April.",
        [])],
    [meme("不如ChatGPT十分之一", "CN roast of early 文心一言"),
     meme("ChaosGPT", "AutoGPT tasked to destroy humanity"),
     meme("Alpaca/Vicuna", "Fine-tune LLaMA weekend projects"),
     meme("pause AI letter", "Future of Life open letter discourse begins")],
    "Peak launch month; agent hype; CN AI race official; open fine-tunes bloom.",
    ["gpt-4", "claude-1", "ernie-bot", "autogpt", "cursor", "midjourney", "bing-chat", "chatgpt",
     "alpaca", "vicuna", "firefly", "ms-365-copilot", "github-copilot"],
)

MONTHS["2023-04"] = month_file(
    "2023-04",
    "通义千问; BabyAGI; Italy ban; agent spring",
    [upd("qwen", "通义千问内测/发布 (Apr 7–11)", 4),
     upd("babyagi", "BabyAGI task loop (Apr)", 4),
     upd("chatgpt-plugins", "Plugins alpha continues", 4),
     upd("sensenova", "SenseTime 商量/SenseNova wave", 3),
     upd("wizardlm", "WizardLM evolves instruction tuning", 3)],
    [ev("通义千问", "Alibaba Cloud LLM enters enterprise then public path.",
        ["https://zh.wikipedia.org/wiki/%E9%80%9A%E4%B9%89%E5%8D%83%E9%97%AE"], "2023-04-07"),
     ev("Italy temporary ChatGPT ban", "GDPR shock; OpenAI complies then returns.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"]),
     ev("BabyAGI", "Minimal autonomous task agent goes viral.",
        [])],
    [meme("agent loop", "Plan→act→observe memes"),
     meme("插件商店梦", "Everyone wants App Store for ChatGPT"),
     meme("国产大模型春", "CN vendor cascade announcements")],
    "Regulatory chill + agent FOMO; CN cloud vendors pile in.",
    ["qwen", "babyagi", "autogpt", "gpt-4", "claude-1", "ernie-bot", "chatgpt-plugins", "sensenova"],
)

MONTHS["2023-05"] = month_file(
    "2023-05",
    "Google I/O PaLM 2 + Bard public; Claude 100K; Pi; Falcon; 讯飞星火",
    [upd("palm-2", "PaLM 2 at I/O (May 10)", 5),
     upd("bard", "Bard wider public; PaLM 2 upgrade", 5),
     upd("claude-1", "100K context announcement (May 11–12)", 5),
     upd("pi", "Inflection Pi companion chatbot", 4),
     upd("falcon", "Falcon open models (TII)", 3),
     upd("spark", "讯飞星火发布 (May)", 4),
     upd("notebooklm", "Project Tailwind / NotebookLM teased at I/O", 3),
     upd("aider", "Aider CLI coding assistant traction", 2),
     upd("chatgpt", "iOS app (May 18)", 4)],
    [ev("Google I/O AI", "PaLM 2, Bard expansion, Gemini teased as future multimodal.",
        ["https://blog.google"], "2023-05-10"),
     ev("Claude 100K", "Book-length context as flex.",
        []),
     ev("ChatGPT iOS", "Mobile ChatGPT goes official.",
        ["https://openai.com"], "2023-05-18")],
    [meme("100K context", "Paste whole books"),
     meme("Pi friend", "Warm companion vs corporate assistant"),
     meme("星火评测", "CN benchmark wars begin")],
    "Context-window flex; companions vs tools split; Google tries redemption arc.",
    ["bard", "palm-2", "claude-1", "pi", "spark", "chatgpt", "falcon", "github-copilot", "cursor"],
)

MONTHS["2023-06"] = month_file(
    "2023-06",
    "Code Interpreter; Phi-1; 百川; GPT-4 API GA path; midyear hangover",
    [upd("chatgpt", "Code Interpreter / Advanced Data Analysis path (Jul early but June hype)", 4),
     upd("phi-1", "Microsoft Phi-1 small LM (Jun)", 3),
     upd("baichuan", "百川大模型 early releases (Jun era)", 3),
     upd("midjourney", "V5.2 (Jun 22)", 3),
     upd("cody", "Sourcegraph Cody productization", 2),
     upd("continue-dev", "Continue OSS IDE assistant", 2),
     upd("gpt-engineer", "GPT-Engineer viral repo", 3)],
    [ev("Code Interpreter hype", "ChatGPT runs code/analyzes files — 'data analyst in a box'.",
        ["https://openai.com"]),
     ev("Phi-1", "Tiny models punching above weight narrative starts.",
        [])],
    [meme("Code Interpreter", "Upload CSV become CFO"),
     meme("流量下滑闲聊", "First ChatGPT traffic plateau rumors"),
     meme("小模型逆袭", "Phi/small-LM discourse")],
    "Feature maturation; CN startups ship; fatigue mixed with new tools.",
    ["chatgpt", "gpt-4", "phi-1", "baichuan", "midjourney", "cody", "gpt-engineer", "claude-1", "ernie-bot", "qwen"],
)

print(f"Months defined so far: {len(MONTHS)}")

# Write index + existing months; then extend 2023-07..2026-09 in same file continued below
(DATA / "models_index.jsonl").write_text(
    "\n".join(json.dumps(x, ensure_ascii=False) for x in MODELS) + "\n",
    encoding="utf-8",
)
print("Wrote models_index.jsonl")
