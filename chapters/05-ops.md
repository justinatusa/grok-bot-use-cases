# 省额度、routine 和安全

routine 跑得越频繁越费额度，无人值守又容易漏跑或越权。本章收集省额度、体检、可靠性和安全方面的经验，是规模化之前必读的一章。

本章共 24 条，按推荐程度从高到低排列，低分条目也保留。

| 编号 | 用法 | 做法与价值 | 热度 | 推荐程度 | 来源 |
| --- | --- | --- | --- | --- | --- |
| 5-1 | 每 5 分钟跑一次比每小时贵 12 倍 | 一篇长文讲 routine 的频率和成本：每 5 分钟跑一次，花费是每小时跑一次的 12 倍。教你按需求定频率。 | 255赞/469藏 | ★★★★★ | [@gippp69](https://x.com/gippp69/status/2109235458383216811) |
| 5-2 | 先轻量检查，有变化才跑完整任务 | 整晚的 96 次运行里，94 次什么都没发现。办法是存一个 /night-filter skill：一个 bot 每 5 分钟只看有没有变化，没变化就不跑完整任务。 | 38赞 | ★★★★★ | [@gippp69](https://x.com/gippp69/status/2110321307359322494) |
| 5-3 | 一晚 288 次空跑，烧掉 412 美元 | 作者的 bot 团队每 4 分钟检查一次已经不动的行情，每次都唤醒全员，一晚上跑了 288 次，花掉 412 美元。这是一个反面教材。 | 27赞 | ★★★★☆ | [@bl888m_eth](https://x.com/bl888m_eth/status/2110357844071497850) |
| 5-4 | 抓出浪费 99% 运行的 agent | 7 个 agent 分别管 X、邮件、CI、部署、文档和审计，其中一个每次醒来都只报 NO_CHANGE。修法和换更强的模型无关，而是改触发方式。 | 23赞 | ★★★★☆ | [@Nyxera0x](https://x.com/Nyxera0x/status/2110312522498658652) |
| 5-5 | 让 bot 自己砍掉 40% 用量 | 直接问 bot：“怎么在不降质量的前提下把用量砍掉 40%？”它会把 routine 改成事件触发、去掉重复读取、没事就静默。 | — | ★★★★☆ | [@c_olsson](https://x.com/c_olsson/status/2110323881563111543) |
| 5-6 | 先手动做一次，再存成 skill，最后排进日程 | 很多自动化坏掉，是因为还没手动跑通就先排了日程。官方推荐的顺序是：先在聊天里做对一次，存成 skill，再设成 routine。 | — | ★★★★☆ | [@Cyb3rCricket](https://x.com/Cyb3rCricket/status/2110121951175852534) |
| 5-7 | 用一条提示词体检自己的 bot | 作者用一条提示词让 Grok Bot 检查她的几个 bot，结果让她很满意。这种自查值得定期做。 | 619赞/236藏 | ★★★★☆ | [@KatieMiller](https://x.com/KatieMiller/status/2110156792651026619) |
| 5-8 | 把一台 Linux 机器整个交给 bot 维护 | Reddit 用户不熟 Linux，就告诉 bot 这台机器归它管。bot 做完交代的项目后，自己排了更新和巡检计划，每天早上发一份机器状态报告。适合有家用服务器但不想维护的人。 | Reddit | ★★★★☆ | [r/grok](https://www.reddit.com/r/grok/comments/1w8w0gg/grok_bot_is_awesome/) |
| 5-9 | routine 漏跑的应对：重要的事别放无人值守 | Reddit 上多人反映夜间 routine 有时不跑，问它才说“没跑，要现在跑吗”。有经验的人建议，夜里只放低风险、第二天容易检查的活，比如提纲、缺口清单。也有人让 bot 自己诊断并重写 routine 后恢复正常。X 上 @PerssonAC 也反映过 routine 不可靠或严重延迟。 | Reddit | ★★★★☆ | [r/GrokBot](https://www.reddit.com/r/GrokBot/comments/1w2g9xt/anyone_having_problems_with_grok_bots_remembering/) |
| 5-10 | 九个值得先装的 routine（含审批规则） | The Aigentic 根据几位博主的演示整理了九个 routine：早 7:30 收件箱分诊、每日细分领域调研、每周 X 侦察、周一机票价格监控、每周清理订阅和 Drive、多邮箱巡检、营收调研循环、晚间会议准备等。每个都附时间表、起手提示词和审批规则。文章强调先手动跑一次并纠正，再排进日程。 | 博客 | ★★★★☆ | [The Aigentic](https://www.theaigentic.com/hands-on/nine-grok-bot-routines) |
| 5-11 | 官方安全清单：只连需要的工具，对外动作留审批 | 官方的审批与安全文档列出几条原则：只连工作流需要的工具，能用受限服务账号就用，先做只读和草稿任务，发送、发布、购买、删除和改生产都要审批，定期检查连接器和 routine，留下来源链接和操作日志。所有 bot 共用一台电脑，不能把不同 bot 当安全隔离。 | 官方文档 | ★★★★☆ | [docs.x.ai](https://docs.x.ai/grok-bot/approvals-security-and-privacy) |
| 5-12 | Slack 里加一个 :grok: 表情按钮 | 作者做了一个自定义的 :grok: 表情，给任何帖子点上它，bot 会在 30 分钟内读到并处理：加进议程、开 ticket 或起草回复。不需要专门做集成，只要一个 routine。 | 1赞 | ★★★☆☆ | [@imrogb](https://x.com/imrogb/status/2110320214122369106) |
| 5-13 | 每 2 小时清理 box | 作者开了太多 bot，把 box 跑挂了，于是加了一个每 2 小时检查一次的 routine。 | — | ★★★☆☆ | [@hijeffrey46](https://x.com/hijeffrey46/status/2110313550921310537) |
| 5-14 | Notion 和 Drive 当第二记忆，每周备份到 NAS | 把 Notion 和 Google Drive 当成 bot 的第二记忆，每周再让 bot 备份到家里的 NAS。 | — | ★★★☆☆ | [@GReid11802](https://x.com/GReid11802/status/2110391486244102159) |
| 5-15 | 第二大脑：给 bot 一个文件夹 | 作者借用 Karpathy 的第二大脑思路：在 bot 的云电脑上给它一个文件夹，把资料喂进去，由它维护。 | 39赞/45藏 | ★★★☆☆ | [@Argona0x](https://x.com/Argona0x/status/2110382009843331163) |
| 5-16 | 只让 bot 读 Claude Code 和 Codex 的会话记录 | 每次结束 Claude Code 或 Codex 的会话，记录会自动存进 Obsidian。bot 只被允许读这些记录，用来让几个 agent 的项目上下文保持同步。 | — | ★★★☆☆ | [@kithng](https://x.com/kithng/status/2110274830662766843) |
| 5-17 | 额度用完时留一条备用路线 | 有一次额度耗尽，所有 bot 停了三四天。之后作者一直准备着第二条路线，避免一处限额让整天都停下来。 | 1赞 | ★★★☆☆ | [@Steve_Y1986](https://x.com/Steve_Y1986/status/2110225623751037410) |
| 5-18 | 安全监控 bot Watchtower | 所有 bot 共用一台电脑和同一套登录状态，一个坏的 skill 就可能碰到全部东西。Watchtower 负责盯着这类风险。 | 1赞 | ★★★☆☆ | [@Ken_LinkWell](https://x.com/Ken_LinkWell/status/2109749307863969945) |
| 5-19 | grok-bot-jev：用便宜的决策层控制用量 | 把 TypeSafe Jev 接到 Grok Bot 当廉价决策层，先判断要不要跑完整任务，附用量闸门、skill 模板和示例。思路和“先便宜检查再跑完整任务”一致。适合额度紧张的人。 | 107★ | ★★★☆☆ | [Bodila51](https://github.com/Bodila51/grok-bot-jev) |
| 5-20 | 好 tip 的标准：去掉一个反复出现的决定 | @jbellware 认为最好的用法是把工作流里一个反复出现的决定去掉。建议从一个保存好的提示词加明确的输出格式开始，再衡量它是真的缩短了反应时间，还是只多开了一个标签页。这是评估任何 routine 是否值得留下的好标准。 | — | ★★★☆☆ | [@jbellware](https://x.com/jbellware/status/2102056606078824645) |
| 5-21 | Grok Bot 和 Hermes 的比较讨论 | 有一个帖子讨论 Grok Bot 能不能被本地的 Hermes 替代，回复里有不少人分享了自己的取舍。 | 62赞 | ★★☆☆☆ | [@Chris_Wozniczek](https://x.com/Chris_Wozniczek/status/2109997583477440729) |
| 5-22 | 侧边键语音唤起 bot 的坑 | 把手机侧边键设成唤起 Grok Bot 后，走路或开会间隙都能派活。作者踩过的坑：别在公共场合念密码；说完别急着锁屏，它可能还在听；复杂的活拆成两句说。 | — | ★★☆☆☆ | [@hvabdq](https://x.com/hvabdq/status/2110356130178142516) |
| 5-23 | 通勤时用语音操作浏览器（日文） | 语音控制很强，通勤时可以让 bot 操作浏览器，开车通勤的人受益最大。前提是事先把要用的浏览器和信息准备好交给它。 | — | ★★☆☆☆ | [@digista_net](https://x.com/digista_net/status/2110376344500752839) |
| 5-24 | 额度焦虑与计费意外 | @EranHertz 半开玩笑说用 bot 最多的是对剩余额度的焦虑；@jrprehn 则在升级后看到超过 1000 美元的用量费用而困惑。征集帖里多人提到额度很快用完。开大规模 routine 前，先看清计费方式并设上限。 | — | ★★☆☆☆ | [@jrprehn](https://x.com/jrprehn/status/2105171258224824554) |

[← 返回目录](../README.md)
