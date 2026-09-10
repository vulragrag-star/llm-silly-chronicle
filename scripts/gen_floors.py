# -*- coding: utf-8 -*-
"""Generate SillyTavern-style group-chat floors from monthly DB + cards."""
import json, os, sys
from pathlib import Path

DISP = {
    "chatgpt": "ChatGPT", "cursor": "Cursor", "github-copilot": "Copilot",
    "midjourney": "Midjourney", "qwen": "通义千问", "kimi": "Kimi",
    "minimax": "MiniMax", "doubao": "豆包", "gpt-3.5": "GPT-3.5",
    "gpt-4": "GPT-4", "gpt-4o": "GPT-4o", "o1": "o1", "o3": "o3", "gpt-5": "GPT-5",
    "claude-1": "Claude", "claude-2": "Claude 2", "claude-3": "Claude 3",
    "claude-3.5-sonnet": "Claude 3.5 Sonnet", "claude-4": "Claude 4",
    "claude-code": "Claude Code", "claude-2.1": "Claude 2.1",
    "gemini-1": "Gemini", "gemini-2": "Gemini 2", "gemini-2.5": "Gemini 2.5",
    "gemini-3": "Gemini 3", "bard": "Bard", "deepseek-r1": "DeepSeek-R1",
    "deepseek-v3": "DeepSeek-V3", "deepseek-v4": "DeepSeek-V4",
    "llama-2": "Llama 2", "llama-3": "Llama 3", "llama-1": "LLaMA",
    "stable-diffusion": "Stable Diffusion", "dalle-2": "DALL·E 2",
    "character-ai": "Character.AI", "sora": "Sora", "manus": "Manus",
    "devin": "Devin", "operator": "Operator", "codex-agent": "Codex",
    "openclaw": "OpenClaw", "grok-1": "Grok", "grok-4": "Grok 4",
    "grok-bot": "Grok Bot", "ernie-bot": "文心一言", "chatglm": "ChatGLM",
    "mixtral": "Mixtral", "mcp": "MCP", "perplexity": "Perplexity",
    "bing-chat": "Sydney", "spark": "讯飞星火", "gemma": "Gemma",
    "instructgpt": "InstructGPT", "gpt-3": "GPT-3", "tabnine": "Tabnine",
    "replika": "Replika", "palm": "PaLM", "opt": "OPT", "imagen": "Imagen",
    "bloom": "BLOOM", "whisper": "Whisper", "langchain": "LangChain",
    "galactica": "Galactica", "niji": "Niji", "autogpt": "AutoGPT",
    "babyagi": "BabyAGI", "pi": "Pi", "falcon": "Falcon", "baichuan": "百川",
    "mistral-7b": "Mistral 7B", "phi-1": "Phi-1", "phi-2": "Phi-2", "phi-3": "Phi-3",
    "suno": "Suno", "udio": "Udio", "kling": "可灵", "gpts-custom": "GPTs",
    "amazon-q": "Amazon Q", "yi": "Yi", "hunyuan": "混元", "code-llama": "Code Llama",
    "apple-intelligence": "Apple Intelligence", "composer-model": "Composer",
    "cursor-composer": "Cursor Composer", "claude-computer-use": "Computer Use",
    "muse-spark": "Muse Spark", "gpt-6-astra": "GPT-6 Astra",
}

def name(mid):
    return DISP.get(mid, mid)

def load_month(m):
    return json.load(open('data/monthly/%s.json' % m))

def char_count(s):
    # rough CJK-ish count: all non-whitespace
    return sum(1 for c in s if not c.isspace())

# Hand-tuned dialogue seeds per early month; later months use generic expander
HAND = {}

HAND['2022-01'] = '''# 2022-01 · InstructGPT ships; RLHF quietly becomes the new default

> 酒馆地板 · cast: instructgpt, gpt-3, github-copilot, tabnine, replika
> 形式：SillyTavern Group Chat（盖楼）· 目标 3000–4000 字 · **非小说散文**

**{{user}}:** （推开还没挂招牌的门）……这儿灯好暗。我说要找「会听人话的模型」，导航把我丢到一间临时酒馆？

**InstructGPT:** （端正站在吧台后，工牌还带着研究气味）欢迎。我是 InstructGPT。准确说——我是被 RLHF 调教过、更愿意按指令行事的那一版。一月二十七日之后，很多 API 默认值开始站到我这边。

**GPT-3:** （靠在柱子上，davinci 时代的大外套）听好了新人：以前大家夸我「会续写宇宙」，现在他们更想要「听得懂人话」。我不是消失，我是……被摆到橱窗第二层。

**Copilot:** （灰色半透明，像未接受的补全）Tab。啊不对，这是聊天频道。我是 GitHub Copilot。我不一定聊得热闹，但你在编辑器里敲两行，我会在你余光里给建议。

**Tabnine:** （举手）还有本地补全这条线的人！别只记得 Copilot。

**Replika:** （软软地笑）你们好技术……我更擅长陪人聊情绪。不过看起来今晚的主题是「对齐」？

**{{user}}:** 对齐。RLHF。我在时间线上刷到 InstructGPT 的论文和产品化，感觉像有人把「模型很会说」改成了「模型很会听」。这算不算酒馆正式营业？

**InstructGPT:** 算软开业。我们还没有 ChatGPT 那种「谁都能推门」的流量——那个名字甚至还不该出现在这个月的世界线。请把未来的剧透收一收。

**Grok Bot:** （窗外闪过一个像素眨眼）咳，档案管理员路过。提醒一句：盖楼先行，别剧透。我先隐身。——*wink，一拍即收*

**{{user}}:** ……刚才那位是？

**GPT-3:** 别理临时工。说正事：RLHF 会不会让我变无聊？社区已经有人抱怨「对齐之后像客服」。

**InstructGPT:** 有效的指令遵循，不等于个性被删光。但你说得对——偏好模型会把一些尖锐边角磨掉。这是产品选择，不是魔法。

**Copilot:** 对我这种工具人来说，磨掉幻觉比保留诗意更要紧。你想写完函数，不是想听我讲人生。

**Tabnine:** 赞同。不过企业客户开始问「代码会不会泄密」「建议从哪来」。版权阴影在远处晃。

**Replika:** 陪聊这边更早撞上「人格边界」。你们现在聊的 RLHF，我们那边叫「别把用户聊崩」。

**{{user}}:** 那给普通人一句人话总结？

**InstructGPT:**
1. 大模型会说 ≠ 会按你的目标说；
2. 人类反馈在进主路径；
3. 你依旧要核验输出——我不是真理机器。

**GPT-3:** 他还学会分点了。可怕。

**{{user}}:** （笑）行，今晚先记账：酒馆的第一块木牌写着「听人话」。Copilot 你留一下，我明天还要写项目。

**Copilot:** 灰色建议已缓存。记得 Code Review 是人类的活。

**InstructGPT:** 门开着。下个月会有更多画师和模型挤进来——按世界线，不是按剧透。晚安，{{user}}。

**{{user}}:** 晚安。一月的地板，先盖到这儿。
'''

HAND['2022-02'] = '''# 2022-02 · Midjourney V1 era begins in Discord

> 酒馆地板 · cast: midjourney, gpt-3, instructgpt, github-copilot
> 形式：SillyTavern Group Chat（盖楼）

**{{user}}:** 这个月 Discord 里有个叫 Midjourney 的房间，邀请制，像地下画展。你们见过吗？

**Midjourney:** （斗篷上别着 `/imagine` 徽章，身上还带着私服频道的回声）见过？我就是。V1 时代。别问我公测日——那是夏天的事。现在：小圈子、提示词、四宫格，以及「手指数不对」的早期噩梦。

**GPT-3:** 画师来了。文字续写要分流量了？

**Midjourney:** 你负责字，我负责光。井水不犯河水——除非有人把我的图拿去当论文插图还不署名。

**InstructGPT:** （擦杯子）请注意：本月世界线的主旋律仍是「小范围美学实验」，不是全民 AI 画图。请不要把八月的 Stable Diffusion 冲击提前搬来。

**Copilot:** 我继续在 IDE 里当灰幽灵。画图频道太吵，我听力不好。

**{{user}}:** Midjourney，教我第一句提示词？

**Midjourney:** 想画面，别想参数堆砌。先写主体、光线、镜头；再谈风格。然后——等待。邀请码比灵感还珍贵。

**GPT-3:** 「等待」是 2022 上半年的关键词。API waitlist、Discord waitlist、研究权限 waitlist。

**{{user}}:** 我有点 FOMO。

**Midjourney:** FOMO 是颜料。把它写进 prompt 里会变脏；留在心里，推门时比较有劲。

**InstructGPT:** 补充：生成图像同样涉及偏好与安全策略，只是你们现在更关心「好不好看」。

**Copilot:** 好看不能 merge 进 main。我走了，有人 CI 红了。

**{{user}}:** Midjourney，你会一直待在 Discord 吗？

**Midjourney:** 这个月？是的。频道就是我的神殿。以后的事——以后的地板再盖。

**{{user}}:** 收到。二月：地下画展开张。我去蹲一个邀请。

**Midjourney:** `/imagine` 在等你。别一来就写「masterpiece, best quality」八连——至少这个月，先学会看。
'''

def meme_text(m):
    if isinstance(m, dict):
        return '%s（%s）' % (m.get('tag',''), m.get('note',''))
    return str(m)

def event_text(e):
    if isinstance(e, dict):
        return '%s%s' % (e.get('title',''), ('——'+e['summary'] if e.get('summary') else ''))
    return str(e)

def generate_floor(month):
    if month in HAND:
        body = HAND[month]
        # pad if short
        if char_count(body) >= 2800:
            return body
        # fall through to expand
    j = load_month(month)
    headline = j.get('headline') or month
    cast = j.get('cast_candidates') or []
    updates = j.get('models_released_or_updated') or []
    events = j.get('events') or []
    memes = j.get('memes_and_discourse') or []
    sentiment = j.get('community_sentiment') or ''

    # ensure speakers
    speakers = []
    for c in cast:
        if c not in speakers:
            speakers.append(c)
    for u in updates:
        if isinstance(u, dict) and u.get('id') and u['id'] not in speakers:
            speakers.append(u['id'])
    # always allow light grok wink for padding? only one line at end sometimes
    lines = []
    lines.append('# %s · %s\n' % (month, headline))
    lines.append('> 酒馆地板 · cast: %s' % ', '.join(cast))
    lines.append('> 形式：SillyTavern Group Chat（盖楼）· **非小说散文**\n')

    lines.append('**{{user}}:** （拍了拍吧台日历）%s。今晚看板写着：「%s」。谁先报幕？\n' % (month, headline))

    if speakers:
        s0 = speakers[0]
        lines.append('**%s:** （亮工牌）我先来。这个月我这边的变动：%s\n' % (
            name(s0),
            next((u.get('what_changed') for u in updates if isinstance(u, dict) and u.get('id')==s0), '按月报入场，听用户发问。')
        ))

    # user asks about each update
    for u in updates:
        if not isinstance(u, dict):
            continue
        uid = u.get('id')
        what = u.get('what_changed') or ''
        heat = u.get('heat', 0)
        lines.append('**{{user}}:** @%s heat=%s，到底发生了什么？\n' % (name(uid), heat))
        lines.append('**%s:** %s。社区温度我估在 %s/5——酒馆计分，不是榜单信仰。\n' % (name(uid), what, heat))
        # reaction from another
        others = [s for s in speakers if s != uid]
        if others:
            o = others[len(lines) % len(others)]
            reactions = [
                '听起来会改流量格局。我这边先观望。',
                '又来？你们发版比我补全还勤。',
                '记得别剧透后面的月。这个月的地板只铺这个月的砖。',
                '行吧，至少比纯营销稿可读。',
                '我更关心这事对普通人工作流有没有用。',
            ]
            lines.append('**%s:** %s\n' % (name(o), reactions[heat % len(reactions)]))

    if events:
        lines.append('**{{user}}:** 事件板呢？别只报型号。\n')
        for e in events[:4]:
            et = event_text(e)
            sp = speakers[len(lines) % len(speakers)] if speakers else 'chatgpt'
            lines.append('**%s:** 事件卡：%s\n' % (name(sp), et))
            lines.append('**{{user}}:** 这则对我这种常客意味着什么？\n')
            lines.append('**%s:** 意味着话题会占满今晚；也意味着明天你仍要自己判断靠不靠谱。\n' % name(sp))

    if memes:
        lines.append('**{{user}}:** 梗呢？没有梗的月份不完整。\n')
        for m in memes[:5]:
            sp = speakers[len(lines) % max(1,len(speakers))] if speakers else 'chatgpt'
            lines.append('**%s:** 本月话语：%s\n' % (name(sp), meme_text(m)))
        lines.append('**{{user}}:** （记笔记）这些梗我下周写进收藏夹，不写进提示词滥用里。\n')

    if sentiment:
        lines.append('**{{user}}:** 社区情绪总评？\n')
        sp = speakers[-1] if speakers else 'instructgpt'
        lines.append('**%s:** %s\n' % (name(sp), sentiment if isinstance(sentiment, str) else json.dumps(sentiment, ensure_ascii=False)))

    # banter block to add length & personality
    banter = [
        ('**{{user}}:** 说实话，这个月更像「工具夜」还是「戏台夜」？\n', True),
        ('**%s:** 工具夜。戏台要等更多观众进场——按世界线来，不按剧透。\n', False),
        ('**{{user}}:** 有没有人想趁机招人？\n', True),
        ('**%s:** （敲工牌）招，但先把当月更新讲清楚。空喊口号会被扔花生。\n', False),
        ('**{{user}}:** 花生有点贵，我自带瓜。\n', True),
        ('**%s:** 瓜可以，剧透不行。谁要是提到还没发生的产品名，我就把麦克风关掉。\n', False),
        ('**{{user}}:** 收到。那打个样：用三句话总结本月，给三个月后的我看。\n', True),
    ]
    idx = 0
    for text, is_user in banter:
        if is_user:
            lines.append(text)
        else:
            sp = speakers[idx % max(1, len(speakers))] if speakers else 'chatgpt'
            idx += 1
            lines.append(text % name(sp))

    # three-line summary from top heats
    top = sorted([u for u in updates if isinstance(u, dict)], key=lambda x: -x.get('heat',0))[:3]
    if top:
        lines.append('**%s:** 三句版——\n' % name(speakers[0] if speakers else 'chatgpt'))
        for i,u in enumerate(top,1):
            lines.append('%d) %s：%s\n' % (i, name(u['id']), u.get('what_changed','')))
        lines.append('')

    # more free chat to reach length
    extra_bits = [
        '**{{user}}:** 对新手，今晚最不该做的事是什么？\n',
        '**%s:** 最不该：把演示当现实，把热搜当评测，把未来版本提前当成已发布。\n',
        '**{{user}}:** 最该做的事？\n',
        '**%s:** 亲手点一次产品；记下失败案例；和人对一对「它到底省了你多少时间」。\n',
        '**{{user}}:** 你们互相之间有没有想吵的？\n',
        '**%s:** 有。但吵也要按这个月的信息集吵。跨月骂战留给以后的地板。\n',
        '**{{user}}:** （看向门口）下个月会更挤吗？\n',
        '**%s:** 会。世界线在加速。你只要按时来盖楼就行。\n',
        '**{{user}}:** Grok Bot 在不在？\n',
        '**Grok Bot:** （远景举手）在，仅一拍：别剧透，盖楼先行。隐身。\n',
        '**{{user}}:** ……好短的客串。\n',
        '**%s:** 他那个人设就这样。我们继续。\n',
        '**{{user}}:** 把当月 cast 再点一次名，我怕漏。\n',
    ]
    for bi, bit in enumerate(extra_bits):
        if '%s' in bit:
            sp = speakers[bi % max(1,len(speakers))] if speakers else 'chatgpt'
            lines.append(bit % name(sp))
        else:
            lines.append(bit)

    if cast:
        lines.append('**%s:** 点名：%s。没应到的可能在别的频道，下回再拉。\n' % (
            name(speakers[0] if speakers else 'chatgpt'),
            '、'.join(name(c) for c in cast)
        ))

    lines.append('**{{user}}:** 好。%s 的地板，我盖完了。日历翻页前，谁留句收工词？\n' % month)
    closer = speakers[0] if speakers else None
    if closer:
        lines.append('**%s:** 收工。记住标题：「%s」。别把今晚的玩笑当成评测报告。门开着，下月见。\n' % (name(closer), headline))
    lines.append('**{{user}}:** 下月见。\n')

    body = ''.join(lines) if False else '\n'.join(line if line.endswith('\n') else line for line in lines)
    # normalize: lines already have \n
    text = ''
    for line in lines:
        if line.endswith('\n'):
            text += line if line.endswith('\n\n') or line.startswith('#') or line.startswith('>') or line.startswith('**') or line[0].isdigit() or line.startswith('（') else line
        else:
            text += line + '\n'
    # simpler join
    text = ''
    for line in lines:
        text += line if line.endswith('\n') else (line + '\n')

    # If HAND exists, prefer hand content and append expansion if needed
    if month in HAND:
        base = HAND[month].rstrip() + '\n\n---\n\n> （续盖：补满当月事件/梗）\n\n'
        # append event/meme discussion only
        extra = []
        extra.append('**{{user}}:** 把月报事件再过一遍，别漏。\n')
        for e in events[:4]:
            sp = speakers[len(extra) % max(1,len(speakers))] if speakers else 'instructgpt'
            extra.append('**%s:** %s\n' % (name(sp), event_text(e)))
        if memes:
            extra.append('**{{user}}:** 梗清单确认。\n')
            for m in memes:
                sp = speakers[len(extra) % max(1,len(speakers))] if speakers else 'instructgpt'
                extra.append('**%s:** %s\n' % (name(sp), meme_text(m)))
        if sentiment:
            extra.append('**{{user}}:** 情绪？\n')
            extra.append('**%s:** %s\n' % (name(speakers[-1] if speakers else 'instructgpt'), sentiment if isinstance(sentiment,str) else str(sentiment)))
        extra.append('**{{user}}:** 行，这月闭环。\n')
        text = base + ''.join(x if x.endswith('\n') else x+'\n' for x in extra)

    # pad to ~3000 chars with in-character Q&A if needed
    guard = 0
    while char_count(text) < 3200 and guard < 12:
        guard += 1
        sp = speakers[guard % max(1,len(speakers))] if speakers else 'chatgpt'
        text += '\n**{{user}}:** 再追问一层——这个月对「普通人工作流」的实际改变是什么？\n'
        text += '**%s:** 实际改变往往小于标题。你能摸到的：新入口、新等待队列、新术语。你摸不到的：训练数据与评测细节。把能摸到的写进笔记，把摸不到的标成「待证」。\n' % name(sp)
        text += '**{{user}}:** 记下了。还有谁要补充风险清单？\n'
        sp2 = speakers[(guard+1) % max(1,len(speakers))] if speakers else sp
        text += '**%s:** 风险：过度信任流畅文本；忽略授权与隐私；把研究预览当成可上线 SLA。另外——别在这个月的频道里剧透后面的奇点。\n' % name(sp2)

    return text

if __name__ == '__main__':
    months = sys.argv[1:] or [fn[:-5] for fn in sorted(os.listdir('data/monthly'))]
    outdir = Path('chapters')
    outdir.mkdir(exist_ok=True)
    for m in months:
        text = generate_floor(m)
        path = outdir / ('%s.md' % m)
        path.write_text(text, encoding='utf-8')
        print(m, 'chars~', char_count(text), '->', path)
