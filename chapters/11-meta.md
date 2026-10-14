# 模板、目录和教程

找模板、读教程、搭第一个 bot 的入口。先读官方文档和安全清单，再去模板目录里挑低权限的模板改。

本章共 16 条，按推荐程度从高到低排列，低分条目也保留。

| 编号 | 用法 | 做法与价值 | 热度 | 推荐程度 | 来源 |
| --- | --- | --- | --- | --- | --- |
| 11-1 | dr eggbot：先问几个问题再替你设计 bot | poteto 做的元模板，收录在官方市场。它先问你几个偏好问题，再设计一个结构完整的 bot 并直接创建出来。适合不知道 bot 的职责、来源、审批边界该怎么写的人。拿它生成第一版，再自己改，比从空白开始快得多。 | 官方市场 | ★★★★★ | [@poteto](https://x.ai/bot/_jOdbfkB16zxu7MRcmReE) |
| 11-2 | awesome-grok-bot-templates：4500 多个模板的总目录 | 这个仓库按用途整理了 4537 个公开的 Grok Bot 模板链接，每个都标了权限等级（不连账号、连账号、可动钱或发布删除）和运行频率。配套网站 botsdots.site 可以按分类、应用和权限筛选。找现成模板时先查这里，比在 X 上翻快很多。权限标注能帮你优先挑低风险的。 | GitHub | ★★★★★ | [Maimuzamilhu](https://github.com/Maimuzamilhu/awesome-grok-bot-templates) |
| 11-3 | Alfred：审计整个 bot 组织 | 官方市场模板，负责设计、审计和治理你的整套 bot，让每个 bot 都对应真实目标，有明确的人类负责人，没有重复岗位。bot 一多就容易职责重叠、互相踩额度，这个模板专门解决这个问题。它的权限评级是最高一档（可发布或删除），用前要看清它会改什么。 | 官方市场 | ★★★★☆ | [@heyrobinai](https://x.ai/bot/p7Gh6HIrfv4AGzIow6-9X) |
| 11-4 | awesome-grok-bot（中英双语资源表） | 收录 Grok Bot 相关资源的双语清单，423 星，覆盖教程、模板、插件和社区实录。适合中文读者入门。和模板总目录配合用：一个找资源，一个找配置。 | 423★ | ★★★★☆ | [RongleCat](https://github.com/RongleCat/awesome-grok-bot) |
| 11-5 | grokbot-field-notes：官方团队 72 小时直播搭建的规则和失败记录 | 把官方团队 72 小时直播搭建过程整理成仓库：规则、playbook、bot 角色和失败日志，可以直接放进 AGENTS.md。作者在 ericzakariasson 的征集帖里分享了它。失败日志尤其有用，能少走弯路。适合想搭多 bot 团队的人。 | 594★ | ★★★★☆ | [unicodef1wn](https://github.com/unicodef1wn/grokbot-field-notes) |
| 11-6 | Grok Bot 橙皮书：从入门到多智能体协作 | 中文长篇教程，书名《把一支 AI 团队装进口袋》，覆盖入门、多智能体协作、Routine、省钱与自动化。作者在 X 上也分享过飞书接入教程。适合想系统读一遍的中文用户。 | 165★ | ★★★★☆ | [KinGao294](https://github.com/KinGao294/grok-bot-orange-book) |
| 11-7 | 中文上手指南：先画边界再干活 | 中文博客强调 Grok Bot 是一台云端 Linux 电脑加一群同事，所有 bot 共用一台电脑、共享登录态，屏幕分开但安全边界不分开。建议先设审批，遇到密码、验证码、付款时让 bot 交还控制权。有插件的服务优先用插件，比让它点网页稳。 | 中文博客 | ★★★★☆ | [zhanghe.dev](https://zhanghe.dev/zh-CN/posts/7-grok-bot-20260828) |
| 11-8 | 官方文档：先做一次，存成 skill，再排进 routine | 官方文档建议从一次性任务开始，做稳之后把方法存成 skill，最后才排成定时 routine。也可以用“Teach a task”把浏览器操作演示一遍（最长 10 分钟），让 bot 生成 skill 草稿，再补决策规则和失败处理。这是所有 routine 用法的基础流程。 | 官方文档 | ★★★★☆ | [Cursor Docs](https://cursor.com/docs/grok-bot/work.md) |
| 11-9 | awesome-grokbot：1894 个分享链接逐条核验 | 另一个模板目录，每条链接都检查过是否可用，每行都注明作者，中英双语。规模比上一份小，但核验更严。可以和 4500 条那份互相对照。 | 355★ | ★★★☆☆ | [kydlikebtc](https://github.com/kydlikebtc/awesome-grokbot) |
| 11-10 | awesome-grok-bot：4380 个分享链接按档位分级 | 按“书架档位”分级整理 4380 个 x.ai/bot 分享链接，带可搜索的网页。作者强调不是简单堆提示词。适合想看哪些模板被认为更成熟的人。 | 66★ | ★★★☆☆ | [majiayu000](https://github.com/majiayu000/awesome-grok-bot) |
| 11-11 | grok-bot-cli：命令行管理 bot 和群组 | 命令行工具，能创建和更新 bot、发消息、查看会话，并自动清理。适合想用脚本批量管理 bot 的人。bot 数量多时比手动点界面省事。 | 102★ | ★★★☆☆ | [ScriptedAlchemy](https://github.com/ScriptedAlchemy/grok-bot-cli) |
| 11-12 | 26 个模板拆解：重点学它们怎么写任务 | 小互的 AI 解读站拆了 26 个公开模板，包括 dr eggbot、mattyp 的一组模板、Lenny 的 Lennybot 等，按“直接交付、工程外循环、监控与判断、个人事务”分类，附中英提示词原文。价值在于学写法，而不只是抄模板。 | 中文博客 | ★★★☆☆ | [best.xiaohu.ai](https://best.xiaohu.ai/article/grok-bot-templates-26/) |
| 11-13 | 293 个公开例子和 30 个可抄提示词 | ayautomate 收集了 293 条帖子、视频和仓库，分九类用例，并给出 30 个只起草不发送的提示词。还记录了一个反面例子：有人群发时把客户地址都放进了收件人栏。适合作为英文入门索引。 | 博客 | ★★★☆☆ | [ayautomate](https://www.ayautomate.com/grok-bot-examples) |
| 11-14 | usegrokbot：可搜索的用例和提示词库 | 收集 Grok Bot 用例、提示词和工作流的可搜索库。规模不大。可以当补充检索源。 | 18★ | ★★☆☆☆ | [a70win-wq](https://github.com/a70win-wq/usegrokbot) |
| 11-15 | eze-grokbot：一个人公开的全部 bot 配置 | 作者把自己的每个 bot 配置放在一个文件夹里公开。看真实用户的完整配置，比看单条推文更容易理解怎么写职责和边界。适合抄结构。 | 11★ | ★★☆☆☆ | [eze-is](https://github.com/eze-is/eze-grokbot) |
| 11-16 | 开源替代品：rakazo、OpenMausBot、open-dots 等 | GitHub 上有一批自称 Grok Bot 开源替代的项目，比如 rakazo（可选模型和沙箱，约 4000 星）、OpenMausBot（自带虚拟机，约 4900 星）、open-dots（约 5800 星）。它们说明了社区最看重的能力：常驻电脑、多 bot、审批。想自托管或换模型时可以看看。不能直接当 Grok Bot 用。 | GitHub | ★★☆☆☆ | [elie222](https://github.com/elie222/rakazo) |

[← 返回目录](../README.md)
