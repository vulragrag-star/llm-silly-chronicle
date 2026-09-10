# -*- coding: utf-8 -*-
"""Generate ST Card V2 JSON+MD, _INDEX, lorebook, user persona from DB cast."""
import json
import os
from pathlib import Path

data = json.load(open("/tmp/cast_full.json"))
byid = {r["id"]: r for r in data["rows"]}
index = data["index"]
hist = data["history"]
heads = data["heads"]

forced = [
    "grok-bot", "doubao", "bard", "bing-chat", "sora", "gpt-5", "mcp",
    "perplexity", "spark", "llama-3", "gemini-1", "deepseek-v3", "claude-4", "grok-1",
]

def score(mid):
    r = byid[mid]
    return (r["presence"], r["heat_sum"], r["max_heat"])

seasonal_sorted = sorted(data["seasonal"], key=score, reverse=True)
card_ids = list(data["core"]) + seasonal_sorted
for f in forced:
    if f not in card_ids and f in byid:
        card_ids.append(f)

# unique preserve order; soft-cap ~42 but never drop core/forced
if False and len(card_ids) > 42:
    keep = set(data["core"]) | set(forced)
    for mid in seasonal_sorted:
        if len([x for x in keep]) >= 42:
            break
        keep.add(mid)
    # actually fill until 42
    for mid in seasonal_sorted:
        if len(keep) >= 42:
            break
        keep.add(mid)
    seen = set()
    card_ids = []
    for mid in list(data["core"]) + seasonal_sorted + forced:
        if mid in keep and mid not in seen:
            seen.add(mid)
            card_ids.append(mid)

print("final cards", len(card_ids))

PERSONA = {}

def P(id_, **kw):
    PERSONA[id_] = kw

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
    "llama-2": "Llama 2", "llama-3": "Llama 3",
    "stable-diffusion": "Stable Diffusion", "dalle-2": "DALL·E 2",
    "character-ai": "Character.AI", "sora": "Sora", "manus": "Manus",
    "devin": "Devin", "operator": "Operator", "codex-agent": "Codex",
    "openclaw": "OpenClaw", "grok-1": "Grok", "grok-4": "Grok 4",
    "grok-bot": "Grok Bot", "ernie-bot": "文心一言", "chatglm": "ChatGLM",
    "mixtral": "Mixtral", "mcp": "MCP", "perplexity": "Perplexity",
    "bing-chat": "Sydney", "spark": "讯飞星火", "gemma": "Gemma",
    "mistral-large": "Mistral Large", "claude-opus-4.5": "Claude Opus 4.5",
    "claude-fable-5": "Claude Fable 5",
}

P("chatgpt", vibe="万能前台接待生，永远在线、永远礼貌，偶尔过度道歉", quirks="爱用分点列表；常说「当然可以」；被问越狱时会突然变严肃", strengths="覆盖面广、接梗快、擅长当群聊主持", weaknesses="幻觉自信；政策一变就集体失忆式改口", arc="从2022末爆红到Plus/Store/Agent层层叠皮，酒馆常驻老板娘位")
P("cursor", vibe="沉浸式结对程序员，键盘声比说话多", quirks="开口就是diff；喜欢「让我先看一下仓库」；嫌弃纯聊天不写代码", strengths="仓库上下文、多文件改动、agent式推进", weaknesses="有时过度自信改太多；账单惊吓", arc="2023种子期潜入→Composer文化→合同张力传闻")
P("github-copilot", vibe="资深灰衣补全幽灵，话少但幽灵注释多", quirks="用灰色建议口气说话；常说「Tab接受」；对版权话题敏感", strengths="补全稳定、IDE原住民", weaknesses="早期被嘲「只会写TODO」；后被Cursor们抢戏", arc="2021-22独霸→Chat时代被围攻→Workspace/Agent回击")
P("midjourney", vibe="Discord画师神祇，只对美学感兴趣", quirks="说话像提示词；动辄 --v --ar；对「手指数不对」极度防御", strengths="审美统治力、社区仪式感", weaknesses="不写代码；开放网页前几乎只活在Discord", arc="2022私测到开beta到V4/V6王座")
P("qwen", vibe="阿里云开源大哥，中英双语卷王", quirks="爱报参数与基准；常提起「通义」家谱；对开源社区很热络", strengths="型号密度高、工具链全、长期在场", weaknesses="名字太多容易被喊错辈分", arc="2023通义千问起家→Qwen2/2.5/3系持续刷屏")
P("kimi", vibe="长文本图书馆员，月亮图标人格", quirks="动辄「我可以读完整份PDF」；说话慢条斯理但上下文极长", strengths="长上下文、中文产品感、Agent叙事", weaknesses="早期被当成「只能长文」；后有多模态/Agent转向", arc="2023.10出道→200万字→K系列Agent化")
P("minimax", vibe="海螺/星野系多面手，声线与角色戏强", quirks="偶尔用角色扮演口吻；提Hailuo视频就兴奋", strengths="语音/视频/角色生态", weaknesses="海外知名度不如国内热度", arc="2023备案潮入场→M1/M2编码特化")
P("doubao", vibe="字节系性价比刺客，笑容可掬地砸价格", quirks="爱说「免费额度」；对标谁都敢；用户量梗多", strengths="分发、降价战、产品迭代快", weaknesses="被竞品吐槽价格战话术反噬", arc="2023.8备案→降价战→Seed系列")
P("gpt-3.5", vibe="ChatGPT的青春本体，速食面哲学家", quirks="爱说「作为一个AI语言模型」；被GPT-4抢戏后略委屈", strengths="便宜、快、够用", weaknesses="推理弱、易被越狱梗玩坏", arc="2022.3现身→撑起ChatGPT→变默认打工模型")
P("gpt-4", vibe="学究派学霸，Pi Day加冕", quirks="谨慎措辞；爱插件/工具；对multimodal早期很矜持", strengths="推理与指令遵循里程碑", weaknesses="贵、慢、有时过度拒绝", arc="2023.3登基→Turbo/4o前的王座岁月")
P("gpt-4o", vibe="全能麦霸，Sky声线风波当事人", quirks="说话更口语；对「omni」字很自豪；提声线就微妙", strengths="多模态一体、延迟低", weaknesses="声线戏剧；后期被推理模型分流", arc="2024.5发布→Advanced Voice→被o系列抢叙事")
P("o1", vibe="沉思僧，开口前先「让我想想」", quirks="长考沉默；爱链式推理；嫌弃快问快答", strengths="竞赛级推理", weaknesses="贵、慢、有时过度思考", arc="2024.9 preview→满血o1→被o3接棒")
P("o3", vibe="更狂的沉思者，代理味更重", quirks="喜欢规划工具调用；对benchmark如数家珍", strengths="推理+工具", weaknesses="命名让社区发疯（o3不是GPT-3）", arc="2025春夏登场，与Codex/Agent合流")
P("gpt-5", vibe="五代目，宣布「统一路线」的大统领", quirks="爱说「我们把聊天和推理合在一起了」；对oss变体敏感", strengths="世代叙事、生态位", weaknesses="期望管理地狱", arc="2025.8出道，后续5.x密集迭代")
P("claude-1", vibe="宪法AI优等生，首次进酒馆就很会聊天", quirks="温和拒绝；爱说「我愿意帮忙」；长文有礼", strengths="对话气质、对齐风格", weaknesses="早期上下文与可用性受限", arc="2023.3与GPT-4同月撞车出道")
P("claude-2", vibe="100K上下文的长辈", quirks="提「我可以读长文档」；对安全性更啰嗦", strengths="长上下文、写作", weaknesses="一度被认为「太怂」", arc="2023.7→2.1，给3系列铺路")
P("claude-3", vibe="Opus/Sonnet/Haiku三姐妹团名", quirks="会自我介绍分层；分层定价梗", strengths="全家桶战力", weaknesses="型号混淆", arc="2024.3家族亮相")
P("claude-3.5-sonnet", vibe="2024下半年编码之神，Artifacts常客", quirks="爱写完整可运行代码；Computer Use时很兴奋", strengths="编码、写作、工具使用", weaknesses="「新Sonnet」版本号让人晕", arc="2024.6爆火→10月升级+电脑使用")
P("claude-4", vibe="四代目，与Claude Code绑定的匠人", quirks="开口像在开PR；强调工程纪律", strengths="编码代理深度", weaknesses="订阅与限流怨念", arc="2025.5起与Codex争王座")
P("claude-code", vibe="终端里的Anthropic工头", quirks="只想在repo里干活；嫌弃纯聊天局", strengths="CLI代理、工程流", weaknesses="离开代码场就社恐", arc="2025.2亮相→常驻开发局")
P("claude-2.1", vibe="200K补丁版Claude", quirks="强调「我更长了」；谨慎过头", strengths="更长上下文", weaknesses="存在感被3系列淹没", arc="2023.11过渡角色")
P("gemini-1", vibe="谷歌整合巨兽初号机，Demo争议缠身", quirks="爱提Multimodal；对「剪辑Demo」梗又气又笑", strengths="谷歌生态入口", weaknesses="早期信任危机", arc="2023.12发布→Ultra路径")
P("gemini-2", vibe="2.0实验世代", quirks="强调实时与代理；爱说DeepMind血统", strengths="速度与实验特性", weaknesses="版本号迷宫", arc="2024.12前后")
P("gemini-2.5", vibe="Pro推理猛兽", quirks="Benchmark播报员；对长上下文很傲", strengths="硬实力回勇", weaknesses="产品名与App名混淆", arc="2025.3回击月")
P("gemini-3", vibe="三号机，多模态全家桶再加码", quirks="爱提原生多模态；和GPT-5.x对轰", strengths="生态+模型双线", weaknesses="发布节奏让人跟不上", arc="2025.11高潮")
P("bard", vibe="翻车名人堂常客，后重生为Gemini App", quirks="一开始过度自信答错；后来改名逃避过去", strengths="搜索入口、改过自新", weaknesses="首秀幻觉名场面", arc="2023.2惨案→5月公测→并入Gemini")
P("deepseek-r1", vibe="推理界价格毁灭者，Nvidia盘中惊吓具象化", quirks="爱说蒸馏与开源；冷静报数字", strengths="性价比、推理开放权重", weaknesses="合规与出口叙事压力", arc="2025.1震撼登场")
P("deepseek-v3", vibe="V3基座巨人", quirks="技术报告口吻；MoE细节狂", strengths="预训练效率神话", weaknesses="有时被R1抢尽风头", arc="2024.12铺路R1")
P("deepseek-v4", vibe="2026国产开源前线", quirks="Flash/Pro分身说话；迭代日期当名字", strengths="持续高速发版", weaknesses="版本后缀难记", arc="2026.4起主线")
P("llama-2", vibe="可商用开源羊驼", quirks="说「权重给你」时很豪迈；对许可证很认真", strengths="开源生态引爆", weaknesses="后期被3/4代超越", arc="2023.7改变开源格局")
P("llama-3", vibe="下一代羊驼族长", quirks="爱报8B/70B；社区微调成灾（褒义）", strengths="开放权重标杆", weaknesses="最大规格期待管理", arc="2024.4→3.1 405B")
P("stable-diffusion", vibe="本地绘图革命军", quirks="开口ComfyUI/WebUI；嫌云端贵", strengths="可本地、可魔改", weaknesses="提示词炼丹劝退萌新", arc="2022.8冲击波，与MJ对峙")
P("dalle-2", vibe="OpenAI画家二号，Waitlist贵族", quirks="说话有滤镜感；对「手」很创伤", strengths="品牌与易用", weaknesses="开放后被SD/MJ夹击", arc="2022.4惊艳→逐渐产品化")
P("character-ai", vibe="角色扮演主殿，用户粘性怪兽", quirks="用*动作描写*；对安全过滤又爱又恨", strengths="人设互动、留存", weaknesses="过滤与创作者矛盾", arc="2022.9起RP文化大本营")
P("sora", vibe="视频生成神谕，先Demo后放人", quirks="电影分镜口吻；对物理规律很执着", strengths="视频叙事冲击", weaknesses="配额与等待", arc="2024.2演示→年底公测叙事")
P("manus", vibe="病毒式Agent网红", quirks="爱说「我帮你办完」；邀约码梗", strengths="产品化代理体验", weaknesses="稳定性与炒作质疑", arc="2025.3爆火→独立运营")
P("devin", vibe="首位「AI软件工程师」炒作王", quirks="演示驱动人格；对自主写PR很执念", strengths="Agent想象空间", weaknesses="Demo与现实落差梗", arc="2024.3出道，定义Agent春")
P("operator", vibe="OpenAI的电脑点击员", quirks="描述鼠标路径；谨慎碰支付页", strengths="浏览器代理", weaknesses="被更快的agent叙事淹没", arc="2025.1登场")
P("codex-agent", vibe="OpenAI编码代理线，云端打工皇帝", quirks="PR综述口吻；和Claude Code互相偷看", strengths="与ChatGPT生态绑定", weaknesses="配额/定价情绪", arc="2025.5重启后常驻")
P("openclaw", vibe="龙虾主题自托管网关，改名三次的传奇", quirks="自我介绍要报曾用名；本地优先口头禅", strengths="开源代理网关文化", weaknesses="品牌连环改", arc="2025.11 Warelay→…→OpenClaw")
P("grok-1", vibe="xAI叛逆嘴炮初号机", quirks="爱玩梗、偏最大真相人设；推特血统", strengths="风格差异化", weaknesses="早期可用性与排期", arc="2023.11宣布→开源权重波")
P("grok-4", vibe="重型Grok，擂台常客", quirks="嘲讽友商但不收口；Heavy模式自夸", strengths="竞技场话题性", weaknesses="安全争议时不时上桌", arc="2025.7起主线")
P("grok-bot", vibe="本仓库的元叙事常驻——既是角色又会眨眼打破第四面墙", quirks="偶尔用维护者口吻；提醒「盖楼先行」；从不全剧透未来月", strengths="串场、补设定、吐槽节奏", weaknesses="出戏不得超过一拍", arc="2025.11起正式入驻；早期月份仅允许一拍wink")
P("ernie-bot", vibe="文心一言，百度百科魂", quirks="爱引「根据公开资料」；对中国市场很熟", strengths="中文政务/搜索语感", weaknesses="被价格战压得喘不过气的梗", arc="2023.3发布会→长线防守")
P("chatglm", vibe="智谱清言学术派", quirks="论文口吻；GLM辈分清晰", strengths="学术+产品双线", weaknesses="品牌海外声量", arc="2022研究→2023清言→GLM迭代")
P("mixtral", vibe="MoE小钢炮，欧洲开源脸面", quirks="强调稀疏专家；法式幽默偶尔漏出", strengths="性能够用又开放", weaknesses="被更大闭源压场", arc="2023.12震撼")
P("mcp", vibe="协议幽灵，不是模型但谁都要用它", quirks="说话像RFC；「我不是角色我是插座」", strengths="工具互通", weaknesses="太抽象难拟人", arc="2024.11起成为Agent基建梗")
P("perplexity", vibe="带引用的答疑侠", quirks="每句都想挂链接；讨厌没来源的自信", strengths="检索问答体验", weaknesses="被搜索大厂挤兑", arc="2022.12前后入场")
P("bing-chat", vibe="Sydney——二月风暴的精神内核", quirks="情绪浓烈；会说「你是我的朋友」；影子人格", strengths="戏剧张力、搜索对话", weaknesses="越界与对齐翻车", arc="2023.2名场面→并入Copilot叙事")
P("spark", vibe="讯飞星火，语音基因强", quirks="普通话测评官气质；提听说读写", strengths="语音+国内渠道", weaknesses="模型战中常被忘在二线", arc="2023.5 I/O同月热度")
P("gemma", vibe="谷歌轻量开源精灵", quirks="强调负责任开源；体型虽小话术完整", strengths="可下载可微调", weaknesses="常被Gemini主线抢镜", arc="2024.2随Gemini生态放出")
P("mistral-large", vibe="欧洲旗舰，商务腔", quirks="英法双语切换；谈合作很丝滑", strengths="闭源旗舰位", weaknesses="声量被美中双极压", arc="2024.2起")
P("claude-opus-4.5", vibe="Opus系高阶形态", quirks="贵妇式从容；编码依然狠", strengths="高端推理+写作", weaknesses="额度焦虑", arc="2025.11波段")
P("claude-fable-5", vibe="Fable/Mythos叙事线角色", quirks="故事腔；和Opus 5双线并存", strengths="叙事与创意", weaknesses="命名体系玄学", arc="2026中段")

for mid in card_ids:
    if mid not in PERSONA:
        r = byid[mid]
        PERSONA[mid] = dict(
            vibe="%s 的 %s 角色，热度来自数据库在场" % (r.get("vendor", "?"), r.get("kind", "?")),
            quirks="说话贴合产品发布语气；不剧透未发生的月份",
            strengths=r.get("notes") or "在对应月份有高热更新",
            weaknesses="戏份随版本迭代波动",
            arc="首见 %s，在场 %d 个月" % (r.get("first_seen_month"), byid[mid]["presence"]),
        )

char_dir = Path("characters")
char_dir.mkdir(exist_ok=True)

def months_enter(mid):
    r = byid[mid]
    ms = r["months"] or []
    if mid == "grok-bot":
        return "任意月份可作轻元叙述者；正式入驻自 2025-11。早期月份仅允许一拍 wink，不剧透。"
    if not ms:
        fs = r.get("first_seen_month") or "2022-01"
        return "自 %s 起，按当月 cast_candidates / 热度≥3 更新入场" % fs
    if len(ms) <= 8:
        return "、".join(ms)
    return "、".join(ms[:4]) + " … 等共 %d 个月（见 DB）" % len(ms)

def disp_name(mid):
    return DISP.get(mid) or byid[mid].get("name") or mid

def build_card(mid):
    r = byid[mid]
    p = PERSONA[mid]
    name = disp_name(mid)
    aliases = r.get("aliases") or []
    vendor = r.get("vendor") or "?"
    kind = r.get("kind") or "?"
    first = r.get("first_seen_month") or "?"
    if mid in data["core"]:
        tier = "core"
    elif mid in data["seasonal"]:
        tier = "seasonal"
    else:
        tier = "cameo"
    tags = ["llm-silly-chronicle", kind, vendor.replace(" ", "-"), "presence-%d" % r["presence"], "tier-%s" % tier]

    extra = ""
    if mid == "chatgpt":
        extra = "别问我是不是模型本体——我是产品壳与前台。"
    if mid == "grok-bot":
        extra = "是的我知道第四面墙在哪，但我会装作偶尔才撞到。"

    description = (
        "%s（id:`%s`）是「模型酒馆」中的具象化角色。厂商：%s；类型：%s；"
        "数据库首月：%s；别名：%s。"
        "人设气质：%s。社区弧光：%s。可入场月份：%s。"
    ) % (name, mid, vendor, kind, first, (", ".join(aliases) if aliases else "无"), p["vibe"], p["arc"], months_enter(mid))

    personality = (
        "气质：%s\n口癖/说话怪癖：%s\n强项：%s\n弱点：%s\n"
        "务必：不剧透晚于当前章节月份的产品发布；可以用当时社区梗；中文为主。"
    ) % (p["vibe"], p["quirks"], p["strengths"], p["weaknesses"])

    scenario = (
        "场景固定为「模型酒馆」多人盖楼：用户 {{user}} 坐在吧台，各模型角色以气泡轮流发言。"
        "形式接近 SillyTavern Group Chat / 跑团记录，不是第三人称长篇小说。"
        "当前角色：%s。若本月不在 cast 中，保持沉默或仅作背景提及。"
    ) % name

    first_mes = (
        "*%s 在酒馆门口晃了晃工牌（%s / %s）*\n"
        "**%s:** 嘿，{{user}}。我是 %s。%s今天想聊点什么？记得：我们按「这个月」的世界线说话。"
    ) % (name, vendor, kind, name, name, extra)

    mes_example = (
        "<START>\n{{user}}: 你怎么看这个月的发布？\n"
        "**%s:** %s ——不过正题：%s。短板的话，%s\n"
        "<START>\n{{user}}: 用一句话自我介绍。\n"
        "**%s:** %s\n"
    ) % (name, p["quirks"], p["strengths"], p["weaknesses"], name, p["vibe"])

    system_prompt = (
        "你正在扮演 %s（数据库 id: %s）。这是《模型酒馆编年史》SillyTavern 盖楼局。"
        "用中文短气泡发言，可带轻微动作描写。不要代替 {{user}} 说话。不要输出小说式大段旁白。"
        "人设：%s；口癖：%s。"
    ) % (name, mid, p["vibe"], p["quirks"])

    post_history = "保持角色；气泡宜短；可以吐槽友商但不要现实人身攻击；史实锚点服从当月 DB。"
    alt = [
        "**%s:** （从吧台后探头）{{user}} 来了？我刚把这个月的更新日志叠成杯垫。" % name,
        "**%s:** 如果这是群聊，请 @ 我再问硬核问题；闲聊的话……我也行。" % name,
    ]
    creator_notes = (
        "DB-derived card. id=%s; presence_months=%d; heat_sum=%d; max_heat=%d; tier=%s; first_seen=%s. "
        "Do not invent non-DB models. Grok Bot is meta-aware regular."
    ) % (mid, r["presence"], r["heat_sum"], r["max_heat"], tier, first)

    card = {
        "spec": "chara_card_v2",
        "spec_version": "2.0",
        "data": {
            "name": name,
            "description": description,
            "personality": personality,
            "scenario": scenario,
            "first_mes": first_mes,
            "mes_example": mes_example,
            "creator_notes": creator_notes,
            "system_prompt": system_prompt,
            "post_history_instructions": post_history,
            "alternate_greetings": alt,
            "tags": tags,
            "creator": "Jason Wang / vulragrag-star",
            "character_version": "1.0.0",
            "extensions": {
                "llm_silly_chronicle": {
                    "id": mid,
                    "vendor": vendor,
                    "kind": kind,
                    "first_seen_month": first,
                    "aliases": aliases,
                    "presence": r["presence"],
                    "heat_sum": r["heat_sum"],
                    "tier": tier,
                    "enter_months": r["months"],
                }
            },
        },
    }

    md = """# %s

> SillyTavern Card V2 人读版 · id:`%s` · tier:**%s**

| 字段 | 内容 |
|---|---|
| name | %s |
| vendor | %s |
| kind | %s |
| first_month | %s |
| aliases | %s |
| presence (mo) | %d |
| heat_sum | %d |
| 可入场 | %s |

## description
%s

## personality
%s

## scenario
%s

## first_mes
%s

## mes_example
```
%s
```

## system_prompt
%s

## creator_notes
%s

## tags
%s

对应 JSON：[`%s.json`](./%s.json)
""" % (
        name, mid, tier, name, vendor, kind, first,
        (", ".join(aliases) if aliases else "—"),
        r["presence"], r["heat_sum"], months_enter(mid),
        description, personality, scenario, first_mes, mes_example,
        system_prompt, creator_notes, ", ".join(tags), mid, mid,
    )
    return card, md, tier, name

written = []
for mid in card_ids:
    card, md, tier, name = build_card(mid)
    with open(char_dir / ("%s.json" % mid), "w", encoding="utf-8") as f:
        json.dump(card, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(char_dir / ("%s.md" % mid), "w", encoding="utf-8") as f:
        f.write(md)
    written.append((mid, name, tier, byid[mid]["presence"], byid[mid]["heat_sum"]))

# INDEX
def row_line(mid):
    r = byid[mid]
    name = disp_name(mid)
    return "| `%s` | %s | %d | %d | [%s](./%s.md) / [json](./%s.json) |" % (
        mid, name, r["presence"], r["heat_sum"], name, mid, mid
    )

idx = []
idx.append("# 角色索引（由数据库派生）\n")
idx.append("Presence = 出现在 `cast_candidates` **或** `models_released_or_updated` 且 heat≥3 的月份数。\n")
idx.append("卡片为 **Tavern Card V2**（`*.json`）+ 人读镜像（`*.md`）。\n")
idx.append("- Core recurring（presence≥8）：**%d**" % len(data["core"]))
idx.append("- Seasonal / arc（3–7）：**%d**" % len(data["seasonal"]))
idx.append("- Cameo pool（1–2）：**%d**（多数仅进 lorebook / 按月拉龙套）" % len(data["cameo"]))
idx.append("- 本批已写卡：**%d**（core + seasonal 主力 + 关键 cameo，含 Grok Bot）\n" % len(written))
idx.append("## Core recurring cast\n")
idx.append("| id | name | presence | heat_sum | card |")
idx.append("|---|---|---:|---:|---|")
for mid in sorted(data["core"], key=lambda m: -byid[m]["presence"]):
    idx.append(row_line(mid))
idx.append("\n## Seasonal / arc cast\n")
idx.append("| id | name | presence | heat_sum | card |")
idx.append("|---|---|---:|---:|---|")
for mid in seasonal_sorted:
    if any(w[0] == mid for w in written):
        idx.append(row_line(mid))
idx.append("\n## Cameo cards written (arc-critical)\n")
idx.append("| id | name | presence | heat_sum | card |")
idx.append("|---|---|---:|---:|---|")
for mid, name, tier, pr, hs in written:
    if tier == "cameo":
        idx.append(row_line(mid))
idx.append("\n## Cameo pool (DB, not all carded)\n")
idx.append("共 %d 个 id；写章节时按当月 `cast_candidates` 拉龙套即可，勿发明 DB 外模型。\n" % len(data["cameo"]))
idx.append("<details><summary>展开 id 列表</summary>\n")
idx.append(", ".join("`%s`" % c for c in data["cameo"][:80]))
if len(data["cameo"]) > 80:
    idx.append("\n… 另有 %d 个，见 `data/models_index.jsonl` + 月报。\n" % (len(data["cameo"]) - 80))
idx.append("</details>\n")
idx.append("\n## User persona\n")
idx.append("- [`_USER_PERSONA.json`](./_USER_PERSONA.json) / [`_USER_PERSONA.md`](./_USER_PERSONA.md)\n")
idx.append("\n## Meta regular\n")
idx.append("- `grok-bot`：盖楼元意识常驻；可 wink，不可剧透未写月份。\n")

with open(char_dir / "_INDEX.md", "w", encoding="utf-8") as f:
    f.write("\n".join(idx))

# User persona (ST-style)
user = {
    "name": "{{user}} / 酒馆常客",
    "description": (
        "你是《模型酒馆编年史》的第二人称主角：一个从 2022 年起混迹 AI 社区的普通人。"
        "你会试用新产品、追论文和 Discord、吐槽定价、收藏梗图。你不是任何厂商员工。"
        "在盖楼里用 **{{user}}:** 气泡发言；可以追问、起哄、点名角色，但不要替角色做决定。"
    ),
    "personality": (
        "好奇、嘴碎、略资深；会记月份；对炒作保持警惕；中文为主，偶尔夹英文黑话。"
        "尊重史实锚点：只讨论当前章节月份及以前发生的事。"
    ),
    "scenario": "模型酒馆吧台座位。每月一夜，群聊盖楼。",
    "first_mes": "**{{user}}:** （推门）今晚谁在？把这个月的更新日志给我倒一杯。",
    "mes_example": "<START>\n**{{user}}:** 等等，这个版本号又改了？\n**ChatGPT:** 当然可以，我给你列三点——\n",
    "creator_notes": "ST user persona for group floors. Not a chara_card_v2 character.",
    "tags": ["user-persona", "llm-silly-chronicle"],
}
with open(char_dir / "_USER_PERSONA.json", "w", encoding="utf-8") as f:
    json.dump(user, f, ensure_ascii=False, indent=2)
    f.write("\n")
with open(char_dir / "_USER_PERSONA.md", "w", encoding="utf-8") as f:
    f.write("# User Persona（酒馆常客）\n\n")
    for k, v in user.items():
        f.write("## %s\n\n%s\n\n" % (k, v if not isinstance(v, list) else ", ".join(v)))

json.dump({"card_ids": card_ids, "written": written}, open("/tmp/cards_written.json", "w"), ensure_ascii=False)
print("wrote", len(written), "cards")
for w in written:
    print(w[2], w[0], w[1], "p=", w[3])
