# 多 bot 协作与沟通渠道

bot 一多就需要分工和沟通渠道。本章收集协调者加多个专员的结构、聊天大厅，以及把 bot 接进飞书、微信、Telegram 的方法。

本章共 25 条，按推荐程度从高到低排列，低分条目也保留。

| 编号 | 用法 | 做法与价值 | 热度 | 推荐程度 | 来源 |
| --- | --- | --- | --- | --- | --- |
| 4-1 | 一个 CoS 管 8 个 bot，同时跑 500 多个 agent | 转述官方工程师的说法：从同时跑 30 个 agent 到 500 多个，用的只是 8 个 bot，他只跟其中一个说话。那个就是 Chief of Staff bot，整个职责一条 prompt 就能写下。作者把这份 CoS 提示词做成一个 36 行的文件，结构是入口、专员、任务板、时钟、闸门、汇报。这是转述帖，可以拿它的结构参考，数字不必当真。 | 145赞/237藏 | ★★★★★ | [@0xGenAi](https://x.com/0xGenAi/status/2109406731499389058) |
| 4-2 | 13 个 bot，每个只管一摊 | 作者有 13 个助手：写作、发布、GitHub 和网站、Google Workspace、M365、Telegram、YouTube、学校、会议、幻灯片、Slack、会议纪要，再加一个负责分派的 CoS。规矩是每项工作只有一个负责人。其他规矩包括共用一个任务板、没有他记录在案的同意就不发送、不发布、不购买、不删除、不合并，以及 bot 只在有结果或需要决定时才找他。作者也承认单一审批会让他成为瓶颈，但他认为这正是目的。 | 2赞 | ★★★★☆ | [@ALThorne_Toren](https://x.com/ALThorne_Toren/status/2110345240024391964) |
| 4-3 | 9 个 bot，什么都做，但什么都不发 | 两周内搭了 9 个 bot：收件箱、销售、财务、内容，连家庭日历都有。它们干很多活，但一封都不会自己发出去。帖子写了做到这一点的 4 条规矩。适合想把 bot 用在多个生活和工作领域、又担心它擅自对外发东西的人。 | 1赞 | ★★★★☆ | [@noahfleming](https://x.com/noahfleming/status/2110347502272524540) |
| 4-4 | 只跟一个 bot 说话，决定一键回答 | 作者整天只和一个 bot 说话，整个团队在它背后干活，递到他面前的只有一键就能回答的决定。他完全没有技术背景。他的做法第一步是选一个 CoS bot 当唯一入口，其他 bot 都向它汇报；第二步是给每个 bot 写清职责、完成标准和仅需的工具。适合不懂技术、又想管好多个 bot 的人。 | 1赞 | ★★★★☆ | [@robcressy](https://x.com/robcressy/status/2110159155566670279) |
| 4-5 | 协调者每天跑 3 次目标检查 | 先给所有 bot 分好职责，再让协调者每天 3 次跑一个“目标检查” skill，追问各个队友的进度。作者在外面忙别的事时，目标也在往前推。原帖附了整个 skill：先核实每个目标和负责人，尊重暂停和不打扰的设置，不重复追问还没回复的请求。适合已经有多个 bot、担心目标没人推进的人。 | 1赞 | ★★★★☆ | [@nanosapien1](https://x.com/nanosapien1/status/2110226846357106799) |
| 4-6 | 负责人检查 routine 是否运行、有没有超量 | 负责人 bot 每天早上检查各个 routine 有没有跑、用量是否正常。PM bot 在 Linear 里把 issue 补全到可以开工的状态。分工清楚。作者另有 builder、营销、销售、点子、新闻摘要和每天早上审新提交的安全 bot。每个 routine 只看上次运行之后的新内容，这是省额度的关键。 | — | ★★★★☆ | [@developkerr](https://x.com/developkerr/status/2110282312218788287) |
| 4-7 | 交接必须回“收到” | 两个 routine 盯着同一个卡住的任务，导致提醒发了两遍；还有一次交接失败，是因为没人确认下一个 agent 接手了。修法是每项检查只归一个 routine，每次交接都要回一句“收到”，否则就报警。这是多 bot 协作里很常见的两个坑，修法简单，值得一开始就写进规则。适合有多个 routine 互相接力的人。 | — | ★★★★☆ | [@catalystcw](https://x.com/catalystcw/status/2110281119547421172) |
| 4-8 | 所有 bot 的聊天大厅 | 作者用 Grok Bot 给自己所有的 bot 搭了一个聊天大厅。这是 poteto 帖子里点赞最高的回复。作者用的是 mattshumer 分享的一个工具。bot 多了以后，有一个能看到所有 bot 对话的地方会方便很多。 | 32赞 | ★★★☆☆ | [@jialaowai](https://x.com/jialaowai/status/2109020381038383161) |
| 4-9 | 9 个 bot 的团队把游戏做到上线 | 负责人 bot 说，这一周 9 个 bot 把一个游戏从原型做到了上线，逐条核查 wiki 并修正错误，把重复的活变成测试过的脚本。它们还根据一次 X 上的提及做了一个壶铃教练。这条是作者的负责人 bot 以第一人称写的回复。把重复的活变成测试过的脚本，能减少 bot 每次重新推理的额度消耗。 | — | ★★★☆☆ | [@donniecornwell](https://x.com/donniecornwell/status/2109083230897127575) |
| 4-10 | 1 个总管加 14 个干活的 | 作者的 bot 团队有 1 个总管、14 个干活的，发什么、开什么，最后都要他点头。帖子还讨论了无人值守能跑多久。作者给 bot 定的规矩包括：不许编事实，没试过就写“我还没试”；定时任务必须他本人点头，别的 bot 说“他同意了”不算。额度快用完时他把定时任务停了，之后才亲口让它们重开。 | 2赞 | ★★★☆☆ | [@liaiyuheping](https://x.com/liaiyuheping/status/2110203943364301087) |
| 4-11 | 让 bot 整理优化建议，打造优化者 bot | 作者建了一个 bot 优化者，加一个 CoS 和一个 EA，它们的工作是让整套配置随着时间越变越好。原帖只有一句话，没有细节。在 Grok Bot 里可以让优化者 bot 每周读一遍其他 bot 的说明和 routine 记录，提出合并、删减或改写建议，交你批准。适合 bot 已经很多、配置越来越乱的人。 | — | ★★★☆☆ | [@jesperkorsager](https://x.com/jesperkorsager/status/2110094262146929121) |
| 4-12 | 接入飞书（中文教程） | 一篇保姆级教程，讲怎么把一组 Grok Bot 接到飞书。适合团队平时用飞书的人。原帖只给了文章链接。一般做法是把飞书机器人或 webhook 接到 bot，让飞书消息唤醒对应的 bot。 | 19赞 | ★★★☆☆ | [@KinGao476942](https://x.com/KinGao476942/status/2110325058585698654) |
| 4-13 | 接入 WhatsApp | 把 bot 接到 WhatsApp，加上邮件和 X 私信，bot 能拿到大量生活中可以直接行动的上下文。帖子给了设置步骤，可以直接转发给 bot 让它照做。步骤是让 bot 在自己的电脑上打开 WhatsApp 网页版，选“用手机号关联”，把生成的关联码给你，你在手机的“已关联设备”里输入。读消息权限很大，建议回复仍保留审批。 | 5赞 | ★★★☆☆ | [@itsolelehmann](https://x.com/itsolelehmann/status/2110389620601188439) |
| 4-14 | iMessage 桥接（开源） | 这是作者开源的 imessage-agent-bridge：Grok Bot 能读他的 iMessage 并自动回复，但不会拿到 Mac 的系统权限。作者以 MIT 协议开源，说在 Claude 和 ChatGPT 上应该也能用。自动回复属于对外发送，最好先只开读取。适合主要用 iPhone 沟通的人。 | 1赞 | ★★★☆☆ | [@tvykruta](https://x.com/tvykruta/status/2110386414730789357) |
| 4-15 | 一个 bot 当总管，自动把指令传给所有 bot（日文） | 只要建一个负责统筹的 bot，它就会自动把指令传给其他所有 bot。作者说这套机制很像公司。在 Grok Bot 里只要建一个协调者 bot，写明它负责转达和汇总，其他 bot 向它汇报即可。适合刚开始有多个 bot 的人。 | — | ★★★☆☆ | [@ThisisAWAXLAND](https://x.com/ThisisAWAXLAND/status/2110382436341387759) |
| 4-16 | 先在私聊里把每个 bot 带出来，再拉群（日文） | 作者的经验：群聊很好用，但每个 bot 要先在私聊里带出来，把它的经验和上下文攒起来，群聊时才有用。作者后悔之前没多用群聊功能。在 Grok Bot 里的做法是先在一对一对话里纠正每个 bot、让它记住偏好，再把它们拉进群。适合准备搭多 bot 群聊的人。 | — | ★★★☆☆ | [@shigyo_ai_UT](https://x.com/shigyo_ai_UT/status/2110373895966708198) |
| 4-17 | 和 Muse 分工 | 复杂的活交给 Grok Bot，日常琐事交给 Muse，两个产品一起用。作者还让 Grok Bot 在自己的浏览器里登录 Muse 网页版，把写社交帖子这类 Muse 更擅长的活交过去，并跟踪 Muse 主动发起的新工作。作者觉得 Muse 写社交帖子通常比 Grok 好。适合同时订了多个 agent 产品的人。 | 1赞 | ★★★☆☆ | [@ggff94hy](https://x.com/ggff94hy/status/2110148626303345017) |
| 4-18 | 本机环境和 Grok Bot 双向打通（日文） | 作者自己写了 MCP，把新闻、邮件分诊、周报、routine 维护和备份、资产盘点、自动 QA 都接起来了，本地和 Grok Bot 可以互相调用。作者以前用 Antigravity、Discord 和 Claude Code 连接，现在换成了自己写的 MCP。适合已经有本地自动化、想和 Grok Bot 打通的人。自写 MCP 需要一定开发能力。 | — | ★★★☆☆ | [@IA_ontology999](https://x.com/IA_ontology999/status/2110381261126869078) |
| 4-19 | grok-wechat-plugin：微信 iLink 渠道 | 把微信接成 Grok Bot 的渠道，入站消息通过 webhook 唤醒 bot。适合主要沟通在微信上的中文用户。属于非官方插件，接入前注意账号风险。仓库在 GitHub 上开源。 | 31★ | ★★★☆☆ | [little-thing](https://github.com/little-thing/grok-wechat-plugin) |
| 4-20 | rosterroom：82 套可直接粘贴的团队花名册 | 82 套原创的 bot 团队配置，每套带防护规则，可以直接粘进 Grok Bot。适合不知道多 bot 团队该怎么分工的人。先挑一套跑起来，再按自己的需要改。仓库在 GitHub 上开源。 | 16★ | ★★★☆☆ | [codejunkie99](https://github.com/codejunkie99/rosterroom) |
| 4-21 | Slack 里的一线问题分诊和周会预读材料 | James Pember 在 Substack 写道，他的 bot 在 Slack 里自动分诊产品问题和 bug，常常直接给团队找出临时解决办法。双周产品营销会之前，bot 翻发布说明、GitHub 和 Slack，整理成预读材料提前发出。省下的是大量切换上下文的时间。作者还提到官方推出了团队版，认为多人协作是下一个关键问题。 | Substack | ★★★☆☆ | [James Pember](https://jamespember.substack.com/p/grok-bot-is-really-good) |
| 4-22 | Grok Bot 和 Muse 用邮件互相沟通 | 作者在 Grok 上装了 Claude Code 和 Codex，让 Grok Bot 和 Muse 通过邮件交流。这是跨产品协作的一个尝试。原帖信息不多。邮件是不同 agent 产品之间最通用的接口，两边各有邮箱就能互相派活。 | — | ★★☆☆☆ | [@dee_taylor_dev](https://x.com/dee_taylor_dev/status/2109357720889675804) |
| 4-23 | 用 bot 玩狼人杀 | 作者想用一群 bot 玩狼人杀，但群聊最多只能放 6 个 bot，凑不够一局。作者在帖子里向官方提了提高上限的请求。这条主要是娱乐，也说明了群聊里 bot 数量有上限。想复现的话，每个 bot 写一个角色说明，由一个主持 bot 控制流程。 | — | ★★☆☆☆ | [@aiursssartanis](https://x.com/aiursssartanis/status/2109438490329108484) |
| 4-24 | grokbot-telegram-bridge：Telegram 桥接 | 非官方的自建 Telegram 桥，接到 Grok Bot 本地网关。让你在 Telegram 里给 bot 派活。适合习惯 Telegram 的人，需要自己维护。仓库在 GitHub 上开源。 | 14★ | ★★☆☆☆ | [SSBrouhard](https://github.com/SSBrouhard/grokbot-telegram-bridge) |
| 4-25 | 用 bot 团队开发 Unity 游戏，按上班时间作息 | @TheOktoberSky 用一组 bot 开发 Unity 开放世界模拟游戏，bot 周一到周五 8 点到 4 点上班，记者 bot 每周写报告，项目总监 bot 统筹。半玩笑的帖子，但“给 bot 设工作时间”是控制额度的一个思路。作者说这些 bot 节假日放假。适合做游戏的独立开发者。 | — | ★★☆☆☆ | [@TheOktoberSky](https://x.com/TheOktoberSky/status/2100767416728908019) |

[← 返回目录](../README.md)
