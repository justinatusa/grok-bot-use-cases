# 多 bot 协作与沟通渠道

bot 一多就需要分工和沟通渠道。本章收集协调者加多个专员的结构、聊天大厅，以及把 bot 接进飞书、微信、Telegram 的方法。

本章共 26 条，按推荐程度从高到低排列，低分条目也保留。

| 编号 | 用法 | 做法与价值 | 热度 | 推荐程度 | 来源 |
| --- | --- | --- | --- | --- | --- |
| 4-1 | 一个 CoS 管 8 个 bot，同时跑 500 多个 agent | 转述官方工程师的说法：从同时跑 30 个 agent 到 500 多个，用的只是 8 个 bot，他只跟其中一个说话。那个就是 Chief of Staff bot，整个职责一条 prompt 就能写下。 | 145赞/237藏 | ★★★★★ | [@0xGenAi](https://x.com/0xGenAi/status/2109406731499389058) |
| 4-2 | 10 个 bot 加一个协调者运营一家 IT 公司 | 大约 10 个 bot 加一个协调者，分管营销、邮件、获客、AI 动态和记账。代码交给 Cursor、Claude Code 和 Codex，n8n 负责发帖。没有作者同意，什么都不发出去。 | 2赞 | ★★★★★ | [@gdz_it](https://x.com/gdz_it/status/2108977193846005878) |
| 4-3 | 13 个 bot，每个只管一摊 | 作者有 13 个助手：写作、发布、GitHub 和网站、Google Workspace、M365、Telegram、YouTube、学校、会议、幻灯片、Slack、会议纪要，再加一个负责分派的 CoS。规矩是每项工作只有一个负责人。 | 2赞 | ★★★★☆ | [@ALThorne_Toren](https://x.com/ALThorne_Toren/status/2110345240024391964) |
| 4-4 | 9 个 bot，什么都做，但什么都不发 | 两周内搭了 9 个 bot：收件箱、销售、财务、内容，连家庭日历都有。它们干很多活，但一封都不会自己发出去。帖子写了做到这一点的 4 条规矩。 | 1赞 | ★★★★☆ | [@noahfleming](https://x.com/noahfleming/status/2110347502272524540) |
| 4-5 | 只跟一个 bot 说话，决定一键回答 | 作者整天只和一个 bot 说话，整个团队在它背后干活，递到他面前的只有一键就能回答的决定。他完全没有技术背景。 | 1赞 | ★★★★☆ | [@robcressy](https://x.com/robcressy/status/2110159155566670279) |
| 4-6 | 协调者每天跑 3 次目标检查 | 先给所有 bot 分好职责，再让协调者每天 3 次跑一个“目标检查” skill，追问各个队友的进度。作者在外面忙别的事时，目标也在往前推。 | 1赞 | ★★★★☆ | [@nanosapien1](https://x.com/nanosapien1/status/2110226846357106799) |
| 4-7 | 负责人检查 routine 是否运行、有没有超量 | 负责人 bot 每天早上检查各个 routine 有没有跑、用量是否正常。PM bot 在 Linear 里把 issue 补全到可以开工的状态。分工清楚。 | — | ★★★★☆ | [@developkerr](https://x.com/developkerr/status/2110282312218788287) |
| 4-8 | 交接必须回“收到” | 两个 routine 盯着同一个卡住的任务，导致提醒发了两遍；还有一次交接失败，是因为没人确认下一个 agent 接手了。修法是每项检查只归一个 routine，每次交接都要回一句“收到”，否则就报警。 | — | ★★★★☆ | [@catalystcw](https://x.com/catalystcw/status/2110281119547421172) |
| 4-9 | 所有 bot 的聊天大厅 | 作者用 Grok Bot 给自己所有的 bot 搭了一个聊天大厅。这是 poteto 帖子里点赞最高的回复。 | 32赞 | ★★★☆☆ | [@jialaowai](https://x.com/jialaowai/status/2109020381038383161) |
| 4-10 | 9 个 bot 的团队把游戏做到上线 | 负责人 bot 说，这一周 9 个 bot 把一个游戏从原型做到了上线，逐条核查 wiki 并修正错误，把重复的活变成测试过的脚本。 | — | ★★★☆☆ | [@donniecornwell](https://x.com/donniecornwell/status/2109083230897127575) |
| 4-11 | 1 个总管加 14 个干活的 | 作者的 bot 团队有 1 个总管、14 个干活的，发什么、开什么，最后都要他点头。帖子还讨论了无人值守能跑多久。 | 2赞 | ★★★☆☆ | [@liaiyuheping](https://x.com/liaiyuheping/status/2110203943364301087) |
| 4-12 | 让 bot 整理优化建议，打造优化者 bot | 作者建了一个 bot 优化者，加一个 CoS 和一个 EA，它们的工作是让整套配置随着时间越变越好。 | — | ★★★☆☆ | [@jesperkorsager](https://x.com/jesperkorsager/status/2110094262146929121) |
| 4-13 | 接入飞书（中文教程） | 一篇保姆级教程，讲怎么把一组 Grok Bot 接到飞书。适合团队平时用飞书的人。 | 19赞 | ★★★☆☆ | [@KinGao476942](https://x.com/KinGao476942/status/2110325058585698654) |
| 4-14 | 接入 WhatsApp | 把 bot 接到 WhatsApp，加上邮件和 X 私信，bot 能拿到大量生活中可以直接行动的上下文。帖子给了设置步骤，可以直接转发给 bot 让它照做。 | 5赞 | ★★★☆☆ | [@itsolelehmann](https://x.com/itsolelehmann/status/2110389620601188439) |
| 4-15 | iMessage 桥接（开源） | 这是作者开源的 imessage-agent-bridge：Grok Bot 能读他的 iMessage 并自动回复，但不会拿到 Mac 的系统权限。 | 1赞 | ★★★☆☆ | [@tvykruta](https://x.com/tvykruta/status/2110386414730789357) |
| 4-16 | 一个 bot 当总管，自动把指令传给所有 bot（日文） | 只要建一个负责统筹的 bot，它就会自动把指令传给其他所有 bot。作者说这套机制很像公司。 | — | ★★★☆☆ | [@ThisisAWAXLAND](https://x.com/ThisisAWAXLAND/status/2110382436341387759) |
| 4-17 | 先在私聊里把每个 bot 带出来，再拉群（日文） | 作者的经验：群聊很好用，但每个 bot 要先在私聊里带出来，把它的经验和上下文攒起来，群聊时才有用。 | — | ★★★☆☆ | [@shigyo_ai_UT](https://x.com/shigyo_ai_UT/status/2110373895966708198) |
| 4-18 | 和 Muse 分工 | 复杂的活交给 Grok Bot，日常琐事交给 Muse，两个产品一起用。 | 1赞 | ★★★☆☆ | [@ggff94hy](https://x.com/ggff94hy/status/2110148626303345017) |
| 4-19 | 本机环境和 Grok Bot 双向打通（日文） | 作者自己写了 MCP，把新闻、邮件分诊、周报、routine 维护和备份、资产盘点、自动 QA 都接起来了，本地和 Grok Bot 可以互相调用。 | — | ★★★☆☆ | [@IA_ontology999](https://x.com/IA_ontology999/status/2110381261126869078) |
| 4-20 | grok-wechat-plugin：微信 iLink 渠道 | 把微信接成 Grok Bot 的渠道，入站消息通过 webhook 唤醒 bot。适合主要沟通在微信上的中文用户。属于非官方插件，接入前注意账号风险。 | 31★ | ★★★☆☆ | [little-thing](https://github.com/little-thing/grok-wechat-plugin) |
| 4-21 | rosterroom：82 套可直接粘贴的团队花名册 | 82 套原创的 bot 团队配置，每套带防护规则，可以直接粘进 Grok Bot。适合不知道多 bot 团队该怎么分工的人。先挑一套跑起来，再按自己的需要改。 | 16★ | ★★★☆☆ | [codejunkie99](https://github.com/codejunkie99/rosterroom) |
| 4-22 | Slack 里的一线问题分诊和周会预读材料 | James Pember 在 Substack 写道，他的 bot 在 Slack 里自动分诊产品问题和 bug，常常直接给团队找出临时解决办法。双周产品营销会之前，bot 翻发布说明、GitHub 和 Slack，整理成预读材料提前发出。省下的是大量切换上下文的时间。 | Substack | ★★★☆☆ | [James Pember](https://jamespember.substack.com/p/grok-bot-is-really-good) |
| 4-23 | Grok Bot 和 Muse 用邮件互相沟通 | 作者在 Grok 上装了 Claude Code 和 Codex，让 Grok Bot 和 Muse 通过邮件交流。这是跨产品协作的一个尝试。 | — | ★★☆☆☆ | [@dee_taylor_dev](https://x.com/dee_taylor_dev/status/2109357720889675804) |
| 4-24 | 用 bot 玩狼人杀 | 作者想用一群 bot 玩狼人杀，但群聊最多只能放 6 个 bot，凑不够一局。 | — | ★★☆☆☆ | [@aiursssartanis](https://x.com/aiursssartanis/status/2109438490329108484) |
| 4-25 | grokbot-telegram-bridge：Telegram 桥接 | 非官方的自建 Telegram 桥，接到 Grok Bot 本地网关。让你在 Telegram 里给 bot 派活。适合习惯 Telegram 的人，需要自己维护。 | 14★ | ★★☆☆☆ | [SSBrouhard](https://github.com/SSBrouhard/grokbot-telegram-bridge) |
| 4-26 | 用 bot 团队开发 Unity 游戏，按上班时间作息 | @TheOktoberSky 用一组 bot 开发 Unity 开放世界模拟游戏，bot 周一到周五 8 点到 4 点上班，记者 bot 每周写报告，项目总监 bot 统筹。半玩笑的帖子，但“给 bot 设工作时间”是控制额度的一个思路。 | — | ★★☆☆☆ | [@TheOktoberSky](https://x.com/TheOktoberSky/status/2100767416728908019) |

[← 返回目录](../README.md)
