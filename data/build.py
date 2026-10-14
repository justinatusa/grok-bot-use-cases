import collections, re, html
exec(open('data/x_entries.py').read()); exec(open('data/more_entries.py').read())
ALL = [e for e in E+M]
CATS = [("mail","邮件和收件箱","01-mail"),("radar","调研和信息雷达","02-radar"),("code","编程和 PR 看护","03-code"),
("team","多 bot 协作与沟通渠道","04-team"),("ops","省额度、routine 和安全","05-ops"),("buy","购物、出行和办事","06-buy"),
("life","生活、家庭和健康","07-life"),("content","内容创作和营销","08-content"),("biz","生意和运营","09-biz"),
("trade","交易和投资（谨慎）","10-trade"),("meta","模板、目录和教程","11-meta")]
INTRO = {
"mail":"邮件是最常见的切入点：bot 有自己的邮箱，能被转发触发，又天然适合“只起草、不发送”。本章收集了从单一邮箱分诊到全家共用邮件服务台的做法。",
"radar":"让 bot 定期扫信息源、只在有变化时提醒你，是第二大类用法。本章收集收藏夹回顾、新闻和竞品监控、论文拆解等做法，重点看它们怎么控制噪音。",
"code":"开发者把 bot 放在 IDE 之外的“外循环”：接 bug、开 PR、追 CI、做 review。本章收集从报错到修复 PR 的闭环和对抗式审查的做法。",
"team":"bot 一多就需要分工和沟通渠道。本章收集协调者加多个专员的结构、聊天大厅，以及把 bot 接进飞书、微信、Telegram 的方法。",
"ops":"routine 跑得越频繁越费额度，无人值守又容易漏跑或越权。本章收集省额度、体检、可靠性和安全方面的经验，是规模化之前必读的一章。",
"buy":"打电话、比价、订位、追医院确认，这些琐事最适合交给有电脑和电话能力的 bot，付款和最终确认留给自己。",
"life":"家庭和个人生活里的用法：健康数据、孩子学校、财务、家务设备。很多都是“一个具体痛点加一条 routine”。",
"content":"内容生产和营销：剪辑、写作、SEO、设计评审。官方市场里营销类模板尤其多。",
"biz":"小生意和销售团队的用法：客户跟进、记账、招租、外呼。官方市场里销售类模板集中在这里。",
"trade":"交易类帖子热度高，但夸大收益很多。本章全部条目推荐度偏低，并标注谨慎；只建议学习角色分工和模拟盘复盘，不建议交出真钱。",
"meta":"找模板、读教程、搭第一个 bot 的入口。先读官方文档和安全清单，再去模板目录里挑低权限的模板改。",
}
def star(n): return "★"*n+"☆"*(5-n)
def src(h,u):
    if u.startswith("https://x.com") or u.startswith("https://x.ai"): return f"[@{h}]({u})"
    if "github.com" in u: return f"[{h}]({u})"
    return f"[{h}]({u})"
def cell(s): return s.replace("|","\\|")
counts = {}
for k,name,fn in CATS:
    es = sorted([e for e in ALL if e[0]==k], key=lambda e:-e[1])
    counts[k]=len(es)
    L=[f"# {name}\n",INTRO[k]+"\n",f"本章共 {len(es)} 条，按推荐程度从高到低排列，低分条目也保留。\n",
       "| 编号 | 用法 | 做法与价值 | 热度 | 推荐程度 | 来源 |","| --- | --- | --- | --- | --- | --- |"]
    num = fn[:2].lstrip("0")
    for i,e in enumerate(es,1):
        L.append(f"| {num}-{i} | {cell(e[2])} | {cell(e[3])} | {cell(e[4])} | {star(e[1])} | {src(e[5],e[6])} |")
    L.append("\n[← 返回目录](../README.md)\n")
    open(f"chapters/{fn}.md","w").write("\n".join(L))
# 先扫版
L=["# 先扫版：4 星和 5 星\n","只想先看最值得试的，从这里开始。条目和分类章节里的一样，这里按推荐程度和分类排列，每条附一段说明。\n"]
idx={}
for k,name,fn in CATS:
    es=sorted([e for e in ALL if e[0]==k], key=lambda e:-e[1])
    for i,e in enumerate(es,1): idx[id(e)]=(fn[:2].lstrip("0"),i,name)
top=sorted([e for e in ALL if e[1]>=4], key=lambda e:(-e[1],[c[0] for c in CATS].index(e[0])))
for e in top:
    n,i,name=idx[id(e)]
    L.append(f"- **{n}-{i} · {star(e[1])} · {name}** [{e[2]}]({e[6]})（{e[5]}，{e[4]}）\n  {e[3]}\n")
L.append("[← 返回目录](../README.md)\n")
open("chapters/12-top-picks.md","w").write("\n".join(L))
json_counts = counts
stars=collections.Counter(e[1] for e in ALL)
open("data/stats.txt","w").write(repr((counts,dict(stars),len(ALL),len(top))))
# 总览图
mx=max(counts.values())
bars="".join(f'<div class="r"><span class="l">{n}</span><div class="b" style="width:{counts[k]/mx*430:.0f}px"></div><span class="v">{counts[k]}</span></div>' for k,n,f in CATS)
sbars="".join(f'<div class="s"><div class="sb" style="height:{stars[s]/max(stars.values())*150:.0f}px"></div><div>{star(s)}</div><div>{stars[s]} 条</div></div>' for s in [5,4,3,2,1])
open("figures/overview.html","w").write(f'''<html><head><meta charset="utf-8"><style>
body{{font-family:"Noto Sans CJK SC";margin:0;padding:36px;width:1120px;overflow:hidden;background:#fafaf7;color:#222}}
h1{{font-size:30px;margin:0 0 6px}} .sub{{color:#666;margin-bottom:24px}}
.wrap{{display:flex;gap:40px}} .r{{display:flex;align-items:center;margin:9px 0}} .l{{width:220px;font-size:17px}}
.b{{height:22px;background:#3b6fd8;border-radius:4px}} .v{{margin-left:10px;font-weight:bold}}
.stars{{display:flex;align-items:flex-end;gap:14px;height:240px;margin-top:20px}} .s{{text-align:center;font-size:13px}} .sb{{width:52px;background:#e0903b;margin:0 auto 6px;border-radius:4px}}
h3{{margin:0 0 8px}}</style></head><body><h1>大家用 Grok Bot 做什么</h1>
<div class="sub">共 {len(ALL)} 条用法 · 11 类 · 来源：X 征集帖回复、官方市场、GitHub、Reddit 与博客</div>
<div class="wrap"><div><h3>各类条数</h3>{bars}</div><div><h3>推荐程度分布</h3><div class="stars">{sbars}</div></div></div></body></html>''')
print(counts, dict(stars), len(ALL), len(top))
