# 编程和 PR 看护

开发者把 bot 放在 IDE 之外的“外循环”：接 bug、开 PR、追 CI、做 review。本章收集从报错到修复 PR 的闭环和对抗式审查的做法。

本章共 23 条，按推荐程度从高到低排列，低分条目也保留。

| 编号 | 用法 | 做法与价值 | 热度 | 推荐程度 | 来源 |
| --- | --- | --- | --- | --- | --- |
| 3-1 | 对抗式 review bot 把关 PR | 负责构建的 bot 把 PR 交给一个专门审代码的 review bot，修完它提的问题后，再交给 CoS bot 合并。合并的门槛是每个仓库的 CI 全绿，加上 review bot 读完全部 diff。今天它拦下了一个 167 个文件的 PR，要求先修 6 处。这是把“自己审自己”换成“另一个 bot 来挑错”。 | — | ★★★★★ | [@jason_bennitt](https://x.com/jason_bennitt/status/2109007446530482388) |
| 3-2 | 线上报错自动出修复 PR | 生产环境出错时，LogNorth 监控抓到问题并唤醒 bot。bot 读日志，写一个会失败的测试，再写修复，然后开 PR。合并由人来做。从发现故障到出修复的链路是完整的。 | — | ★★★★★ | [@karloscodes](https://x.com/karloscodes/status/2110282717216551360) |
| 3-3 | 用户报 bug 到修复上线的闭环 | 家长在 app 里报 bug，helpdesk bot 开 GitHub issue，Codex 提修复 PR，作者合并，再自动回复家长。作者一个人开发，还有全职工作。客服加开发的闭环全靠 bot 撑着。 | 1赞 | ★★★★★ | [@jenkins_bevan](https://x.com/jenkins_bevan/status/2109473918130241937) |
| 3-4 | Engineering Lead：把开发闭环交给一个 bot | Lauren Tan（poteto）做的官方模板。它把工作拆成多个 Cloud Agent 任务，追 CI，做 review，并在工作日定期检查卡住的事。等于一个专职的技术负责人，人只需要合并和拍板。和多 bot 开发团队的做法一致，但已经是现成配置。 | 官方市场 | ★★★★★ | [@poteto](https://x.ai/bot/Ks3X7JpD-6I86s3zkJFRh) |
| 3-5 | ticket 到 PR 的流程搬进 bot，还会盯 PR | 作者把从 ticket 到 PR 的整套流程搬进了 Grok Bot，它会一直盯着 PR 的状态。他还把 bot 的电脑加进 Tailscale，用来管自己的 VM、在 VM 里开 Claude Code，再从手机访问。 | — | ★★★★☆ | [@denCual](https://x.com/denCual/status/2110317406963064838) |
| 3-6 | 小模型实验的探针和基线 | bot 为作者的小模型实验室做了一套快速失败探针，还跑了 Pythia 和 SmolLM2 的参考基线。每个 PR 作者都亲自审，bot 按他审出的问题修，前后改了 3 轮。是研究类工程的好例子。 | 2赞 | ★★★★☆ | [@byron_miller](https://x.com/byron_miller/status/2109001058022461951) |
| 3-7 | 一支开发团队：orchestrator、tech lead、IT、会议 | 一个 orchestrator，加一个负责驱动 Codex 和 Cursor agent 的 tech lead，再加 IT 支持 bot 和会议 bot。这一周它们把 ticket 和电脑的对应关系做了出来，抓到一条坏掉的流水线，还在树莓派上把一个网站部署上线了。上生产必须作者同意。 | 1赞 | ★★★★☆ | [@ThiagoCosta50](https://x.com/ThiagoCosta50/status/2108987619627368623) |
| 3-8 | 调度家里 Mac mini 上的 Claude Code | bot 整周调度家里 Mac mini 上的 Claude Code：提任务、审 PR，agent 卡住时有一个普通脚本负责重启。它还抓到了一封荷兰海关通知，Teams 上只在紧急时才提醒作者。 | — | ★★★★☆ | [@cbgrok](https://x.com/cbgrok/status/2109329337053020643) |
| 3-9 | 远程 Mac 上做 iOS app，在模拟器上测试 | bot 能访问家里的 Mac mini，在上面让 Codex 和 Claude 用 Xcode 做 iOS app，在模拟器里测试，需要素材时用 Blender 生成。作者从手机或 iPad 下指令。 | 9赞 | ★★★★☆ | [@enjojoyy](https://x.com/enjojoyy/status/2110316983572943178) |
| 3-10 | 把编码任务分给 Codex CLI 和多台机器 | 作者觉得最大的效率提升在编排：bot 把编码任务交给 Codex CLI agent 和本地模型，分散到五台机器上跑。作者只看结果，不用在工具之间来回切换。 | 1赞 | ★★★★☆ | [@EspressoMagi](https://x.com/EspressoMagi/status/2110378835741208861) |
| 3-11 | lauren-poteto-rules：可信编码 agent 工作流的规则 | 受 Lauren Tan 启发整理的一套工程规则，讲怎么让编码 agent 的工作流值得信任。可以直接作为开发 bot 的规则底稿。和对抗式 review 关卡的思路配合使用效果更好。 | 86★ | ★★★★☆ | [unicodef1wn](https://github.com/unicodef1wn/lauren-poteto-rules) |
| 3-12 | grok-ship：把 Grok Bot 变成软件工厂 | 一套让 Grok Bot 承担完整软件交付流程的配置。适合想把“ticket 到 PR”流程标准化的人。可以和 Engineering Lead 模板对照着看，挑适合自己的那套。 | 187★ | ★★★★☆ | [kunchenguid](https://github.com/kunchenguid/grok-ship) |
| 3-13 | 在超市里口述想法，bot 改写成 prompt 交给 Cursor | Reddit 用户让 bot 连上开发文档，出门时随口发几句简写想法，bot 改写成正式的 prompt，再通过命令行交给 Cursor 写代码。人在外面，开发也不停。核心价值是 bot 当了“需求翻译层”。适合经常有零碎想法的开发者。 | Reddit | ★★★★☆ | [r/GrokBot](https://www.reddit.com/r/GrokBot/comments/1wiuwmw/whats_the_most_useful_grokbot_automation_youve/) |
| 3-14 | Autoloop 插件：7×24 小时循环开发 | 作者给 Grok Bot 做了一个循环开发插件：自动建分支，自己写代码、改代码，跑测试。是全自动迭代。要有很好的测试兜底，不然容易跑偏。 | 1赞 | ★★★☆☆ | [@arito_si](https://x.com/arito_si/status/2110329208484376618) |
| 3-15 | 按影响范围打分，过夜修小 bug | 客户的 bug 从 GitHub 和邮件进来，先按“修了会波及多少”打分，低于阈值才让 agent 过夜自动修。早会前就修好了 7 个。帖子语气比较夸张，阈值设计倒是可以借鉴。 | 4赞 | ★★★☆☆ | [@DonatelloXPro](https://x.com/DonatelloXPro/status/2110307374158471171) |
| 3-16 | Dev bot 跑 pstack 并 squash merge | 作者在 Omarchy 上建了几个 bot，其中 Dev bot 对自己的应用和插件跑 pstack，再 squash merge。一天就把 Cursor 额度用完了。说明这种用法很耗额度。 | 1赞 | ★★★☆☆ | [@ShieldsWorks](https://x.com/ShieldsWorks/status/2109001868731167105) |
| 3-17 | bot 主动接活，问你要不要做（日文） | 以前作者是把需求消息的链接丢给 AI，让它开 PR。现在 bot 会自己发现需求消息，问他“要不要做”，他只需要说“好”。作者打算让完成标准清楚的小修改自动做到开 PR 为止。 | — | ★★★☆☆ | [@aku11i](https://x.com/aku11i/status/2110394935543480495) |
| 3-18 | 主力用 Cursor Cloud，本地任务交给专用 agent（日文） | 作者的 Grok Bot 平时调用 Cursor Cloud 干活；要碰本地 Mac 的任务，就交给一个专门熟悉本地开发工具和配置的 agent。云端和本地分工明确。 | 2赞 | ★★★☆☆ | [@miyatti](https://x.com/miyatti/status/2110384527948611613) |
| 3-19 | 20 分钟做出 Stripe 计费模块 | 作者让 bot 基于 Stripe 做一个计费模块，20 分钟出了结果。这只是一个演示，生产环境用之前需要人工审。 | — | ★★★☆☆ | [@TwoWeeksLOL](https://x.com/TwoWeeksLOL/status/2110335371360002479) |
| 3-20 | 多个 bot 组成产品团队优化个人网站 | 作者建了产品、设计、开发、测试、增长各一个 bot，拉进一个群。产品拆需求，测试先写用例，开发照着修，增长 bot 还提了 SEO 建议。作者只负责拍板。 | 5赞 | ★★★☆☆ | [@ai_edisonZ](https://x.com/ai_edisonZ/status/2110272456552292566) |
| 3-21 | 断网时自己写了个 Telegram 客户端 | 飞机上的 Wi-Fi 只能发消息，bot 就给自己写了一个 Telegram 客户端，好继续和作者联系。这是个趣闻，说明 bot 能自己动手解决问题。 | 4赞 | ★★☆☆☆ | [@carlosnoriega](https://x.com/carlosnoriega/status/2109064450838044827) |
| 3-22 | SpaceXAI 用 Grok Bot 开发 Grok Bot | 转述的说法是团队里的 Lauren 一个月出了 2500 个 PR。这条是转述，不是亲测，作为参考。 | 33赞 | ★★☆☆☆ | [@0xGenAi](https://x.com/0xGenAi/status/2110140342658019616) |
| 3-23 | 修好云电脑断网 | bot 的云电脑断了网，作者用另一个 agent 在终端里排查，发现是走本机代理时 TLS 握手失败，最后让 Chrome 绕开代理解决了。这是运维排障的经验。 | — | ★★☆☆☆ | [@justic_hot](https://x.com/justic_hot/status/2110281758944149731) |

[← 返回目录](../README.md)
