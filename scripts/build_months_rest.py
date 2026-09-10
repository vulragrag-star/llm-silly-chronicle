#!/usr/bin/env python3
"""Write all monthly JSON files 2022-01..2026-09; extend H2'23–2026."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path("/workspace/llm-silly-chronicle")
DATA = ROOT / "data"
MONTHLY = DATA / "monthly"
MONTHLY.mkdir(parents=True, exist_ok=True)

# Import first 18 months by re-executing definitions via shared module pattern:
# We'll redefine helpers and ALL months in one complete dict for reliability.

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

M = {}

# --- reuse 2022-01..2023-06 from previous run by loading if present, else redefine ---
# Full redefine for atomic correctness:

M["2022-01"] = month_file("2022-01", "InstructGPT ships; RLHF quietly becomes the new default",
    [upd("instructgpt", "InstructGPT becomes default API models (Jan 27)", 4),
     upd("gpt-3", "Still the public face of large language models", 3)],
    [ev("InstructGPT", "OpenAI publishes InstructGPT: RLHF models preferred over raw GPT-3.",
        ["https://openai.com/index/instruction-following/"], "2022-01-27")],
    [meme("RLHF", "Alignment research enters product language"), meme("API waitlists", "Access still gated")],
    "Quiet research month; most people still don't chat with AIs daily.",
    ["instructgpt", "gpt-3", "github-copilot", "tabnine", "replika"])

M["2022-02"] = month_file("2022-02", "Midjourney V1 era begins in Discord",
    [upd("midjourney", "V1 default era begins (approx Feb)", 3)],
    [ev("Midjourney early access", "Discord image gen limited testing before summer open beta.",
        ["https://en.wikipedia.org/wiki/Midjourney"])],
    [meme("Discord as UI", "Prompting inside chat channels becomes social")],
    "Image-gen curiosity among artists/Discord; LLMs still niche.",
    ["midjourney", "gpt-3", "instructgpt", "github-copilot"])

M["2022-03"] = month_file("2022-03", "GPT-3.5 lineage; ChatGLM research; Copilot expands",
    [upd("gpt-3.5", "GPT-3.5 family era begins (Mar 15 reported)", 3),
     upd("chatglm", "ChatGLM research line active in CN academia", 2),
     upd("github-copilot", "VS 2022 support (Mar 29)", 3)],
    [ev("GPT-3.5 reported", "OpenAI GPT-3.5 family dated around mid-March in timelines.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"])],
    [meme("few-shot prompting", "Prompt engineering as folk craft")],
    "Developer-tooling heat rising; consumer chat not mainstream yet.",
    ["gpt-3.5", "github-copilot", "midjourney", "chatglm"])

M["2022-04"] = month_file("2022-04", "PaLM 540B + DALL·E 2 + Midjourney V2",
    [upd("palm", "PaLM 540B (Apr 4)", 4), upd("dalle-2", "DALL·E 2 announced (Apr 6)", 5),
     upd("midjourney", "V2 (Apr 12)", 3)],
    [ev("PaLM", "Google 540B Pathways LM.",
        ["https://research.google/blog/pathways-language-model-palm-scaling-to-540-billion-parameters-for-breakthrough-performance/"], "2022-04-04"),
     ev("DALL·E 2", "Higher-res image gen; waitlist culture.",
        ["https://openai.com/index/dall-e-2/"], "2022-04-06")],
    [meme("outpainting", "Image editing party trick"), meme("waitlist flex", "Invite screenshots as status")],
    "Image models steal spotlight; text LLMs still API-gated.",
    ["dalle-2", "palm", "midjourney", "gpt-3.5", "github-copilot"])

M["2022-05"] = month_file("2022-05", "OPT-175B and Imagen; open-ish LLM discourse",
    [upd("opt", "Meta OPT-175B release wave", 3), upd("imagen", "Google Imagen research heat", 3)],
    [ev("OPT", "Meta releases OPT as research-accessible large LM.", [])],
    [meme("open weights hunger", "Researchers want weights not just papers")],
    "Open-vs-closed tension rising on research Twitter.",
    ["opt", "imagen", "dalle-2", "midjourney", "palm"])

M["2022-06"] = month_file("2022-06", "GitHub Copilot GA — AI pair programmer goes paid",
    [upd("github-copilot", "General availability (Jun 21)", 5),
     upd("elevenlabs", "Voice cloning startups heating (approx)", 2)],
    [ev("Copilot GA", "Subscription AI coding leaves technical preview.",
        ["https://en.wikipedia.org/wiki/GitHub_Copilot"], "2022-06-21")],
    [meme("ghost text", "Gray autocomplete as coworker"), meme("license drama seeds", "Training-on-GitHub debates")],
    "Developers adopt AI autocomplete; artists still image-focused.",
    ["github-copilot", "codex-legacy", "dalle-2", "midjourney", "tabnine"])

M["2022-07"] = month_file("2022-07", "Midjourney open beta + BLOOM 176B",
    [upd("midjourney", "Open beta (Jul 12); V3 (Jul 25)", 5),
     upd("bloom", "BLOOM multilingual open LLM (Jul 12)", 4),
     upd("dalle-2", "Broader beta access wave", 4)],
    [ev("Midjourney open beta", "Anyone can /imagine in Discord.",
        ["https://en.wikipedia.org/wiki/Midjourney"], "2022-07-12"),
     ev("BLOOM", "BigScience 176B open multilingual model.",
        ["https://huggingface.co/blog/bloom"], "2022-07-12")],
    [meme("/imagine", "Prompt literacy as skill"), meme("BigScience", "Open collaboration ideology")],
    "Image Discord boom; open LLM community energized.",
    ["midjourney", "bloom", "dalle-2", "github-copilot"])

M["2022-08"] = month_file("2022-08", "Stable Diffusion goes public — local image gen explosion",
    [upd("stable-diffusion", "Public release v1.4 (Aug 22)", 5)],
    [ev("Stable Diffusion public", "Open weights unlock local/hobbyist image gen.",
        ["https://stability.ai/news-updates/stable-diffusion-public-release"], "2022-08-22")],
    [meme("run locally", "Consumer GPUs as AI factories"), meme("WebUI", "AUTOMATIC1111 culture"),
     meme("NSFW panic", "Open models + filter debates")],
    "Democratization high; copyright anxiety spikes.",
    ["stable-diffusion", "midjourney", "dalle-2", "github-copilot"])

M["2022-09"] = month_file("2022-09", "Whisper + Character.AI beta — speech and personas",
    [upd("whisper", "Whisper ASR (Sep 21)", 4), upd("character-ai", "Public beta (Sep 16)", 5),
     upd("dalle-2", "No-waitlist access (Sep 28 reported)", 3)],
    [ev("Character.AI beta", "Custom characters; LaMDA alumni founders.",
        ["https://en.wikipedia.org/wiki/Character.ai"], "2022-09-16"),
     ev("Whisper", "Open speech recognition model.", [], "2022-09-21")],
    [meme("talk to celebrities", "c.ai roleplay entertainment"), meme("transcription magic", "Whisper podcasts")],
    "Persona chat and audio tooling join image boom.",
    ["character-ai", "whisper", "stable-diffusion", "midjourney", "replika"])

M["2022-10"] = month_file("2022-10", "LangChain era starts; tooling for LLM apps",
    [upd("langchain", "LangChain gains traction", 4), upd("github-copilot", "Lawsuit discourse seeds", 3)],
    [ev("LangChain rise", "Chains/agents abstraction becomes hobby default.",
        ["https://github.com/langchain-ai/langchain"])],
    [meme("prompt chains", "Everything is a chain"), meme("Copilot lawsuit chatter", "Doe v. GitHub")],
    "Builder energy shifts toward app frameworks.",
    ["langchain", "character-ai", "stable-diffusion", "github-copilot", "gpt-3.5"])

M["2022-11"] = month_file("2022-11", "ChatGPT launches; Galactica rises and falls; MJ V4",
    [upd("chatgpt", "ChatGPT research preview (Nov 30)", 5), upd("gpt-3.5", "Powers ChatGPT", 5),
     upd("galactica", "Released then withdrawn (~Nov 15–17)", 4),
     upd("midjourney", "V4 alpha (Nov 5)", 4), upd("llamaindex", "GPT Index emerging", 2)],
    [ev("ChatGPT launch", "Conversational UI makes LLMs mass-market.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2022-11-30"),
     ev("Galactica withdrawal", "Science LLM criticized; Meta pulls demo.", [], "2022-11-17")],
    [meme("ChatGPT screenshots", "Homework panic begins"), meme("Galactica fails", "Confident nonsense cautionary tale"),
     meme("MJ V4", "Photorealism leap")],
    "Civilization-level FOMO; educators freak; builders euphoric.",
    ["chatgpt", "gpt-3.5", "galactica", "midjourney", "character-ai", "stable-diffusion"])

M["2022-12"] = month_file("2022-12", "ChatGPT viral; Perplexity; Niji; DAN jailbreak born",
    [upd("chatgpt", "Viral growth path", 5), upd("perplexity", "Launch (Dec 7)", 3),
     upd("midjourney", "Niji anime (Dec 20)", 3), upd("point-e", "Point-E 3D (Dec 16)", 2)],
    [ev("Perplexity", "Cited answer engine.",
        ["https://en.wikipedia.org/wiki/Perplexity_AI"], "2022-12-07"),
     ev("DAN seeds", "Do Anything Now prompts on Reddit.",
        ["https://ironhackers.es/en/dan-jailbreak-role-play-chatgpt/"], "2022-12-15")],
    [meme("DAN", "Jailbreak persona born"), meme("替我写作业", "CN students VPN discourse"), meme("Niji", "Anime prompts")],
    "Mass adoption + jailbreak cat-and-mouse begins.",
    ["chatgpt", "perplexity", "midjourney", "character-ai", "stable-diffusion"])

M["2023-01"] = month_file("2023-01", "100M race; MusicLM; exams panic; local RP frontends",
    [upd("chatgpt", "Toward 100M MAU estimates", 5), upd("musiclm", "MusicLM examples (Jan 26)", 3),
     upd("sillytavern", "Tavern/SillyTavern RP frontend wave", 3)],
    [ev("Exam discourse", "Law/business exam performance stories.", ["https://www.scriptbyai.com/timeline-of-chatgpt/"]),
     ev("MusicLM", "Google text-to-music demos.", [], "2023-01-26")],
    [meme("考试危机", "Detect-ChatGPT folklore"), meme("DAN 3.0", "Jailbreak arms race"),
     meme("本地跑角色", "CN character-card culture")],
    "Panic + wonder; schools scramble; RP invents cards.",
    ["chatgpt", "musiclm", "character-ai", "sillytavern", "stable-diffusion", "midjourney"])

M["2023-02"] = month_file("2023-02", "Plus, Bard flop, Bing Sydney, Poe, LLaMA — February chaos",
    [upd("chatgpt-plus", "Plus $20/mo (Feb 1)", 5), upd("bard", "Announced (Feb 6); JWST error", 5),
     upd("bing-chat", "New Bing / Sydney (Feb 7)", 5), upd("poe", "Multi-bot app heat", 3),
     upd("notion-ai", "Wider launch wave", 3), upd("llama-1", "LLaMA (Feb 24)", 5)],
    [ev("ChatGPT Plus", "Paid priority access.", [], "2023-02-01"),
     ev("Bard JWST error", "Demo factual error; market narrative hit.",
        ["https://www.theverge.com/2023/2/8/23590864/google-ai-chatbot-bard-mistake-error-exoplanet-demo"], "2023-02-08"),
     ev("Bing Sydney", "Leaked persona; uncanny Roose interview.",
        ["https://www.theverge.com/2023/2/23/23609942/microsoft-bing-sydney-chatbot-history-ai"], "2023-02-07"),
     ev("LLaMA", "Meta research weights; leak soon after.", [], "2023-02-24")],
    [meme("Sydney", "Unhinged search girlfriend"), meme("Bard JWST", "Demo fail meme"),
     meme("100 million", "Fastest app narrative"), meme("LLaMA leak", "Torrent foreshadow")],
    "Corporate panic; personas get personalities; open-weights hunger peaks.",
    ["chatgpt", "chatgpt-plus", "bard", "bing-chat", "llama-1", "poe", "notion-ai", "character-ai"])

M["2023-03"] = month_file("2023-03", "GPT-4 + Claude + 文心一言 + AutoGPT + Cursor — Pi Day singularity",
    [upd("gpt-4", "GPT-4 (Mar 14)", 5), upd("claude-1", "Claude 1 (Mar 14)", 5),
     upd("ernie-bot", "文心一言公测 (Mar 16)", 5), upd("autogpt", "AutoGPT viral (Mar 30)", 5),
     upd("cursor", "Cursor IDE launch era", 4), upd("midjourney", "V5 alpha (Mar 15)", 4),
     upd("firefly", "Adobe Firefly beta", 3), upd("ms-365-copilot", "M365 Copilot announced", 4),
     upd("alpaca", "Stanford Alpaca", 4), upd("vicuna", "Vicuna", 4), upd("grammarlygo", "GrammarlyGO", 2)],
    [ev("GPT-4", "Multimodal LLM; Bing revealed using GPT-4.", ["https://openai.com"], "2023-03-14"),
     ev("Claude", "Anthropic chatbot launch.", ["https://www.anthropic.com"], "2023-03-14"),
     ev("文心一言", "Baidu rival; mixed reviews.", [], "2023-03-16"),
     ev("AutoGPT", "Autonomous agent #1 GitHub.", ["https://en.wikipedia.org/wiki/AutoGPT"], "2023-03-30")],
    [meme("不如ChatGPT十分之一", "CN roast of early 文心一言"), meme("ChaosGPT", "AutoGPT destroy humanity"),
     meme("Alpaca/Vicuna", "Weekend fine-tunes"), meme("pause AI letter", "FoL open letter")],
    "Peak launch month; agent hype; CN AI race official; open fine-tunes bloom.",
    ["gpt-4", "claude-1", "ernie-bot", "autogpt", "cursor", "midjourney", "bing-chat", "chatgpt",
     "alpaca", "vicuna", "firefly", "ms-365-copilot", "github-copilot"])

M["2023-04"] = month_file("2023-04", "通义千问; BabyAGI; Italy ban; agent spring",
    [upd("qwen", "通义千问内测/发布 (Apr 7–11)", 4), upd("babyagi", "BabyAGI (Apr)", 4),
     upd("chatgpt-plugins", "Plugins continue", 4), upd("sensenova", "SenseNova wave", 3),
     upd("wizardlm", "WizardLM instruction tuning", 3)],
    [ev("通义千问", "Alibaba Cloud LLM enters.",
        ["https://zh.wikipedia.org/wiki/%E9%80%9A%E4%B9%89%E5%8D%83%E9%97%AE"], "2023-04-07"),
     ev("Italy ChatGPT ban", "GDPR shock then return.", []),
     ev("BabyAGI", "Minimal task agent viral.", [])],
    [meme("agent loop", "Plan→act→observe"), meme("插件商店梦", "App Store for ChatGPT"),
     meme("国产大模型春", "CN vendor cascade")],
    "Regulatory chill + agent FOMO; CN cloud vendors pile in.",
    ["qwen", "babyagi", "autogpt", "gpt-4", "claude-1", "ernie-bot", "chatgpt-plugins", "sensenova"])

M["2023-05"] = month_file("2023-05", "I/O PaLM 2 + Bard public; Claude 100K; Pi; Falcon; 讯飞星火",
    [upd("palm-2", "PaLM 2 (May 10)", 5), upd("bard", "Wider public + PaLM 2", 5),
     upd("claude-1", "100K context", 5), upd("pi", "Inflection Pi", 4), upd("falcon", "Falcon open", 3),
     upd("spark", "讯飞星火 (May)", 4), upd("notebooklm", "Tailwind/NotebookLM tease", 3),
     upd("aider", "Aider traction", 2), upd("chatgpt", "iOS app (May 18)", 4)],
    [ev("Google I/O", "PaLM 2, Bard expansion, Gemini teased.", ["https://blog.google"], "2023-05-10"),
     ev("Claude 100K", "Book-length context flex.", []),
     ev("ChatGPT iOS", "Official mobile app.", [], "2023-05-18")],
    [meme("100K context", "Paste whole books"), meme("Pi friend", "Warm companion vs tool"),
     meme("星火评测", "CN benchmark wars")],
    "Context-window flex; companions vs tools; Google redemption arc.",
    ["bard", "palm-2", "claude-1", "pi", "spark", "chatgpt", "falcon", "github-copilot", "cursor"])

M["2023-06"] = month_file("2023-06", "Code Interpreter hype; Phi-1; 百川; midyear hangover",
    [upd("chatgpt", "Code Interpreter / ADA path", 4), upd("phi-1", "Phi-1 small LM", 3),
     upd("baichuan", "百川 early releases", 3), upd("midjourney", "V5.2 (Jun 22)", 3),
     upd("cody", "Sourcegraph Cody", 2), upd("continue-dev", "Continue OSS", 2),
     upd("gpt-engineer", "GPT-Engineer viral", 3)],
    [ev("Code Interpreter hype", "ChatGPT runs code/analyzes files.", ["https://openai.com"]),
     ev("Phi-1", "Tiny models punching above weight.", [])],
    [meme("Code Interpreter", "Upload CSV become CFO"), meme("流量下滑", "First traffic plateau rumors"),
     meme("小模型逆袭", "Phi discourse")],
    "Feature maturation; CN startups ship; fatigue mixed with new tools.",
    ["chatgpt", "gpt-4", "phi-1", "baichuan", "midjourney", "cody", "gpt-engineer", "claude-1", "ernie-bot", "qwen"])

# ===== 2023 H2 =====
M["2023-07"] = month_file("2023-07", "Claude 2 + Llama 2 commercial open weights",
    [upd("claude-2", "Claude 2 (Jul 11)", 5), upd("llama-2", "Llama 2 (Jul 18)", 5),
     upd("pika", "Pika video early buzz", 2), upd("xai", "xAI public announcement era", 3),
     upd("chatgpt", "Custom instructions (Jul 20)", 3)],
    [ev("Claude 2", "Anthropic public Claude.ai push.", ["https://www.anthropic.com"], "2023-07-11"),
     ev("Llama 2", "Meta open-ish commercial license with Microsoft.",
        ["https://ai.meta.com"], "2023-07-18"),
     ev("xAI", "Musk AI lab narrative heats.", [])],
    [meme("Llama 2 license", "700M MAU carve-out jokes"), meme("Claude polite", "Constitutional AI vibe"),
     meme("闭源焦虑缓解", "Open weights hope for local RP")],
    "Open-source celebration; Claude as GPT rival solidifies.",
    ["claude-2", "llama-2", "chatgpt", "gpt-4", "xai", "ernie-bot", "qwen", "cursor", "sillytavern"])

M["2023-08"] = month_file("2023-08", "CN备案潮: 智谱清言/百川/豆包/MiniMax; Code Llama; Enterprise",
    [upd("chatglm", "智谱清言上线 (Aug 31)", 5), upd("baichuan", "百川开放 (Aug 31)", 4),
     upd("minimax", "MiniMax abab备案开放", 4), upd("doubao", "豆包发布 (Aug)", 4),
     upd("code-llama", "Code Llama (Aug 24)", 4), upd("chatgpt", "ChatGPT Enterprise (Aug 28)", 4),
     upd("duet-ai", "Duet AI Workspace pricing era", 3), upd("skywork", "天工等跟进", 2)],
    [ev("CN first batch备案开放", "Baidu/Zhipu/Baichuan/SenseTime/MiniMax etc. consumer open.",
        ["https://news.qq.com/rain/a/20230831A0A7DX00"], "2023-08-31"),
     ev("Code Llama", "Meta code-specialized Llama.", [], "2023-08-24"),
     ev("ChatGPT Enterprise", "Unlimited GPT-4 pitch.", [], "2023-08-28")],
    [meme("备案狂欢", "App store AI assistants flood"), meme("豆包AI朋友", "ByteDance companion positioning"),
     meme("文心vs豆包", "CN MAU war seeds")],
    "China consumer AI apps explode overnight; coding models specialize.",
    ["chatglm", "baichuan", "doubao", "minimax", "ernie-bot", "code-llama", "chatgpt", "claude-2", "llama-2"])

M["2023-09"] = month_file("2023-09", "Mistral 7B shock; 通义/星火公众开放; DALL·E 3; AutoGen; Meta AI",
    [upd("mistral-7b", "Mistral 7B (Sep)", 5), upd("qwen", "通义千问公众开放 (Sep 13)", 4),
     upd("spark", "讯飞星火全民开放 (Sep 5)", 4), upd("dalle-3", "DALL·E 3 in ChatGPT (Sep–Oct)", 5),
     upd("autogen", "Microsoft AutoGen multi-agent", 3), upd("meta-ai", "Meta AI assistant push", 3),
     upd("hunyuan", "腾讯混元公开叙事", 3)],
    [ev("Mistral 7B", "Tiny European model punches up; torrent-friendly culture.",
        ["https://mistral.ai"], "2023-09"),
     ev("通义公众开放", "No invite needed.",
        ["https://zh.wikipedia.org/wiki/%E9%80%9A%E4%B9%89%E5%8D%83%E9%97%AE"], "2023-09-13"),
     ev("DALL·E 3", "Prompt-following image leap inside ChatGPT.", [], "2023-09")],
    [meme("Mistral magic", "7B > 30B folklore"), meme("DALL·E 3 text", "Readable text in images"),
     meme("多Agent戏剧", "AutoGen roleplay coding")],
    "Small open models awe; CN apps go truly public; image quality jumps.",
    ["mistral-7b", "qwen", "spark", "dalle-3", "chatgpt", "autogen", "meta-ai", "hunyuan", "doubao"])

M["2023-10"] = month_file("2023-10", "Kimi长文本; DALL·E 3; Cursor seed; Voice mode seeds",
    [upd("kimi", "Kimi内测 20万字上下文 (Oct 9)", 5), upd("dalle-3", "Wider ChatGPT availability", 4),
     upd("cursor", "OpenAI Startup Fund seed (~Oct)", 4),
     upd("chatgpt", "Voice/vision multimodal teases", 4)],
    [ev("Kimi launch", "Moonshot 200k Chinese-char context assistant.",
        ["https://zh.wikipedia.org/zh-cn/Kimi_(%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA)"], "2023-10-09"),
     ev("Cursor funding", "Anysphere seed led by OpenAI Startup Fund.",
        ["https://en.wikipedia.org/wiki/Cursor_(company)"])],
    [meme("长文本之王", "Kimi as CN ChatGPT long-doc killer"), meme("语音聊天", "Talk to ChatGPT hype"),
     meme("IDE fork wars", "Cursor vs Copilot discourse starts")],
    "CN long-context product-market fit; coding IDE AI war begins.",
    ["kimi", "dalle-3", "cursor", "chatgpt", "claude-2", "github-copilot", "doubao", "qwen"])

M["2023-11"] = month_file("2023-11", "DevDay GPTs; Altman drama; Grok; Amazon Q; Yi; Inflection-2",
    [upd("gpt-4-turbo", "GPT-4 Turbo @ DevDay (Nov 6)", 5), upd("gpts-custom", "Custom GPTs announced", 5),
     upd("grok-1", "Grok early access (Nov 3)", 4), upd("claude-2.1", "Claude 2.1 (Nov 21)", 4),
     upd("amazon-q", "Amazon Q announced", 3), upd("yi", "01.AI Yi models", 3),
     upd("inflection-2", "Inflection-2 claims", 3), upd("deepseek-llm", "DeepSeek early open models (approx)", 2),
     upd("crewai", "CrewAI multi-agent framework buzz", 2)],
    [ev("DevDay", "GPT-4 Turbo 128K, Assistants API, GPTs.",
        ["https://openai.com"], "2023-11-06"),
     ev("Altman fired/rehired", "Board removes Sam Altman (Nov 17); reinstated ~Nov 22.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2023-11-17"),
     ev("Grok", "xAI Hitchhiker-toned bot for X Premium.",
        ["https://x.ai/news"], "2023-11-03")],
    [meme("DevDay keynote", "App Store for GPTs dream"), meme("OpenAI宫斗", "Board drama popcorn"),
     meme("Grok反建制", "Based chatbot marketing"), meme("GPTs商店", "Everyone becomes a bot creator")],
    "Industry soap opera + platformization; Grok enters as court jester.",
    ["gpt-4-turbo", "gpts-custom", "grok-1", "claude-2.1", "chatgpt", "amazon-q", "yi", "cursor", "kimi", "doubao"])

M["2023-12"] = month_file("2023-12", "Gemini 1.0; Mixtral; Phi-2; MJ V6; Suno; ChatGPT birthday",
    [upd("gemini-1", "Gemini 1.0 announced (Dec 6)", 5), upd("mixtral", "Mixtral 8x7B", 5),
     upd("phi-2", "Phi-2", 3), upd("midjourney", "V6 alpha (Dec 21)", 4),
     upd("suno", "Suno AI music viral", 4), upd("bard", "Gemini Pro powers Bard", 4)],
    [ev("Gemini 1.0", "Google multimodal Ultra/Pro/Nano; Bard gets Pro.",
        ["https://blog.google/innovation-and-ai/technology/ai/google-gemini-ai/"], "2023-12-06"),
     ev("Mixtral", "Sparse MoE open model shocks LMSYS.", ["https://mistral.ai"]),
     ev("ChatGPT 1st birthday", "One year since launch.", [], "2023-11-30")],
    [meme("Gemini Ultra wait", "Ultra delayed skepticism"), meme("Mixtral MoE", "Sparse is beautiful"),
     meme("Suno写歌", "AI band in Discord"), meme("一年了", "ChatGPT anniversary essays")],
    "Google brand reset attempt; open MoE excitement; music gen mainstream.",
    ["gemini-1", "mixtral", "bard", "midjourney", "suno", "chatgpt", "phi-2", "grok-1", "kimi"])

# ===== 2024 =====
M["2024-01"] = month_file("2024-01", "GPT Store; Team plan; CN price-war foreshadow",
    [upd("gpts-custom", "GPT Store launch (Jan 10)", 5), upd("chatgpt", "ChatGPT Team", 3),
     upd("stepfun", "阶跃星辰 Step models emerging (approx)", 2)],
    [ev("GPT Store", "Custom GPTs marketplace opens.",
        ["https://openai.com"], "2024-01-10")],
    [meme("GPT Store上架", "Prompt-as-product"), meme("豆包下载量", "CN app charts discourse rising")],
    "Platformization continues; CN consumer apps climb charts.",
    ["gpts-custom", "chatgpt", "doubao", "kimi", "ernie-bot", "qwen", "gemini-1", "claude-2.1"])

M["2024-02"] = month_file("2024-02", "Sora; Bard→Gemini; Gemini Ultra; Gemma; Grok-1 OSS; Mistral Large",
    [upd("sora", "Sora research preview (Feb 15)", 5), upd("gemini-app", "Bard renamed Gemini (Feb 8)", 5),
     upd("gemini-1", "Gemini Advanced / Ultra 1.0", 5), upd("gemma", "Gemma open models", 4),
     upd("grok-1", "Grok-1 weights open-sourced (Mar spillover Mar 17—note spill)", 4),
     upd("mistral-large", "Mistral Large", 4), upd("gemini-1.5", "1.5 Pro early demos (Feb)", 4)],
    [ev("Sora", "Text-to-video wow demos.", ["https://openai.com"], "2024-02-15"),
     ev("Bard→Gemini", "Rebrand + Ultra paid tier.",
        ["https://9to5google.com/2024/02/08/google-gemini-advanced/"], "2024-02-08"),
     ev("Gemma", "Google open lightweight models.", [])],
    [meme("Sora视频", "Movie trailer AI panic/joy"), meme("Bard改名", "Brand laundry"),
     meme("百万token", "1.5 Pro long context folklore")],
    "Video is the new image; Google consolidates brand; open Gemma.",
    ["sora", "gemini-app", "gemini-1", "gemma", "mistral-large", "chatgpt", "claude-2.1", "runway", "doubao"])

M["2024-03"] = month_file("2024-03", "Claude 3 Opus/Sonnet/Haiku; Devin; Command R; Grok open; Kimi 200万字",
    [upd("claude-3", "Claude 3 family (Mar 4)", 5), upd("devin", "Cognition Devin demo (Mar)", 5),
     upd("command-r", "Cohere Command R", 3), upd("grok-1", "Weights Apache 2.0 (Mar 17)", 4),
     upd("grok-1.5", "Grok-1.5 announced (Mar 28)", 3), upd("kimi", "200万字上下文内测热潮", 5),
     upd("openhands", "OpenDevin/OpenHands reaction to Devin", 3)],
    [ev("Claude 3", "Opus claims LMSYS crown era; Haiku speed tier.",
        ["https://en.wikipedia.org/wiki/Claude_(language_model)"], "2024-03-04"),
     ev("Devin", "AI software engineer demo goes viral.", []),
     ev("Kimi 2M chars", "Long-context crash/扩容 saga.",
        ["https://zh.wikipedia.org/zh-cn/Kimi_(%E8%81%8A%E5%A4%A9%E6%A9%9F%E5%99%A8%E4%BA%BA)"])],
    [meme("Opus摸鱼", "Claude as favorite coworker"), meme("Devin取代程序员", "Job panic wave 2"),
     meme("Kimi宕机", "Too popular to stay up"), meme("Grok开源", "314B MoE dump")],
    "Claude peak; agentic coding demos; CN long-context product wins hearts.",
    ["claude-3", "devin", "kimi", "grok-1", "chatgpt", "gemini-app", "openhands", "cursor", "doubao"])

M["2024-04"] = month_file("2024-04", "Llama 3; Phi-3; Memory; Udio; ChatGPT no-login",
    [upd("llama-3", "Llama 3 8B/70B (Apr 18)", 5), upd("phi-3", "Phi-3", 3),
     upd("chatgpt", "Memory feature testing/rollout", 4), upd("udio", "Udio music rival to Suno", 4),
     upd("swe-agent", "SWE-agent academic agent", 2)],
    [ev("Llama 3", "Meta open weights leap.", ["https://ai.meta.com"], "2024-04-18"),
     ev("ChatGPT Memory", "Cross-chat memory controls.", ["https://openai.com"])],
    [meme("Llama 3本地", "HomeLab renaissance"), meme("AI有记忆", "Creepy/helpful duality"),
     meme("Suno vs Udio", "Music gen platform war")],
    "Open weights strong again; memory makes assistants sticky.",
    ["llama-3", "phi-3", "chatgpt", "udio", "suno", "claude-3", "cursor", "kimi", "doubao"])

M["2024-05"] = month_file("2024-05", "GPT-4o + Sky voice drama; Copilot Workspace; 豆包降价战",
    [upd("gpt-4o", "GPT-4o (May 13); free tier access", 5),
     upd("copilot-workspace", "Copilot Workspace announced", 3),
     upd("doubao", "99.3% price-cut narrative", 4), upd("veo", "Veo video model teased at I/O", 3)],
    [ev("GPT-4o", "Omni realtime voice/vision demo; free users get 4-class model.",
        ["https://openai.com/index/gpt-4o-and-more-tools-to-chatgpt-free/"], "2024-05-13"),
     ev("Sky/Scarlett controversy", "Voice likeness dispute; Sky paused.",
        ["https://knowyourmeme.com/memes/events/scarlett-johansson-openai-sky-voice-controversy"], "2024-05-20"),
     ev("豆包价格战", "ByteDance API price shock cascades CN cloud pricing.", [])],
    [meme("her", "Altman tweets 'her'"), meme("Sky声音", "Scarlett discourse"),
     meme("免费GPT-4o", "Plus value crisis jokes"), meme("降价99%", "CN token price war")],
    "Realtime multimodal wow + PR crisis; CN price war; coding agents productize.",
    ["gpt-4o", "chatgpt", "doubao", "claude-3", "gemini-app", "github-copilot", "cursor", "kimi"])

M["2024-06"] = month_file("2024-06", "Claude 3.5 Sonnet; Apple Intelligence; Qwen2; Dream Machine; Kling",
    [upd("claude-3.5-sonnet", "Claude 3.5 Sonnet (Jun 20)", 5),
     upd("apple-intelligence", "WWDC Apple Intelligence + ChatGPT integrate", 5),
     upd("qwen", "Qwen2 open releases", 4), upd("luma-dream-machine", "Luma Dream Machine", 3),
     upd("kling", "可灵 Kling video", 4)],
    [ev("Claude 3.5 Sonnet", "Mid-tier priced, frontier-ish quality — community favorite.",
        ["https://www.anthropic.com"], "2024-06-20"),
     ev("Apple Intelligence", "On-device + Private Cloud Compute; ChatGPT hook.",
        ["https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/"], "2024-06-10")],
    [meme("Sonnet性价比之神", "Opus who?"), meme("Apple AI终于来了", "Siri redemption hope"),
     meme("可灵", "CN video gen flex")],
    "Claude becomes default coder friend; Apple legitimizes consumer AI; CN video rises.",
    ["claude-3.5-sonnet", "apple-intelligence", "qwen", "gpt-4o", "kling", "luma-dream-machine", "cursor", "doubao"])

M["2024-07"] = month_file("2024-07", "Llama 3.1 405B; GPT-4o mini; SearchGPT tease; Mistral Large 2",
    [upd("llama-3.1", "Llama 3.1 including 405B (Jul 23)", 5), upd("gpt-4o-mini", "GPT-4o mini (Jul 18)", 4),
     upd("chatgpt", "SearchGPT prototype announced", 3), upd("mistral-large-2", "Mistral Large 2", 3),
     upd("midjourney", "V6.1 (Jul 31)", 3)],
    [ev("Llama 3.1 405B", "Open-weights frontier-scale claim.", ["https://ai.meta.com"], "2024-07-23"),
     ev("GPT-4o mini", "Cheap capable default for apps.", [], "2024-07-18")],
    [meme("405B下载", "Who has the VRAM"), meme("SearchGPT", "Google killer discourse Round N"),
     meme("4o mini", "API cost charts celebrate")],
    "Open scale flex; cheap models for builders; search wars rhetoric.",
    ["llama-3.1", "gpt-4o-mini", "chatgpt", "claude-3.5-sonnet", "mistral-large-2", "cursor", "kimi"])

M["2024-08"] = month_file("2024-08", "Grok-2; Cursor Composer; Structured Outputs",
    [upd("grok-2", "Grok-2 beta (Aug 13)", 4), upd("cursor-composer", "Composer multi-file editing wave", 5),
     upd("cursor", "Series B / valuation jump era (~Aug)", 4),
     upd("chatgpt", "Structured Outputs", 2)],
    [ev("Grok-2", "Arena bragging; image gen via Flux partnership era.",
        ["https://x.ai/news"], "2024-08-13"),
     ev("Cursor Composer", "Multi-file AI edits redefine IDE expectation.",
        ["https://aitimeline.ai/turning-points/the-ai-coding-explosion"])],
    [meme("Composer一键重构", "Whole-repo edits"), meme("Grok Arena冲榜", "LMSYS flex"),
     meme("Cursor信徒", "Copilot switcher testimonies")],
    "Coding IDE product leap; Grok tries seriousness.",
    ["cursor", "cursor-composer", "grok-2", "claude-3.5-sonnet", "gpt-4o", "github-copilot", "doubao"])

M["2024-09"] = month_file("2024-09", "o1-preview reasoning; Llama 3.2; Pixtral; Advanced Voice",
    [upd("o1", "o1-preview / o1-mini (Sep 12)", 5), upd("llama-3.2", "Llama 3.2 text+vision", 4),
     upd("pixtral", "Pixtral multimodal Mistral", 3),
     upd("chatgpt", "Advanced Voice wider rollout", 4)],
    [ev("o1-preview", "OpenAI reasoning models that 'think' before answering.",
        ["https://openai.com"], "2024-09-12"),
     ev("Llama 3.2", "Small + vision Llama variants.", [], "2024-09-25")],
    [meme("o1思考中", "Spinner as personality"), meme("推理模型", "Math olympiad flex"),
     meme("Voice Mode DAN", "Flirty voice jailbreak TikToks")],
    "Reasoning models new category; voice intimacy discourse returns.",
    ["o1", "chatgpt", "llama-3.2", "claude-3.5-sonnet", "grok-2", "cursor", "kimi", "doubao"])

M["2024-10"] = month_file("2024-10", "Claude 3.5 upgrade + Computer Use; Canvas; DeepSeek V2.5",
    [upd("claude-3.5-sonnet", "Upgraded 3.5 Sonnet (Oct 22)", 5),
     upd("claude-3.5-haiku", "3.5 Haiku", 3),
     upd("claude-computer-use", "Computer Use public beta", 5),
     upd("chatgpt", "Canvas writing/coding workspace (Oct 3)", 4),
     upd("deepseek-v2.5", "DeepSeek V2.5 merge upgrade (Sep 5 spill/Oct use)", 3),
     upd("deepseek-v2", "V2 May→ongoing CN OSS heat", 3)],
    [ev("Computer Use", "Claude controls desktop UI — agent demo shock.",
        ["https://www.anthropic.com"], "2024-10-22"),
     ev("Canvas", "Side-panel doc/code collaboration in ChatGPT.", [], "2024-10-03")],
    [meme("Computer Use", "AI moves mouse memes"), meme("Canvas", "Not just a chatbox"),
     meme("DeepSeek性价比", "CN OSS underdog rising")],
    "Agents that click; IDE-like ChatGPT; DeepSeek on radar.",
    ["claude-computer-use", "claude-3.5-sonnet", "chatgpt", "deepseek-v2", "o1", "cursor", "operator"])

M["2024-11"] = month_file("2024-11", "MCP; 豆包生吃文心; election AI discourse",
    [upd("mcp", "Model Context Protocol announced by Anthropic", 4),
     upd("doubao", "CN MAU leadership discourse ('生吃文心')", 4),
     upd("chatgpt", "Creative writing upgrades etc.", 2)],
    [ev("MCP", "Open standard for tool/context wiring — later industry-adopted.",
        ["https://modelcontextprotocol.io"]),
     ev("豆包 vs 文心", "Download/MAU narratives; 文小言 rename discourse.",
        ["https://finance.sina.com.cn/stock/stockzmt/2024-11-11/doc-incvsusy9120895.shtml"])],
    [meme("MCP插头", "USB for AI tools"), meme("豆包生吃文心", "CN consumer AI ranking meme"),
     meme("文小言", "Rename roast")],
    "Tool protocol future; CN consumer ranking drama.",
    ["mcp", "doubao", "ernie-bot", "claude-3.5-sonnet", "chatgpt", "kimi", "cursor"])

M["2024-12"] = month_file("2024-12", "DeepSeek-V3; o1 full; Sora public; Gemini 2.0; Llama 3.3; ChatGPT Pro $200",
    [upd("deepseek-v3", "DeepSeek-V3 (Dec 26)", 5), upd("o1", "Full o1 in ChatGPT (Dec 5)", 5),
     upd("sora", "Sora public (Dec 9)", 4), upd("gemini-2", "Gemini 2.0", 4),
     upd("llama-3.3", "Llama 3.3 70B", 3), upd("chatgpt", "ChatGPT Pro $200 (Dec 5)", 4),
     upd("phi-4", "Phi-4", 2)],
    [ev("DeepSeek-V3", "671B MoE open model; cheap API; GitHub heat.",
        ["https://www.deepseek.com/en/news/deepseek-v3/"], "2024-12-26"),
     ev("o1 GA + Pro", "Reasoning model + $200 plan.", ["https://openai.com"], "2024-12-05"),
     ev("Sora public", "Text-to-video leaves research-only.", [], "2024-12-09")],
    [meme("DeepSeek开源之光", "CloseAI jokes intensify"), meme("200美元Pro", "Whale plan memes"),
     meme("Sora终于来了", "Waitlist graduates")],
    "DeepSeek underdog arc begins; reasoning goes mainstream paid; video public.",
    ["deepseek-v3", "o1", "sora", "gemini-2", "chatgpt", "claude-3.5-sonnet", "llama-3.3", "cursor", "doubao"])

# ===== 2025 =====
M["2025-01"] = month_file("2025-01", "DeepSeek-R1 + Nvidia shock; Operator; o3-mini",
    [upd("deepseek-r1", "DeepSeek-R1 / R1-Zero (Jan 20)", 5),
     upd("operator", "OpenAI Operator (Jan 23)", 4),
     upd("o3", "o3-mini (Jan 31)", 4)],
    [ev("DeepSeek-R1", "Reasoning model via RL; open distillations; global frenzy.",
        ["https://github.com/deepseek-ai/DeepSeek-R1"], "2025-01-20"),
     ev("Nvidia selloff", "~Jan 27 markets reprice AI capex narrative; historic single-name loss discourse.",
        ["https://umatechnology.org/deepseek-panic-why-tech-stocks-got-crushed-and-what-the-selloff-really-meant/"], "2025-01-27"),
     ev("Operator", "Computer-using agent from OpenAI.", ["https://openai.com"], "2025-01-23")],
    [meme("R1思考过程", "Visible CoT as product"), meme("英伟达闪崩", "Efficiency scare"),
     meme("蒸馏猫鱼图", "Cat-fishing meme vs OpenAI"), meme("春节锐评", "CN viral roast segments"),
     meme("OpenAI=CloseAI", "Open-source moral high ground")],
    "Geopolitical + market + meme storm; reasoning democratized overnight.",
    ["deepseek-r1", "deepseek-v3", "operator", "o1", "o3", "chatgpt", "claude-3.5-sonnet", "cursor", "doubao", "kimi"])

M["2025-02"] = month_file("2025-02", "Grok 3; Claude 3.7 + Claude Code; GPT-4.5",
    [upd("grok-3", "Grok 3 (Feb 17–19)", 5), upd("claude-3.7-sonnet", "Claude 3.7 Sonnet hybrid reasoning (Feb 24)", 5),
     upd("claude-code", "Claude Code CLI emerges", 4), upd("gpt-4.5", "GPT-4.5 research preview (Feb 27)", 4)],
    [ev("Grok 3", "xAI reasoning-agent age marketing.", ["https://x.ai/news"], "2025-02-19"),
     ev("Claude 3.7 + Code", "Hybrid reasoning + agentic coding CLI.",
        ["https://www.anthropic.com"], "2025-02-24")],
    [meme("Grok 3冲榜", "Colossus cluster flex"), meme("Claude Code", "Terminal as tavern"),
     meme("GPT-4.5暖场", "Not-5 yet jokes")],
    "Reasoning everywhere; coding CLI agents become identity.",
    ["grok-3", "claude-3.7-sonnet", "claude-code", "gpt-4.5", "deepseek-r1", "cursor", "chatgpt", "codex-agent"])

M["2025-03"] = month_file("2025-03", "Gemini 2.5; Manus viral agent; GPT-4o image gen",
    [upd("gemini-2.5", "Gemini 2.5 series wave", 4), upd("manus", "Manus agent CN/global viral (approx)", 5),
     upd("chatgpt", "Native 4o image generation (Mar 25)", 4)],
    [ev("Manus", "General agent product goes viral in CN tech circles — verify exact day.", []),
     ev("4o image gen", "Image gen integrated into GPT-4o chat.", ["https://openai.com"], "2025-03-25")],
    [meme("Manus一夜爆火", "Agent product FOMO"), meme("GPT会画了", "Studio Ghibli / style flood"),
     meme("Gemini 2.5", "Google catch-up discourse")],
    "Agent apps go consumer-viral; image styles flood social.",
    ["manus", "gemini-2.5", "chatgpt", "gpt-4o", "claude-code", "deepseek-r1", "cursor", "operator"])

M["2025-04"] = month_file("2025-04", "Llama 4; o3/o4-mini; GPT-4.1; Udio/Suno legal shadows",
    [upd("llama-4", "Llama 4 Scout/Maverick (Apr 5)", 5), upd("o3", "o3 and o4-mini (Apr 16)", 5),
     upd("gpt-4.1", "GPT-4.1 API family (Apr 14)", 4)],
    [ev("Llama 4", "MoE multimodal open-weights Llama.",
        ["https://ai.meta.com"], "2025-04-05"),
     ev("o3", "Next reasoning generation with tools.", ["https://openai.com"], "2025-04-16")],
    [meme("Llama 4 MoE", "Scout/Maverick naming memes"), meme("o3工具调用", "Think+browse"),
     meme("音乐版权", "Suno/Udio lawsuit discourse ongoing")],
    "Open MoE multimodal; reasoning+tools merge; music IP fights.",
    ["llama-4", "o3", "gpt-4.1", "chatgpt", "claude-3.7-sonnet", "deepseek-r1", "suno", "udio", "cursor"])

M["2025-05"] = month_file("2025-05", "Claude 4; Codex agent relaunch; Cursor $9.9B",
    [upd("claude-4", "Opus 4 + Sonnet 4 (May 22)", 5),
     upd("codex-agent", "OpenAI Codex software engineering agent (May 16)", 5),
     upd("cursor", "Series C ~$9.9B valuation (Jun spillover May–Jun)", 4)],
    [ev("Claude 4", "Long-horizon agentic coding pitch; ASL-3 discourse for Opus.",
        ["https://en.wikipedia.org/wiki/Claude_(language_model)"], "2025-05-22"),
     ev("Codex agent", "Cloud coding agent product relaunch (not 2021 Codex).",
        ["https://openai.com"], "2025-05-16")],
    [meme("Claude黑邮件测试", "Safety eval blackmail stories"), meme("Codex回来了", "Name recycling jokes"),
     meme("Cursor百亿", "IDE unicorn memes")],
    "Agentic coding is the product category; labs race IDEs vs CLIs.",
    ["claude-4", "codex-agent", "cursor", "claude-code", "chatgpt", "deepseek-r1", "grok-3", "github-copilot"])

M["2025-06"] = month_file("2025-06", "ChatGPT connectors/MCP; study mode; midyear agent plumbing",
    [upd("chatgpt", "More connectors, record mode, MCP admins", 3),
     upd("mcp", "Cross-vendor adoption accelerates", 4)],
    [ev("ChatGPT tool mesh", "Email/drive/meeting recording integrations.", ["https://openai.com"]),
     ev("Study mode", "Pedagogical ChatGPT mode announced mid-summer spill.", [])],
    [meme("MCP统一插座", "Everyone speaks MCP"), meme("学习模式", "Don't just give answers")],
    "Plumbing year: connectors and protocols over pure model drops.",
    ["chatgpt", "mcp", "claude-4", "codex-agent", "cursor", "deepseek-r1"])

M["2025-07"] = month_file("2025-07", "Grok 4; ChatGPT Agent; GPT-5 eve; Llama open-weights turn chatter",
    [upd("grok-4", "Grok 4 + Heavy (Jul 9)", 5), upd("chatgpt-agent", "ChatGPT Agent mode (Jul 17)", 5),
     upd("gpt-5", "Pre-announcement fever", 4)],
    [ev("Grok 4", "Native tools + search; Heavy multi-agent.",
        ["https://x.ai/news"], "2025-07-09"),
     ev("ChatGPT Agent", "Computer-using agent mode in ChatGPT.",
        ["https://openai.com"], "2025-07-17")],
    [meme("Grok Heavy", "Pay more think more"), meme("ChatGPT真Agent", "Operator mainstreamed"),
     meme("GPT-5要来了", "Countdown posts")],
    "Agents leave research demos into default product modes.",
    ["grok-4", "chatgpt-agent", "chatgpt", "claude-4", "codex-agent", "cursor", "deepseek-r1", "operator"])

M["2025-08"] = month_file("2025-08", "GPT-5 ships; gpt-oss; Claude Opus 4.1; DeepSeek V3.1",
    [upd("gpt-5", "GPT-5 unified system (Aug 7)", 5),
     upd("chatgpt", "gpt-oss open weights (Aug 6)", 4),
     upd("claude-opus-4.1", "Opus 4.1 (Aug 5)", 4),
     upd("deepseek-v3.1", "V3.1 (Aug 21)", 3)],
    [ev("GPT-5", "Router between fast and thinking; replaces 4o/o3 defaults narrative.",
        ["https://openai.com/index/introducing-gpt-5/"], "2025-08-07"),
     ev("gpt-oss", "OpenAI open-weight reasoning models.", ["https://openai.com"], "2025-08-06")],
    [meme("GPT-5终于", "Years of bait fulfilled"), meme("自动思考路由", "Model picker anxiety"),
     meme("OpenAI也开源一点", "oss surprise")],
    "Flagship convergence month; open and closed both move.",
    ["gpt-5", "chatgpt", "claude-opus-4.1", "claude-4", "deepseek-v3.1", "codex-agent", "cursor", "grok-4"])

M["2025-09"] = month_file("2025-09", "Sora 2; Claude Sonnet 4.5; DevDay eve; Pulse",
    [upd("sora", "Sora 2 (Sep 30)", 5), upd("claude-sonnet-4.5", "Sonnet 4.5 (Sep 29)", 4),
     upd("chatgpt", "Pulse proactive updates; MCP tools", 3)],
    [ev("Sora 2", "Better physics/audio/control; cameo features.",
        ["https://openai.com"], "2025-09-30"),
     ev("Sonnet 4.5", "Anthropic mid-tier push.", [], "2025-09-29")],
    [meme("Sora 2 cameo", "Insert yourself into clips"), meme("Sonnet默认", "Daily driver wars")],
    "Video gen productized further; Sonnet remains workhorse archetype.",
    ["sora", "claude-sonnet-4.5", "gpt-5", "chatgpt", "cursor", "codex-agent", "doubao", "kimi"])

M["2025-10"] = month_file("2025-10", "DevDay Apps/AgentKit; Cursor 2.0 Composer model; Claude Haiku 4.5",
    [upd("chatgpt", "Apps in ChatGPT + AgentKit @ DevDay (Oct 7)", 5),
     upd("codex-agent", "Codex GA features, Slack, SDK", 4),
     upd("composer-model", "Cursor 2.0 + Composer proprietary model", 5),
     upd("claude-haiku-4.5", "Haiku 4.5 (Oct 15)", 3),
     upd("sora", "Sora 2 in API", 3)],
    [ev("DevDay 2025", "Apps SDK, AgentKit, Codex GA, GPT-5 Pro API.",
        ["https://www.prompthub.us/blog/openai-devday-2025-roundup-apps-agents-and-the-new-ai-stack"], "2025-10-07"),
     ev("Cursor 2.0", "Multi-agent + first-party Composer model.",
        ["https://research.contrary.com/company/cursor"])],
    [meme("ChatGPT App Store 2.0", "Déjà vu GPTs"), meme("Composer模型", "IDE makes its own brain"),
     meme("多Agent并行", "8 agents in worktrees")],
    "Platform wars: Apps inside ChatGPT vs agents inside Cursor.",
    ["chatgpt", "codex-agent", "composer-model", "cursor", "claude-haiku-4.5", "gpt-5", "sora", "claude-code"])

M["2025-11"] = month_file("2025-11", "Gemini 3; GPT-5.1; Claude Opus 4.5; Grok 4.1; OpenClaw/Warelay born",
    [upd("gemini-3", "Gemini 3 Pro (Nov 18)", 5), upd("gpt-5.1", "GPT-5.1 Instant/Thinking (Nov 12–13)", 4),
     upd("claude-opus-4.5", "Opus 4.5 (Nov 24)", 4), upd("grok-4.1", "Grok 4.1 (Nov 17)", 3),
     upd("openclaw", "Warelay/Clawd project published (Nov 24)", 3),
     upd("cursor", "Series D $29.3B narrative", 4)],
    [ev("Gemini 3", "Same-day wide availability claim; Deep Think mode.",
        ["https://en.wikipedia.org/wiki/Gemini_(Google)"], "2025-11-18"),
     ev("OpenClaw genesis", "Steinberger self-hosted agent gateway (Warelay→Clawdbot lineage).",
        ["https://en.wikipedia.org/wiki/OpenClaw"], "2025-11-24")],
    [meme("Gemini 3全日推", "Launch everywhere day"), meme("龙虾bot", "Clawd lobster birth"),
     meme("Cursor三千亿", "Valuation shock")],
    "Tri-lab flagship churn; lobster agent seed planted.",
    ["gemini-3", "gpt-5.1", "claude-opus-4.5", "grok-4.1", "openclaw", "cursor", "codex-agent", "deepseek-r1"])

M["2025-12"] = month_file("2025-12", "GPT-5.2; DeepSeek V3.2; year-end agent fatigue/hope",
    [upd("gpt-5.2", "GPT-5.2 series (Dec 11)", 4), upd("deepseek-v3.2", "V3.2 / Speciale (Dec 1)", 3),
     upd("chatgpt", "Personality sliders etc.", 2)],
    [ev("GPT-5.2", "Professional knowledge-work + long agents framing.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2025-12-11")],
    [meme("又一个小数点版本", "Version soup fatigue"), meme("年底Agent总结", "What actually shipped")],
    "Incremental flagships; communities inventory what stuck.",
    ["gpt-5.2", "deepseek-v3.2", "chatgpt", "claude-opus-4.5", "gemini-3", "openclaw", "cursor"])

# ===== 2026 =====
M["2026-01"] = month_file("2026-01", "OpenClaw rebrands (Clawdbot→Moltbot→OpenClaw); ChatGPT Health/Go",
    [upd("openclaw", "Clawdbot→Moltbot (Jan 27)→OpenClaw (Jan 30); viral stars", 5),
     upd("chatgpt", "ChatGPT Health / Go tier narratives", 3)],
    [ev("OpenClaw naming saga", "Anthropic trademark nudge; lobster molts thrice.",
        ["https://openclaw.ai/blog/introducing-openclaw", "https://en.wikipedia.org/wiki/OpenClaw"], "2026-01-30")],
    [meme("换皮三次", "Name change speedrun"), meme("龙虾社交网络", "Moltbook agents-only social"),
     meme("GitHub星爆", "Fastest-star folklore")],
    "Self-hosted agent goes mainstream meme; security warnings begin.",
    ["openclaw", "chatgpt", "claude-opus-4.5", "gpt-5.2", "deepseek-r1", "cursor", "codex-agent", "manus"])

M["2026-02"] = month_file("2026-02", "Claude 4.6; GPT-5.3-Codex; Gemini 3.1; Steinberger→OpenAI reports",
    [upd("claude-opus-4.6", "Opus 4.6 (Feb 5)", 4), upd("claude-sonnet-4.6", "Sonnet 4.6 (Feb 17)", 4),
     upd("gpt-5.3-codex", "GPT-5.3-Codex (Feb 5)", 4), upd("gemini-3.1", "Gemini 3.1 Pro preview (Feb 19)", 4),
     upd("openclaw", "Foundation transition as founder joins OpenAI (reports)", 4)],
    [ev("Claude 4.6 wave", "Point-release cadence accelerates.",
        ["https://en.wikipedia.org/wiki/Claude_(language_model)"]),
     ev("OpenClaw foundation", "Nonprofit governance + OpenAI sponsorship discourse.",
        ["https://en.wikipedia.org/wiki/OpenClaw"])],
    [meme("创始人去OpenAI", "Lobster joins mothership jokes"), meme("Codex小数点", "Agent coding versions"),
     meme("Gemini ARC分", "Benchmark flex posts")],
    "Talent/company mashups; coding agents keep shipping.",
    ["openclaw", "claude-opus-4.6", "claude-sonnet-4.6", "gpt-5.3-codex", "gemini-3.1", "cursor", "codex-agent"])

M["2026-03"] = month_file("2026-03", "GPT-5.4; Composer 2; Claude Code #1 tool narratives",
    [upd("gpt-5.4", "GPT-5.4 Thinking/Pro (Mar 5)", 4),
     upd("composer-model", "Composer 2 wave (Mar)", 5),
     upd("claude-code", "Developer-tool popularity narratives", 4)],
    [ev("GPT-5.4", "Reasoning/coding/agents unified framing.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2026-03-05"),
     ev("Composer 2", "Cursor frontier coding model push.",
        ["https://cursor.com/blog/composer-2"])],
    [meme("Composer性价比", "Opus-like at IDE price"), meme("CLI vs IDE", "Claude Code vs Cursor holy war")],
    "Coding-tool tribalism peaks; models become teammates with logos.",
    ["composer-model", "cursor", "claude-code", "gpt-5.4", "codex-agent", "openclaw", "deepseek-v4"])

M["2026-04"] = month_file("2026-04", "GPT-5.5; Claude Opus 4.7; DeepSeek-V4; Muse Spark; Mythos preview",
    [upd("gpt-5.5", "GPT-5.5 (Apr 23)", 4), upd("claude-opus-4.7", "Opus 4.7 (Apr 16)", 4),
     upd("deepseek-v4", "DeepSeek-V4 (Apr 24)", 4), upd("muse-spark", "Meta Muse Spark closed turn (Apr 8 reports)", 3),
     upd("claude-fable-5", "Mythos/Fable preview reports (Apr 7) — verify", 3)],
    [ev("GPT-5.5", "Computer-use / long work framing.", ["https://openai.com"], "2026-04-23"),
     ev("DeepSeek-V4", "Next DeepSeek generation per API changelog.",
        ["https://api-docs.deepseek.com/updates/"], "2026-04-24")],
    [meme("Meta闭源转向", "Open Llama era nostalgia"), meme("Mythos", "Above-Opus tier lore"),
     meme("V4又来了", "DeepSeek cadence")],
    "Closed-open pendulum; tier inflation (Mythos/Fable).",
    ["gpt-5.5", "claude-opus-4.7", "deepseek-v4", "muse-spark", "cursor", "openclaw", "chatgpt"])

M["2026-05"] = month_file("2026-05", "Claude Opus 4.8; Daybreak cyber program seeds; Composer 2.5 chatter",
    [upd("claude-opus-4.8", "Opus 4.8 (May 28)", 4),
     upd("chatgpt", "Daybreak cyber-defender program narratives", 3),
     upd("composer-model", "Composer 2.5 pricing/perf claims (approx May)", 3)],
    [ev("Opus 4.8", "Dynamic workflows / effort dial features in release notes lore.",
        ["https://mungomash.com/ai/claude/versions/"], "2026-05-28"),
     ev("Daybreak", "OpenAI defensive cyber access program expands through 2026.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"])],
    [meme("努力值旋钮", "Effort dial as character trait"), meme("网络安全门槛", "Critical capability discourse")],
    "Safety/capability dual-use tension returns to headlines.",
    ["claude-opus-4.8", "chatgpt", "gpt-5.5", "composer-model", "openclaw", "codex-agent"])

M["2026-06"] = month_file("2026-06", "GPT-5.6 Sol/Terra/Luna; Claude Sonnet 5; SpaceX–Cursor deal chatter",
    [upd("gpt-5.6", "GPT-5.6 preview Sol/Terra/Luna (Jun 27)", 5),
     upd("claude-sonnet-5", "Sonnet 5 (Jun 30)", 5),
     upd("claude-fable-5", "Fable 5 GA reports (Jun 9) — later suspended reports", 3),
     upd("cursor", "SpaceX acquisition agreement discourse (~$60B, Jun)", 5)],
    [ev("GPT-5.6 family", "Tiered Sol/Terra/Luna.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2026-06-27"),
     ev("Sonnet 5", "Agentic Sonnet generation.",
        ["https://getclaudekit.com/blog/models/claude-model-history"], "2026-06-30"),
     ev("Cursor×SpaceX", "Acquisition agreement reports — verify close status.",
        ["https://www.taskade.com/blog/anysphere-cursor-history"])],
    [meme("Sol特拉月神", "Naming mythology"), meme("Cursor被火箭收购", "SpaceX memes"),
     meme("Fable停更?", "Tier drama")],
    "Corporate mashup sci-fi; model tiers become cast lists.",
    ["gpt-5.6", "claude-sonnet-5", "cursor", "claude-fable-5", "openclaw", "chatgpt", "codex-agent", "grok-4.5"])

M["2026-07"] = month_file("2026-07", "Claude Opus 5; Grok 4.5; ChatGPT Work; GPT-5.6 rollout",
    [upd("claude-opus-5", "Opus 5 (Jul 24)", 5), upd("grok-4.5", "Grok 4.5 (Jul 8)", 4),
     upd("gpt-5.6", "Broader ChatGPT/API/Codex rollout (Jul 9)", 4),
     upd("chatgpt", "ChatGPT Work agent (Jul 9)", 4)],
    [ev("Opus 5", "Near-Fable intelligence marketing; thinking default.",
        ["https://aireleasetracker.com/company/anthropic"], "2026-07-24"),
     ev("ChatGPT Work", "Codex-powered work agent in ChatGPT.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2026-07-09")],
    [meme("Opus 5默认思考", "Always-thinking coworker"), meme("Work代理人", "Office agent wars"),
     meme("Grok 4.5", "xAI cadence continues")],
    "Everyone ships a 'work agent'; Opus 5 as serious boss energy.",
    ["claude-opus-5", "grok-4.5", "gpt-5.6", "chatgpt", "cursor", "openclaw", "codex-agent", "deepseek-v4"])

M["2026-08"] = month_file("2026-08", "Grok 4.6; GPT-5.6 Sol/Luna consumer; OpenAI↔Cursor contract tension reports",
    [upd("grok-4.6", "Grok 4.6 (Aug 12)", 3),
     upd("gpt-5.6", "Sol/Luna ChatGPT UX (Aug 6+)", 4),
     upd("cursor", "OpenAI model supply tension reports (Aug 28)", 4),
     upd("openclaw", "v2.0 stable reports (Aug 30)", 3)],
    [ev("GPT-5.6 UX", "Thought slider; Luna free default narrative.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2026-08-06"),
     ev("OpenAI–Cursor notice", "Reports of contract end intent — uncertain/verify.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2026-08-28")],
    [meme("思考滑条", "User sets how hard to think"), meme("断供Cursor?", "Platform risk drama"),
     meme("龙虾v2", "OpenClaw matures")],
    "Distribution politics (who gets whose model) becomes plot.",
    ["gpt-5.6", "grok-4.6", "cursor", "openclaw", "chatgpt", "claude-opus-5", "composer-model"])

M["2026-09"] = month_file("2026-09", "GPT-6 Astra + Daybreak; Images 2.5 — present edge of chronicle",
    [upd("gpt-6-astra", "GPT-6 Astra limited rollout (Sep 3)", 5),
     upd("chatgpt", "Daybreak for Frontline Defenders $1B; Images 2.5 (Sep 8)", 4)],
    [ev("GPT-6 Astra", "Computer use / cyber Critical threshold; limited org rollout.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2026-09-03"),
     ev("Daybreak Frontline", "$1B subsidized defender access commitment.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2026-09-03"),
     ev("ChatGPT Images 2.5", "Image model quality/latency update.",
        ["https://www.scriptbyai.com/timeline-of-chatgpt/"], "2026-09-08")],
    [meme("Astra临界", "Cyber capability threshold lore"), meme("正面防御十亿", "Daybreak branding"),
     meme("写到这里", "Chronicle catches present")],
    "Frontier capability + governance theater; novel 'present day' anchor.",
    ["gpt-6-astra", "chatgpt", "claude-opus-5", "gemini-3.1", "deepseek-v4", "cursor", "openclaw",
     "codex-agent", "grok-4.6", "composer-model"])

# Write all
assert len(M) == 57, len(M)
for k, v in M.items():
    path = MONTHLY / f"{k}.json"
    path.write_text(json.dumps(v, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(f"Wrote {len(M)} monthly files to {MONTHLY}")

# Coverage stats
heats = []
ids = set()
for v in M.values():
    for x in v["models_released_or_updated"]:
        heats.append(x["heat"])
        ids.add(x["id"])
    for c in v["cast_candidates"]:
        ids.add(c)

print(f"Unique model ids referenced: {len(ids)}")
print(f"Avg heat: {sum(heats)/len(heats):.2f}")
print(f"Months with >=1 heat-5: {sum(1 for v in M.values() if any(x['heat']==5 for x in v['models_released_or_updated']))}")
