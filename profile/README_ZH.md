<p align="center">
  <img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/main/assets/flowllm-banner.png" alt="FlowLLM-AI: AxonX, FlowLLM, and Finance-MCP" width="1200" />
</p>

<p align="center"><strong>让 Agent 执行可追溯的金融研究。</strong></p>

<p align="center">
  <a href="https://github.com/FlowLLM-AI/AxonX"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/d0c8cbaf82a3c995bb6f9a4bf010892813da0a08/assets/badges/axonx.svg" alt="AxonX" height="28" /></a>
  <a href="https://flowllm-ai.github.io/AxonX/zh/"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/d0c8cbaf82a3c995bb6f9a4bf010892813da0a08/assets/badges/docs-zh.svg" alt="文档" height="28" /></a>
  <a href="https://flowllm-ai.github.io/AxonX/playground/?lang=zh"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/d0c8cbaf82a3c995bb6f9a4bf010892813da0a08/assets/badges/studio-zh.svg" alt="体验 Studio" height="28" /></a>
  <a href="https://github.com/FlowLLM-AI/AxonX/discussions"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/d0c8cbaf82a3c995bb6f9a4bf010892813da0a08/assets/badges/community-zh.svg" alt="社区" height="28" /></a>
  <a href="https://github.com/FlowLLM-AI/.github/blob/main/profile/README.md"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/d0c8cbaf82a3c995bb6f9a4bf010892813da0a08/assets/badges/language-zh.svg" alt="English" height="28" /></a>
</p>

**AxonX 是我们的主要入口：** 让 Agent 调用量化研究 Task，在 Studio 跟踪执行，
并在同一工作区检查参数、日志、产物和依赖关系。
FlowLLM 提供配置驱动的 LLM 应用工作流；Finance-MCP 为 MCP 客户端提供金融研究工具。

## 从这里开始

| 你的目标 | 第一步 |
| --- | --- |
| 无需安装，先了解研究工作区 | [体验 AxonX Studio](https://flowllm-ai.github.io/AxonX/playground/?lang=zh)，使用模拟数据和模拟执行。 |
| 在本地运行量化研究 | 按照 [AxonX 快速开始](https://flowllm-ai.github.io/AxonX/zh/getting-started/quickstart)安装，并为研究任务安装相应插件。 |
| 让编码 Agent 调用研究任务 | 加载 [AxonX Skill](https://github.com/FlowLLM-AI/AxonX/blob/main/skills/axonx/SKILL.md)，再阅读 [Agent 接入指南](https://flowllm-ai.github.io/AxonX/zh/agent/external)。 |
| 为 MCP 客户端接入金融搜索和数据工具 | 阅读 [Finance-MCP 配置指南](https://github.com/FlowLLM-AI/finance-mcp/blob/main/README_ZH.md)。 |
| 构建并提供自己的 LLM 工作流服务 | 阅读 [FlowLLM 快速开始](https://github.com/FlowLLM-AI/flowllm/blob/main/docs/zh/quick_start.md)。 |

**最新发布：** [AxonX v0.1.0](https://github.com/FlowLLM-AI/AxonX/releases/tag/v0.1.0)
（2026 年 10 月 4 日），提供研究 Task、执行跟踪、产物依赖追溯和 Studio。

## 为什么选择 FlowLLM-AI？

- **Agent 执行，研究者检查。** AxonX 通过 CLI 和 MCP 提供研究 Task，Studio 展示执行记录与结果。
- **研究证据可追溯。** 在 ETL、训练、预测和回测过程中保留任务参数、日志、产物和上游依赖。
- **研究方法可扩展。** 通过独立安装的 AxonX 插件增加研究方法，显式声明 Task 输入和输出。
- **按用途选择工具。** FlowLLM 用于组合和提供 LLM 工作流服务；Finance-MCP 将金融搜索与数据工具接入 MCP 客户端。

## 探索我们的项目

| 项目 | 用途 | 从这里开始 |
| --- | --- | --- |
| **[AxonX](https://github.com/FlowLLM-AI/AxonX)** | 面向 Agent 的量化研究 Harness，提供插件式 Task、可追溯产物和浏览器 Studio。 | [快速开始](https://flowllm-ai.github.io/AxonX/zh/getting-started/quickstart) · [Agent 集成](https://flowllm-ai.github.io/AxonX/zh/agent/external) |
| **[FlowLLM](https://github.com/FlowLLM-AI/flowllm)** | 配置驱动的 LLM 应用框架，用于组合工作流，并通过 HTTP 或 MCP 提供 Job 服务。 | [快速开始](https://github.com/FlowLLM-AI/flowllm/blob/main/docs/zh/quick_start.md) · [开发 Skill](https://github.com/FlowLLM-AI/flowllm/blob/main/skills/flowllm_dev/SKILL.md) |
| **[Finance-MCP](https://github.com/FlowLLM-AI/finance-mcp)** | 基于 FlowLLM 的金融研究工具集与 MCP 服务，集成搜索、抓取和金融数据。 | [配置与工具说明](https://github.com/FlowLLM-AI/finance-mcp/blob/main/README_ZH.md) |

## 项目之间是什么关系？

- **FlowLLM → Finance-MCP：** Finance-MCP 使用 FlowLLM 组合金融研究工具并提供服务。
- **AxonX：** 量化研究 Harness，提供自己的 Task 与产物契约，通过 CLI / HTTP / MCP / Studio 运行实验和检查结果。
- **Agent 与开发者：** 根据任务选择工具。Finance-MCP 与 AxonX 提供不同的研究能力，无需部署成一套系统即可分别使用。

## 体验 AxonX Studio

打开 [浏览器 Playground](https://flowllm-ai.github.io/AxonX/playground/?lang=zh)，通过**模拟数据和模拟执行**体验界面，无需在本地安装。

<p align="center">
  <a href="https://flowllm-ai.github.io/AxonX/playground/?lang=zh">
    <img src="https://raw.githubusercontent.com/FlowLLM-AI/AxonX/main/docs/figures/studio/home.png" alt="AxonX Studio：研究工作区、任务与产物" width="900" />
  </a>
</p>

实际研究请按照 [AxonX 快速开始](https://flowllm-ai.github.io/AxonX/zh/getting-started/quickstart)部署。
研究插件需单独安装；行情数据和模型服务可能需要 API 凭据。

## 查看 Agent 驱动的研究案例

**Alpha158 Enhanced** 展示了编码 Agent 如何开发独立研究插件，通过 AxonX 执行
ETL → 训练 → 预测 → 回测，并比较基线与锁定的特征配置。

先阅读 [案例概览](https://github.com/FlowLLM-AI/AxonX/blob/main/README_ZH.md#benchmark-agent-%E5%BC%80%E5%8F%91%E5%B8%82%E5%9C%BA%E6%A8%AA%E6%88%AA%E9%9D%A2%E5%A2%9E%E5%BC%BA%E7%89%B9%E5%BE%81)，
再查看 [复现指南](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/a158_enhanced/README_ZH.md)
和 [完整实验结果](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/a158_enhanced/EXPERIMENT_RESULTS.md)。
报告包含筛选与确认窗口、不同持仓数量的对比和不确定性分析。确认期改善未覆盖所有持仓数量，
日配对增量的 95% 区间均包含零，尚不能证明收益稳定提升。

如果希望让编码 Agent 参与自己的研究，从
[AxonX Skill](https://github.com/FlowLLM-AI/AxonX/blob/main/skills/axonx/SKILL.md)
和 [外部 Agent 指南](https://flowllm-ai.github.io/AxonX/zh/agent/external)开始。

## 参与共建

- **社区交流与使用帮助：** 进入 [GitHub Discussions](https://github.com/FlowLLM-AI/AxonX/discussions)，在 [Q&A](https://github.com/FlowLLM-AI/AxonX/discussions/categories/q-a) 提问，在 [Ideas](https://github.com/FlowLLM-AI/AxonX/discussions/categories/ideas) 分享建议，在 [Show and tell](https://github.com/FlowLLM-AI/AxonX/discussions/categories/show-and-tell) 展示案例。欢迎中英文交流。
- **缺陷报告与具体功能请求：** 在对应项目提交 Issue：[AxonX](https://github.com/FlowLLM-AI/AxonX/issues)、[FlowLLM](https://github.com/FlowLLM-AI/flowllm/issues)、[Finance-MCP](https://github.com/FlowLLM-AI/finance-mcp/issues)。
- **贡献代码与内容：** 改进文档、开发研究插件或工具、修复缺陷。先阅读 [AxonX 贡献指南](https://github.com/FlowLLM-AI/AxonX/blob/main/CONTRIBUTING_ZH.md)或 [FlowLLM 贡献指南](https://github.com/FlowLLM-AI/flowllm/blob/main/docs/zh/contributing.md)。
- **关注进展：** 为你使用的项目点 Star，并通过 Watch 关注仓库更新。
