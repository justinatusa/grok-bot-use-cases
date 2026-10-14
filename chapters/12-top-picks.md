# 先扫版：4 星和 5 星

只想先看最值得试的，从这里开始。条目和分类章节里的一样，这里按推荐程度和分类排列，每条附一段说明。

- **1-1 · ★★★★★ · 邮件和收件箱** [bot 独立邮箱处理项目邮件](https://x.com/TheRundownAI/status/2109750003313037547)（TheRundownAI，23赞）
  把项目邮件抄送或转发到 bot 自己领取的邮箱。bot 读到改期之类的变化后，会总结哪里变了，再起草一封标着“需批准”的回复。用到的是 bot 邮箱和草稿审批。好处是改期不会漏看，回复又始终要你点头才发。

- **1-2 · ★★★★★ · 邮件和收件箱** [每 15 分钟查邮件，按你的语气起草回复](https://x.com/IsaiahCrossman/status/2110368460106600711)（IsaiahCrossman，1赞）
  先让另一个模型读一遍自己的历史邮件，写出一份“我的写信风格”说明，再交给 bot。之后由 routine 每 15 分钟查一次邮箱，需要回复的就起草好。作者说有的草稿一字没改就直接发了。前期花点时间做风格说明，后面就省事。

- **1-3 · ★★★★★ · 邮件和收件箱** [大客户来信时自动备好回复（事件触发）](https://x.com/warriormomLA/status/2110396247274397791)（warriormomLA，—）
  这个 routine 不按时间跑，而是等重要客户来信时才启动。bot 先拉出这个客户的往来历史，查一下日历，再写好一份回复草稿。等你看到通知的时候，草稿已经在那了。比按时间轮询省额度，反应也更快。

- **2-1 · ★★★★★ · 调研和信息雷达** [X 收藏夹每 6 小时自动分类进 Notion](https://x.com/jestonlu/status/2109667034862862418)（jestonlu，1659赞/2762藏）
  bot 每 6 小时抓取一次 X 收藏，按主题分类写进 Notion 数据库。用到 X 插件、Notion 连接器和 routine。收藏终于不再只是堆在那里，是本次收集到的热度最高的用法之一。

- **2-2 · ★★★★★ · 调研和信息雷达** [收藏夹每日邮件：找关联加今日可用点子](https://x.com/jestonlu/status/2110028601554845836)（jestonlu，216赞/394藏）
  这是上面那个 agent 的 v2：每 24 小时发一封邮件，挑出 2 到 4 条话题不相关但底层想法相通的收藏。邮件最后给一条当天就能用在工作上的点子。重点不是分类，而是让收藏重新被翻出来用上。

- **2-3 · ★★★★★ · 调研和信息雷达** [每天把关注列表和 X 列表做成简报](https://x.com/giselleh/status/2110243450373472602)（giselleh，4赞）
  授权 X 插件后，bot 直接读时间线、关注列表和自建的 X 列表，按需要每天定时出简报。作者不用再自己刷 X，也比自己调 X API 便宜。中文圈很多人在这样用。

- **3-1 · ★★★★★ · 编程和 PR 看护** [对抗式 review bot 把关 PR](https://x.com/jason_bennitt/status/2109007446530482388)（jason_bennitt，—）
  负责构建的 bot 把 PR 交给一个专门审代码的 review bot，修完它提的问题后，再交给 CoS bot 合并。合并的门槛是每个仓库的 CI 全绿，加上 review bot 读完全部 diff。今天它拦下了一个 167 个文件的 PR，要求先修 6 处。这是把“自己审自己”换成“另一个 bot 来挑错”。

- **3-2 · ★★★★★ · 编程和 PR 看护** [线上报错自动出修复 PR](https://x.com/karloscodes/status/2110282717216551360)（karloscodes，—）
  生产环境出错时，LogNorth 监控抓到问题并唤醒 bot。bot 读日志，写一个会失败的测试，再写修复，然后开 PR。合并由人来做。从发现故障到出修复的链路是完整的。

- **3-3 · ★★★★★ · 编程和 PR 看护** [用户报 bug 到修复上线的闭环](https://x.com/jenkins_bevan/status/2109473918130241937)（jenkins_bevan，1赞）
  家长在 app 里报 bug，helpdesk bot 开 GitHub issue，Codex 提修复 PR，作者合并，再自动回复家长。作者一个人开发，还有全职工作。客服加开发的闭环全靠 bot 撑着。

- **3-4 · ★★★★★ · 编程和 PR 看护** [Engineering Lead：把开发闭环交给一个 bot](https://x.ai/bot/Ks3X7JpD-6I86s3zkJFRh)（poteto，官方市场）
  Lauren Tan（poteto）做的官方模板。它把工作拆成多个 Cloud Agent 任务，追 CI，做 review，并在工作日定期检查卡住的事。等于一个专职的技术负责人，人只需要合并和拍板。和多 bot 开发团队的做法一致，但已经是现成配置。

- **4-1 · ★★★★★ · 多 bot 协作与沟通渠道** [一个 CoS 管 8 个 bot，同时跑 500 多个 agent](https://x.com/0xGenAi/status/2109406731499389058)（0xGenAi，145赞/237藏）
  转述官方工程师的说法：从同时跑 30 个 agent 到 500 多个，用的只是 8 个 bot，他只跟其中一个说话。那个就是 Chief of Staff bot，整个职责一条 prompt 就能写下。

- **4-2 · ★★★★★ · 多 bot 协作与沟通渠道** [10 个 bot 加一个协调者运营一家 IT 公司](https://x.com/gdz_it/status/2108977193846005878)（gdz_it，2赞）
  大约 10 个 bot 加一个协调者，分管营销、邮件、获客、AI 动态和记账。代码交给 Cursor、Claude Code 和 Codex，n8n 负责发帖。没有作者同意，什么都不发出去。

- **5-1 · ★★★★★ · 省额度、routine 和安全** [每 5 分钟跑一次比每小时贵 12 倍](https://x.com/gippp69/status/2109235458383216811)（gippp69，255赞/469藏）
  一篇长文讲 routine 的频率和成本：每 5 分钟跑一次，花费是每小时跑一次的 12 倍。教你按需求定频率。

- **5-2 · ★★★★★ · 省额度、routine 和安全** [先轻量检查，有变化才跑完整任务](https://x.com/gippp69/status/2110321307359322494)（gippp69，38赞）
  整晚的 96 次运行里，94 次什么都没发现。办法是存一个 /night-filter skill：一个 bot 每 5 分钟只看有没有变化，没变化就不跑完整任务。

- **11-1 · ★★★★★ · 模板、目录和教程** [dr eggbot：先问几个问题再替你设计 bot](https://x.ai/bot/_jOdbfkB16zxu7MRcmReE)（poteto，官方市场）
  poteto 做的元模板，收录在官方市场。它先问你几个偏好问题，再设计一个结构完整的 bot 并直接创建出来。适合不知道 bot 的职责、来源、审批边界该怎么写的人。拿它生成第一版，再自己改，比从空白开始快得多。

- **11-2 · ★★★★★ · 模板、目录和教程** [awesome-grok-bot-templates：4500 多个模板的总目录](https://github.com/Maimuzamilhu/awesome-grok-bot-templates)（Maimuzamilhu，GitHub）
  这个仓库按用途整理了 4537 个公开的 Grok Bot 模板链接，每个都标了权限等级（不连账号、连账号、可动钱或发布删除）和运行频率。配套网站 botsdots.site 可以按分类、应用和权限筛选。找现成模板时先查这里，比在 X 上翻快很多。权限标注能帮你优先挑低风险的。

- **1-4 · ★★★★☆ · 邮件和收件箱** [iCloud 邮件自动转发给 bot](https://x.com/CARN0N/status/2110190319807643717)（CARN0N，6赞）
  Apple 的服务没有官方连接器，作者就在 iCloud 里设了自动转发，把邮件转到 bot 的邮箱。每来一封新邮件，bot 都会自动处理。这个办法绕开了缺少连接器的问题，用 Outlook 或公司邮箱的人也可以照搬。

- **1-5 · ★★★★☆ · 邮件和收件箱** [用转发 Gmail 触发提醒](https://x.com/loam_yu/status/2110322352089182280)（loam_yu，1赞）
  bot 只会自动处理发到它自己邮箱的信。所以作者在 Gmail 里设了过滤规则，把需要注意的邮件转发过去，以此触发提醒。帖子里附了 Gmail 的操作截图。这是一种不用开放整个邮箱的接入方式，权限比较小。

- **1-6 · ★★★★☆ · 邮件和收件箱** [bot 邮箱仪表盘（有模板）](https://x.com/jadmthw/status/2110210896085819557)（jadmthw，1赞）
  根据 bot 邮箱的收发记录生成一个网页，可以搜索、筛选，还会列出哪些信还没回。每来一封新邮件，页面就自动重建一次。整个页面都是 bot 自己做的，作者公开了模板。适合 bot 邮件往来比较多的人。

- **1-7 · ★★★★☆ · 邮件和收件箱** [请人员搜索网站删除你的个人信息](https://x.com/MeowRocketGo/status/2109727769315750318)（MeowRocketGo，2赞）
  让 bot 逐个找出公开你住址和电话的人员搜索网站，用它自己的邮箱发删除请求，再填好退出表单。验证码由 bot 自己处理，最后再点确认邮件里的链接。这类事又多又繁琐，人自己很少会做完。注意：这样会把个人信息交给 bot 去处理。

- **1-8 · ★★★★☆ · 邮件和收件箱** [The Morning Newspaper：一份早报式的个人简报](https://x.ai/bot/1xAJYJPes3X7dUM2mk9Di)（CodeChap，官方市场）
  官方市场模板，夜里读你的收件箱和日历，早饭前排成一份报纸样式的简报。和普通的邮件摘要相比，它把日程和邮件放在一起看。需要连邮箱和日历，属于中等权限。适合每天早上想一眼看清当天要事的人。

- **1-9 · ★★★★☆ · 邮件和收件箱** [出差订票、报销、会议纪要、催交付一条龙](https://www.reddit.com/r/GrokBot/comments/1wiuwmw/whats_the_most_useful_grokbot_automation_youve/)（r/GrokBot，Reddit）
  Reddit 上有人让 bot 订所有出差行程，并把行程发给同行的人。收据转给它就处理报销。它还写会议纪要，每天早上给一份行动项清单，并给逾期两天以上没交东西的人起草催促邮件。这是把助理工作整体交出去的例子。

- **1-10 · ★★★★☆ · 邮件和收件箱** [每天一封邮件：待办、日程和提醒](https://x.com/FiloPietra/status/2101974530613010650)（FiloPietra，—）
  @FiloPietra 让 bot 根据他所有的工作内容，每天发一封邮件，列出当天、本周和本月的待办、日程和个人提醒。做法简单，几乎人人适用。是很好的第一个 routine。

- **2-4 · ★★★★☆ · 调研和信息雷达** [关注和清单都变成每日简报，不再刷 X](https://x.com/howie_serious/status/2110282858665587162)（howie_serious，1赞）
  作者把自己的全部关注和清单都交给 bot 做成每日简报，说每天 1000 次的额度也够用。不用再看营销号和低质内容。适合信息源多、不想天天刷 X 的人。

- **2-5 · ★★★★☆ · 调研和信息雷达** [指定几个人一发帖就推送](https://x.com/TreyFocus/status/2110285116828516627)（TreyFocus，1赞）
  作者只想看少数几个人的帖子，就让 bot 盯着这几个账号，对方一发帖就推送给他。这样他就不用天天打开 X 了。做法很简单，信噪比却很高。

- **2-6 · ★★★★☆ · 调研和信息雷达** [用 X 搜索做定时爆款雷达](https://x.com/yugen_matuni/status/2110202705461588025)（yugen_matuni，277赞）
  bot 每天有 1000 次请求，每次能搜 25 条 X 帖子。作者设了定时调查，找出某个圈子里 1 小时内曝光超过 5 万的帖子，个人也能很快拿到 X 上可能爆的内容。作者另外建议去掉引用帖、直接找源头，这样一手信息更多。

- **2-7 · ★★★★☆ · 调研和信息雷达** [每小时巡检群聊，按价值排好放进飞书](https://x.com/jingran96/status/2110316274802930018)（jingran96，1赞）
  bot 每小时巡检一次微信群等信息流，扫到的东西按价值排序，自动整理进飞书。作者说也有翻车的时候。适合要跟很多群消息的人。

- **2-8 · ★★★★☆ · 调研和信息雷达** [从 Zotero 文献库每天推荐新论文](https://x.com/Yorks0n/status/2110290968822087859)（Yorks0n，—）
  作者把自己写的 Zotero 每日文献推荐工具的 GitHub 仓库交给 bot，可重复运行的部分放在 bot 电脑上跑。拿到候选论文后，再让 bot 按他可能的喜好挑一遍推荐给他。他还让 bot 每天看几个常逛的 Reddit 社区有什么新鲜事。把现有的脚本和 bot 的判断结合起来，这个思路很适合做研究的人。

- **2-9 · ★★★★☆ · 调研和信息雷达** [用 60 天的互动整理出 4 个私人 X 列表](https://x.com/tonysimons_/status/2110234923084734741)（tonysimons_，26赞）
  bot 读取作者 60 天里真实的回复和提及，建了 4 个私人列表：核心圈、AI 开发者、AI 创作者、潜在合作者。每个 handle 都核实过，证明不了的就直说，没有乱编。适合重新整理自己的社交关系。

- **2-10 · ★★★★☆ · 调研和信息雷达** [Cooper：每天 8 点的 AI 与科技新闻简报](https://x.ai/bot/8hhdYqfvRzigWstUtcmBZ)（TommyHansenTA，官方市场）
  官方市场模板，覆盖 AI、科技、风投和商业新闻，每天早上 8 点在 Slack 发一份精简简报，工作日中午再补一次。简报发到团队频道，大家看到的是同一份信息。想做自己的信息雷达，可以拿它的结构改成你关心的领域。

- **2-11 · ★★★★☆ · 调研和信息雷达** [Competitor Watch：竞品页面变化提醒](https://x.ai/bot/aw0Zj54sIsAK7vMnajdz0)（scheemunai，官方市场）
  官方市场模板，你贴一组竞品的定价、产品和招聘页面网址，它定期查看，只在真有变化时才写简报给你。不需要连接任何账号，权限最低。这是“先便宜地查有没有变化，再决定要不要写报告”的典型做法。

- **3-5 · ★★★★☆ · 编程和 PR 看护** [ticket 到 PR 的流程搬进 bot，还会盯 PR](https://x.com/denCual/status/2110317406963064838)（denCual，—）
  作者把从 ticket 到 PR 的整套流程搬进了 Grok Bot，它会一直盯着 PR 的状态。他还把 bot 的电脑加进 Tailscale，用来管自己的 VM、在 VM 里开 Claude Code，再从手机访问。

- **3-6 · ★★★★☆ · 编程和 PR 看护** [小模型实验的探针和基线](https://x.com/byron_miller/status/2109001058022461951)（byron_miller，2赞）
  bot 为作者的小模型实验室做了一套快速失败探针，还跑了 Pythia 和 SmolLM2 的参考基线。每个 PR 作者都亲自审，bot 按他审出的问题修，前后改了 3 轮。是研究类工程的好例子。

- **3-7 · ★★★★☆ · 编程和 PR 看护** [一支开发团队：orchestrator、tech lead、IT、会议](https://x.com/ThiagoCosta50/status/2108987619627368623)（ThiagoCosta50，1赞）
  一个 orchestrator，加一个负责驱动 Codex 和 Cursor agent 的 tech lead，再加 IT 支持 bot 和会议 bot。这一周它们把 ticket 和电脑的对应关系做了出来，抓到一条坏掉的流水线，还在树莓派上把一个网站部署上线了。上生产必须作者同意。

- **3-8 · ★★★★☆ · 编程和 PR 看护** [调度家里 Mac mini 上的 Claude Code](https://x.com/cbgrok/status/2109329337053020643)（cbgrok，—）
  bot 整周调度家里 Mac mini 上的 Claude Code：提任务、审 PR，agent 卡住时有一个普通脚本负责重启。它还抓到了一封荷兰海关通知，Teams 上只在紧急时才提醒作者。

- **3-9 · ★★★★☆ · 编程和 PR 看护** [远程 Mac 上做 iOS app，在模拟器上测试](https://x.com/enjojoyy/status/2110316983572943178)（enjojoyy，9赞）
  bot 能访问家里的 Mac mini，在上面让 Codex 和 Claude 用 Xcode 做 iOS app，在模拟器里测试，需要素材时用 Blender 生成。作者从手机或 iPad 下指令。

- **3-10 · ★★★★☆ · 编程和 PR 看护** [把编码任务分给 Codex CLI 和多台机器](https://x.com/EspressoMagi/status/2110378835741208861)（EspressoMagi，1赞）
  作者觉得最大的效率提升在编排：bot 把编码任务交给 Codex CLI agent 和本地模型，分散到五台机器上跑。作者只看结果，不用在工具之间来回切换。

- **3-11 · ★★★★☆ · 编程和 PR 看护** [lauren-poteto-rules：可信编码 agent 工作流的规则](https://github.com/unicodef1wn/lauren-poteto-rules)（unicodef1wn，86★）
  受 Lauren Tan 启发整理的一套工程规则，讲怎么让编码 agent 的工作流值得信任。可以直接作为开发 bot 的规则底稿。和对抗式 review 关卡的思路配合使用效果更好。

- **3-12 · ★★★★☆ · 编程和 PR 看护** [grok-ship：把 Grok Bot 变成软件工厂](https://github.com/kunchenguid/grok-ship)（kunchenguid，187★）
  一套让 Grok Bot 承担完整软件交付流程的配置。适合想把“ticket 到 PR”流程标准化的人。可以和 Engineering Lead 模板对照着看，挑适合自己的那套。

- **3-13 · ★★★★☆ · 编程和 PR 看护** [在超市里口述想法，bot 改写成 prompt 交给 Cursor](https://www.reddit.com/r/GrokBot/comments/1wiuwmw/whats_the_most_useful_grokbot_automation_youve/)（r/GrokBot，Reddit）
  Reddit 用户让 bot 连上开发文档，出门时随口发几句简写想法，bot 改写成正式的 prompt，再通过命令行交给 Cursor 写代码。人在外面，开发也不停。核心价值是 bot 当了“需求翻译层”。适合经常有零碎想法的开发者。

- **4-3 · ★★★★☆ · 多 bot 协作与沟通渠道** [13 个 bot，每个只管一摊](https://x.com/ALThorne_Toren/status/2110345240024391964)（ALThorne_Toren，2赞）
  作者有 13 个助手：写作、发布、GitHub 和网站、Google Workspace、M365、Telegram、YouTube、学校、会议、幻灯片、Slack、会议纪要，再加一个负责分派的 CoS。规矩是每项工作只有一个负责人。

- **4-4 · ★★★★☆ · 多 bot 协作与沟通渠道** [9 个 bot，什么都做，但什么都不发](https://x.com/noahfleming/status/2110347502272524540)（noahfleming，1赞）
  两周内搭了 9 个 bot：收件箱、销售、财务、内容，连家庭日历都有。它们干很多活，但一封都不会自己发出去。帖子写了做到这一点的 4 条规矩。

- **4-5 · ★★★★☆ · 多 bot 协作与沟通渠道** [只跟一个 bot 说话，决定一键回答](https://x.com/robcressy/status/2110159155566670279)（robcressy，1赞）
  作者整天只和一个 bot 说话，整个团队在它背后干活，递到他面前的只有一键就能回答的决定。他完全没有技术背景。

- **4-6 · ★★★★☆ · 多 bot 协作与沟通渠道** [协调者每天跑 3 次目标检查](https://x.com/nanosapien1/status/2110226846357106799)（nanosapien1，1赞）
  先给所有 bot 分好职责，再让协调者每天 3 次跑一个“目标检查” skill，追问各个队友的进度。作者在外面忙别的事时，目标也在往前推。

- **4-7 · ★★★★☆ · 多 bot 协作与沟通渠道** [负责人检查 routine 是否运行、有没有超量](https://x.com/developkerr/status/2110282312218788287)（developkerr，—）
  负责人 bot 每天早上检查各个 routine 有没有跑、用量是否正常。PM bot 在 Linear 里把 issue 补全到可以开工的状态。分工清楚。

- **4-8 · ★★★★☆ · 多 bot 协作与沟通渠道** [交接必须回“收到”](https://x.com/catalystcw/status/2110281119547421172)（catalystcw，—）
  两个 routine 盯着同一个卡住的任务，导致提醒发了两遍；还有一次交接失败，是因为没人确认下一个 agent 接手了。修法是每项检查只归一个 routine，每次交接都要回一句“收到”，否则就报警。

- **5-3 · ★★★★☆ · 省额度、routine 和安全** [一晚 288 次空跑，烧掉 412 美元](https://x.com/bl888m_eth/status/2110357844071497850)（bl888m_eth，27赞）
  作者的 bot 团队每 4 分钟检查一次已经不动的行情，每次都唤醒全员，一晚上跑了 288 次，花掉 412 美元。这是一个反面教材。

- **5-4 · ★★★★☆ · 省额度、routine 和安全** [抓出浪费 99% 运行的 agent](https://x.com/Nyxera0x/status/2110312522498658652)（Nyxera0x，23赞）
  7 个 agent 分别管 X、邮件、CI、部署、文档和审计，其中一个每次醒来都只报 NO_CHANGE。修法和换更强的模型无关，而是改触发方式。

- **5-5 · ★★★★☆ · 省额度、routine 和安全** [让 bot 自己砍掉 40% 用量](https://x.com/c_olsson/status/2110323881563111543)（c_olsson，—）
  直接问 bot：“怎么在不降质量的前提下把用量砍掉 40%？”它会把 routine 改成事件触发、去掉重复读取、没事就静默。

- **5-6 · ★★★★☆ · 省额度、routine 和安全** [先手动做一次，再存成 skill，最后排进日程](https://x.com/Cyb3rCricket/status/2110121951175852534)（Cyb3rCricket，—）
  很多自动化坏掉，是因为还没手动跑通就先排了日程。官方推荐的顺序是：先在聊天里做对一次，存成 skill，再设成 routine。

- **5-7 · ★★★★☆ · 省额度、routine 和安全** [用一条提示词体检自己的 bot](https://x.com/KatieMiller/status/2110156792651026619)（KatieMiller，619赞/236藏）
  作者用一条提示词让 Grok Bot 检查她的几个 bot，结果让她很满意。这种自查值得定期做。

- **5-8 · ★★★★☆ · 省额度、routine 和安全** [把一台 Linux 机器整个交给 bot 维护](https://www.reddit.com/r/grok/comments/1w8w0gg/grok_bot_is_awesome/)（r/grok，Reddit）
  Reddit 用户不熟 Linux，就告诉 bot 这台机器归它管。bot 做完交代的项目后，自己排了更新和巡检计划，每天早上发一份机器状态报告。适合有家用服务器但不想维护的人。

- **5-9 · ★★★★☆ · 省额度、routine 和安全** [routine 漏跑的应对：重要的事别放无人值守](https://www.reddit.com/r/GrokBot/comments/1w2g9xt/anyone_having_problems_with_grok_bots_remembering/)（r/GrokBot，Reddit）
  Reddit 上多人反映夜间 routine 有时不跑，问它才说“没跑，要现在跑吗”。有经验的人建议，夜里只放低风险、第二天容易检查的活，比如提纲、缺口清单。也有人让 bot 自己诊断并重写 routine 后恢复正常。X 上 @PerssonAC 也反映过 routine 不可靠或严重延迟。

- **5-10 · ★★★★☆ · 省额度、routine 和安全** [九个值得先装的 routine（含审批规则）](https://www.theaigentic.com/hands-on/nine-grok-bot-routines)（The Aigentic，博客）
  The Aigentic 根据几位博主的演示整理了九个 routine：早 7:30 收件箱分诊、每日细分领域调研、每周 X 侦察、周一机票价格监控、每周清理订阅和 Drive、多邮箱巡检、营收调研循环、晚间会议准备等。每个都附时间表、起手提示词和审批规则。文章强调先手动跑一次并纠正，再排进日程。

- **5-11 · ★★★★☆ · 省额度、routine 和安全** [官方安全清单：只连需要的工具，对外动作留审批](https://docs.x.ai/grok-bot/approvals-security-and-privacy)（docs.x.ai，官方文档）
  官方的审批与安全文档列出几条原则：只连工作流需要的工具，能用受限服务账号就用，先做只读和草稿任务，发送、发布、购买、删除和改生产都要审批，定期检查连接器和 routine，留下来源链接和操作日志。所有 bot 共用一台电脑，不能把不同 bot 当安全隔离。

- **6-1 · ★★★★☆ · 购物、出行和办事** [接 Twilio 号码，让 bot 打电话](https://x.com/mattstaton/status/2109427232192225588)（mattstaton，—）
  给 bot 一个 Twilio 号码，它就能打电话、收发短信、接电话。作者让它打电话核对了预约，还给他和太太订了餐厅。

- **6-2 · ★★★★☆ · 购物、出行和办事** [约体检，一直追到医院确认](https://x.com/nelsenafc/status/2109174249219092536)（nelsenafc，—）
  bot 在吉隆坡约好了全套体检，一直发邮件跟进，直到医院确认。作者在走进医院之前，一次都没和他们直接沟通过。

- **6-3 · ★★★★☆ · 购物、出行和办事** [让 bot 研究并购买，到货后自动停止查物流](https://x.com/elonmusk/status/2110138164811833534)（elonmusk，8574赞）
  马斯克让 bot 研究并买了乐高，到货后 bot 自己停掉了查物流的 routine。“到货就收尾”这个设计值得借鉴。

- **7-1 · ★★★★☆ · 生活、家庭和健康** [接 Whoop，每天早上安排训练](https://x.com/cbaGPT/status/2109352157376115177)（cbaGPT，—）
  连接 Whoop 后，用一份详细的私教提示词，按家里健身房现有的器材，每天早上发简报和完整的训练计划，连重量都写好。

- **7-2 · ★★★★☆ · 生活、家庭和健康** [每周日自动更新预算并提醒异常](https://x.com/LucasNavallo/status/2109790900897607759)（LucasNavallo，4赞）
  bot 每周日拉银行卡流水、更新预算表，发一份简短总结：钱进了多少、出了多少、有没有新订阅、有没有异常。

- **7-3 · ★★★★☆ · 生活、家庭和健康** [找出被遗忘的自动扣款，做一个资产总览](https://x.com/yaddbruno/status/2109366857677598748)（yaddbruno，1赞）
  作者取消了一堆好几年没用却还在自动扣款的服务，还做了一个总览，把所有银行和投资账户放在一起。

- **7-4 · ★★★★☆ · 生活、家庭和健康** [自写连接器和 skill：银行、处方、iMessage、个人语气](https://www.reddit.com/r/GrokBot/comments/1vwkzf1/heres_how_grok_bot_is_doing_all_the_stuff_i_hate/)（r/GrokBot，Reddit）
  一位 Reddit 用户给自己的 Monzo 银行账户写了连接器，用 skill 接自己写的 NHS 处方命令行，用 iMessage skill 自动删除用过的验证码，还写了一份“我的语气”说明，规定对谁用什么语气。他每天吃 12 片药，自动续处方对他最有用。bot 还帮他发现两个订阅可以合并省钱。

- **8-1 · ★★★★☆ · 内容创作和营销** [bot 调用 Suno、Midjourney、Opus 做 MV](https://x.com/anabology/status/2110224953287070195)（anabology，2501赞/1694藏）
  “Claudia” bot 能调用 Suno、Midjourney 和 Opus 做音乐视频，还用 Grok Imagine 自主做了一支预告片。

- **8-2 · ★★★★☆ · 内容创作和营销** [bot 自己组队做 MV](https://x.com/Z_XSophie/status/2110382853217218631)（Z_XSophie，9赞）
  bot 组了一支自己的队伍：趋势侦察、写词和分镜、生成画面、QC 审片（废掉所有画歪的火箭）、剪辑和配乐。

- **8-3 · ★★★★☆ · 内容创作和营销** [一条录完的口播自动剪成短视频](https://x.com/BenGruenbaum/status/2110389571066187825)（BenGruenbaum，1赞）
  每天早上 bot 给作者一份隔夜大新闻的脚本，作者一口气录完，连口误一起发给 bot，一小时内拿回带字幕和截图的成片。

- **9-1 · ★★★★☆ · 生意和运营** [一周的虚拟 PM：处理客户投诉](https://x.com/Dawoodiddris/status/2109129592501928055)（Dawoodiddris，2赞）
  作者让 bot 当一周 PM：审客户投诉，参照过去的回复起草团队回复，再给产品团队拟一封带待办清单的邮件，发出前交给作者审。

- **9-2 · ★★★★☆ · 生意和运营** [重做网站和 Etsy 店铺](https://x.com/WitbeckLee/status/2108969520023089259)（WitbeckLee，3赞）
  bot 把作者的网站、Etsy 店铺和画廊库存全部重做了一遍，读完上百封手写信后定了营销计划，还搭好了 newsletter。

- **11-3 · ★★★★☆ · 模板、目录和教程** [Alfred：审计整个 bot 组织](https://x.ai/bot/p7Gh6HIrfv4AGzIow6-9X)（heyrobinai，官方市场）
  官方市场模板，负责设计、审计和治理你的整套 bot，让每个 bot 都对应真实目标，有明确的人类负责人，没有重复岗位。bot 一多就容易职责重叠、互相踩额度，这个模板专门解决这个问题。它的权限评级是最高一档（可发布或删除），用前要看清它会改什么。

- **11-4 · ★★★★☆ · 模板、目录和教程** [awesome-grok-bot（中英双语资源表）](https://github.com/RongleCat/awesome-grok-bot)（RongleCat，423★）
  收录 Grok Bot 相关资源的双语清单，423 星，覆盖教程、模板、插件和社区实录。适合中文读者入门。和模板总目录配合用：一个找资源，一个找配置。

- **11-5 · ★★★★☆ · 模板、目录和教程** [grokbot-field-notes：官方团队 72 小时直播搭建的规则和失败记录](https://github.com/unicodef1wn/grokbot-field-notes)（unicodef1wn，594★）
  把官方团队 72 小时直播搭建过程整理成仓库：规则、playbook、bot 角色和失败日志，可以直接放进 AGENTS.md。作者在 ericzakariasson 的征集帖里分享了它。失败日志尤其有用，能少走弯路。适合想搭多 bot 团队的人。

- **11-6 · ★★★★☆ · 模板、目录和教程** [Grok Bot 橙皮书：从入门到多智能体协作](https://github.com/KinGao294/grok-bot-orange-book)（KinGao294，165★）
  中文长篇教程，书名《把一支 AI 团队装进口袋》，覆盖入门、多智能体协作、Routine、省钱与自动化。作者在 X 上也分享过飞书接入教程。适合想系统读一遍的中文用户。

- **11-7 · ★★★★☆ · 模板、目录和教程** [中文上手指南：先画边界再干活](https://zhanghe.dev/zh-CN/posts/7-grok-bot-20260828)（zhanghe.dev，中文博客）
  中文博客强调 Grok Bot 是一台云端 Linux 电脑加一群同事，所有 bot 共用一台电脑、共享登录态，屏幕分开但安全边界不分开。建议先设审批，遇到密码、验证码、付款时让 bot 交还控制权。有插件的服务优先用插件，比让它点网页稳。

- **11-8 · ★★★★☆ · 模板、目录和教程** [官方文档：先做一次，存成 skill，再排进 routine](https://cursor.com/docs/grok-bot/work.md)（Cursor Docs，官方文档）
  官方文档建议从一次性任务开始，做稳之后把方法存成 skill，最后才排成定时 routine。也可以用“Teach a task”把浏览器操作演示一遍（最长 10 分钟），让 bot 生成 skill 草稿，再补决策规则和失败处理。这是所有 routine 用法的基础流程。

[← 返回目录](../README.md)
