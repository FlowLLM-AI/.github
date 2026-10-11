<p align="center">
  <a href="https://github.com/FlowLLM-AI/AxonX">
    <img src="https://raw.githubusercontent.com/FlowLLM-AI/AxonX/main/axonx_studio/public/axonx-logo.svg" alt="AxonX" width="560" />
  </a>
</p>

<p align="center"><strong>从研究 Prompt 到量化代码，再到可追溯的实验。</strong></p>

<p align="center">
  <a href="https://github.com/FlowLLM-AI/AxonX"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/axonx.svg" alt="AxonX" height="28" /></a>
  <a href="https://flowllm-ai.github.io/AxonX/zh/"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/docs-zh.svg" alt="文档" height="28" /></a>
  <a href="https://flowllm-ai.github.io/AxonX/playground/?lang=zh"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/studio-zh.svg" alt="体验 Studio" height="28" /></a>
  <a href="https://github.com/FlowLLM-AI/AxonX/discussions"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/community-zh.svg" alt="社区" height="28" /></a>
  <a href="https://github.com/FlowLLM-AI/.github/blob/main/profile/README.md"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/language-zh.svg" alt="English" height="28" /></a>
</p>

**FlowLLM-AI 以 AxonX 为核心，构建面向 Agent 的量化研究 Harness。** 将研究 Prompt 与
[AxonX Skill](https://github.com/FlowLLM-AI/AxonX/blob/main/skills/axonx/SKILL.md) 结合，让外部或内置 Agent
开发研究插件、执行实验、检查结果，持续迭代因子、模型与组合策略。

**用户提出研究问题，Agent 实现量化逻辑，AxonX 管理执行与证据。**

## 从 AxonX 开始

| 你的目标 | 第一步 |
| --- | --- |
| 无需安装，先体验研究工作区 | [打开 Studio Playground](https://flowllm-ai.github.io/AxonX/playground/?lang=zh)，使用模拟数据和模拟执行。 |
| 在本地运行第一个实验 | 阅读[快速开始](https://flowllm-ai.github.io/AxonX/zh/getting-started/quickstart)。内置 demo 无需行情或模型凭据。 |
| 让 Agent 开发或改进量化代码 | 加载 [AxonX Skill](https://github.com/FlowLLM-AI/AxonX/blob/main/skills/axonx/SKILL.md)，描述研究目标，再阅读 [Agent 接入指南](https://flowllm-ai.github.io/AxonX/zh/agent/external)。 |
| 开发新的研究插件 | 阅读[开发指南](https://github.com/FlowLLM-AI/AxonX/blob/main/docs/zh/dev_guide.md)，了解 Task 契约与产物兼容要求。 |

本地执行支持 **macOS / Linux，要求 Python 3.12+**。研究插件需从源码单独安装到所选执行服务的环境中，
详见[插件管理](https://flowllm-ai.github.io/AxonX/zh/plugins/management)。

## 从研究 Prompt 到实验依据

1. **开发量化代码。** 使用外部编码 Agent 或 Studio 内置 Agent，创建或改进研究插件。
2. **执行实验。** 查询带类型的 Task 输入输出，提交任务、跟踪进度与日志，或取消 Run。
3. **分析并迭代。** 比较配置、指标、模型、预测与回测，保留 Task/Run ID 和上游依赖。

CLI、HTTP、MCP 和 **AxonX Studio** 通过共享的 Job 提交、查询 Task。选定的本机或远程执行服务
运行插件代码，并将研究证据保存在自己的工作区。

## 研究插件：从 Qlib Alpha158 开始扩展

当前参考工作流将 **Microsoft Qlib 的 Alpha158 基线**适配为 **ETL → 训练 → 预测 → 回测**，
因子分析从 ETL 独立分支。插件逐层复用兼容实现与产物：

| 插件 | 可以探索什么 |
| --- | --- |
| [qlib_a158](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/qlib_a158/README_ZH.md) | 158 个价量特征、LightGBM 训练、因子分析与 TopN 回测。 |
| [qlib_factor](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/qlib_factor/README_ZH.md) | 13 个可选的市场矩、中性动量与风险特征；训练默认仍使用 158 个基线特征。 |
| [qlib_strategy](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/qlib_strategy/README_ZH.md) | 最短持仓期、排名保留与换仓数量限制，复用预测产物，无需重新训练。 |

Agent 可以改进这些插件，也可以通过同一套 Harness 契约实现其他研究方法。

## 体验 AxonX Studio

打开[浏览器 Playground](https://flowllm-ai.github.io/AxonX/playground/?lang=zh)，通过**模拟数据和模拟执行**
体验 Task 与研究图表，无需在本地安装。

<p align="center">
  <a href="https://flowllm-ai.github.io/AxonX/playground/?lang=zh">
    <img src="https://raw.githubusercontent.com/FlowLLM-AI/AxonX/main/docs/figures/studio/home.png" alt="AxonX Studio：Agent、研究任务与产物" width="900" />
  </a>
</p>

真实实验需要部署 AxonX 并安装研究插件。Studio 支持使用内置 Agent、检查任务血缘与研究产物，
以及选择本机或远程执行服务。行情数据和模型服务可能需要 API 凭据。

## 研究案例：因子与持仓策略

当前 Alpha158 案例比较适配后的基线、增加两个风险因子的模型，以及复用因子模型预测的排名保留策略。
2026 年 10 月 10 日重跑结果如下：

| 配置 | Top20 净年化收益 | 净 Sharpe | 日均双边换手率 |
| --- | ---: | ---: | ---: |
| Alpha158 基线 | 7.67% | 0.3619 | 198.83% |
| 风险因子模型 | 9.03% | 0.4052 | 199.35% |
| 排名保留策略 | 32.37% | 1.1575 | 40.01% |

训练窗口为 `[20150101,20230101)`，评估覆盖 `20230103–20261008`（909 个交易日），买入 / 卖出费率为
0.05% / 0.15%。这些结果来自适配后的 AxonX 实验：没有独立确认窗口，模型设置差异未隔离新增因子的效果，
三组回测均报告 `incomplete_market_data`；成交使用同收盘价代理，2026 年仅覆盖部分年份。

查看[完整配置、证据边界、复现命令与 Task 来源](https://github.com/FlowLLM-AI/AxonX/blob/main/docs/zh/research/alpha158-case.md)。

## 最新进展

- **最新发布版本：** [AxonX v0.1.2](https://github.com/FlowLLM-AI/AxonX/releases/tag/v0.1.2)，发布于 2026 年 10 月 10 日。
- **当前 main 分支：** Agent 默认加载开发指南，改进工具参数流式展示与 Studio 任务视图，
  并提供鉴权服务自更新 Job 和重启操作。可用条件与恢复行为见[更新指南](https://github.com/FlowLLM-AI/AxonX/blob/main/docs/zh/guides/self-update.md)。

## 加入 AxonX 社区

- **问题、想法与研究案例：** 进入 [GitHub Discussions](https://github.com/FlowLLM-AI/AxonX/discussions)，欢迎中英文交流。
- **缺陷与具体功能请求：** 提交 [AxonX Issue](https://github.com/FlowLLM-AI/AxonX/issues)。
- **参与贡献：** 改进文档、开发研究插件或修复缺陷，从[贡献指南](https://github.com/FlowLLM-AI/AxonX/blob/main/CONTRIBUTING_ZH.md)开始。
- **关注进展：** [为 AxonX 点 Star](https://github.com/FlowLLM-AI/AxonX)，并通过 Watch 关注仓库更新。

## FlowLLM-AI 的其他项目

[FlowLLM](https://github.com/FlowLLM-AI/flowllm) 提供配置驱动的 LLM 应用工作流。
[Finance-MCP](https://github.com/FlowLLM-AI/finance-mcp) 基于 FlowLLM，为 MCP 客户端提供金融搜索、抓取与数据工具。
按研究需要选用。
