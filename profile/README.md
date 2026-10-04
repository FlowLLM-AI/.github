<p align="center">
  <img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/main/assets/flowllm-banner.svg" alt="FlowLLM-AI: AxonX, FlowLLM, and Finance-MCP" width="1200" />
</p>

<p align="center"><strong>Open-source tools for agent workflows and financial research.</strong></p>

<p align="center">
  <a href="https://flowllm-ai.github.io/AxonX/en/">AxonX Docs</a> ·
  <a href="https://flowllm-ai.github.io/AxonX/playground/?lang=en">Try AxonX Studio</a> ·
  <a href="https://github.com/FlowLLM-AI/AxonX/discussions">Community</a> ·
  <a href="https://github.com/FlowLLM-AI/.github/blob/main/profile/README_ZH.md">简体中文</a>
</p>

We build tools for developers and researchers to turn ideas into executable workflows,
connect agents to research capabilities, and inspect the results.

## Why FlowLLM-AI?

- **Build reusable workflows.** FlowLLM composes configurable Jobs, Steps, and Components and exposes them through HTTP or MCP.
- **Give agents research tools.** Finance-MCP brings web search, crawling, and financial data tools to MCP clients.
- **Make quantitative research traceable.** AxonX records task parameters, logs, artifacts, and dependencies across data processing, factor analysis, training, prediction, and backtesting.
- **Work through your preferred interface.** AxonX offers CLI, HTTP, MCP, and Studio access to the same research workspace, with plugins for extending research Tasks.

## Explore our projects

| Project | What it does | Start here |
| --- | --- | --- |
| **[AxonX](https://github.com/FlowLLM-AI/AxonX)** | An agent-native quantitative research harness with plugin-based Tasks, traceable artifacts, and a browser Studio. | [Quick start](https://flowllm-ai.github.io/AxonX/en/getting-started/quickstart) · [Agent integration](https://flowllm-ai.github.io/AxonX/en/agent/external) |
| **[FlowLLM](https://github.com/FlowLLM-AI/flowllm)** | A configuration-driven LLM application framework for composing workflows and serving Jobs over HTTP or MCP. | [Quick start](https://github.com/FlowLLM-AI/flowllm/blob/main/docs/en/quick_start.md) · [Development skill](https://github.com/FlowLLM-AI/flowllm/blob/main/skills/flowllm_dev/SKILL.md) |
| **[Finance-MCP](https://github.com/FlowLLM-AI/finance-mcp)** | A financial research toolkit and MCP server built on FlowLLM, integrating search, crawling, and financial data. | [Setup and tools](https://github.com/FlowLLM-AI/finance-mcp#-quick-start) |

**Choose a starting point:** use AxonX for quantitative experiments, Finance-MCP for financial research tools,
or FlowLLM to build your own LLM application workflows.

## How the projects fit together

- **FlowLLM → Finance-MCP:** Finance-MCP uses FlowLLM to compose and serve financial research tools.
- **AxonX:** a quantitative research harness with its own Task and artifact contracts. Use it through CLI / HTTP / MCP / Studio to run experiments and inspect results.
- **Agents and developers:** choose the appropriate tool for the task. Finance-MCP and AxonX provide distinct research capabilities; they do not require a combined deployment.

## Try AxonX Studio

[Open the browser Playground](https://flowllm-ai.github.io/AxonX/playground/?lang=en) to explore the interface with
**simulated data and execution**. No local installation is needed for the Playground.

<p align="center">
  <a href="https://flowllm-ai.github.io/AxonX/playground/?lang=en">
    <img src="https://raw.githubusercontent.com/FlowLLM-AI/AxonX/main/docs/figures/studio/home.png" alt="AxonX Studio: research workspace, tasks, and artifacts" width="900" />
  </a>
</p>

For real research, follow the [AxonX quick start](https://flowllm-ai.github.io/AxonX/en/getting-started/quickstart).
Research plugins are installed separately; market data and model services may require API credentials.

## See an agent-driven research case

**Alpha158 Enhanced** shows how a coding agent developed a separate research plugin and used AxonX to execute
ETL → training → prediction → backtesting, then compare a baseline with a locked feature configuration.

Start with the [benchmark overview](https://github.com/FlowLLM-AI/AxonX#benchmark-agent-developed-market-cross-sectional-features),
then inspect the [reproduction guide](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/a158_enhanced/README.md)
and [experiment results](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/a158_enhanced/EXPERIMENT_RESULTS.md).
The report includes screening and confirmation windows, portfolio-size comparisons, and uncertainty analysis.
Confirmation-period improvements were not uniform across portfolio sizes, and the reported 95% intervals for daily
paired increments include zero; stable gains remain unproven.

To connect a coding agent to your own research, start with the
[AxonX Skill](https://github.com/FlowLLM-AI/AxonX/blob/main/skills/axonx/SKILL.md) and
[external-agent guide](https://flowllm-ai.github.io/AxonX/en/agent/external).

## Get involved

- **Community and usage help:** join [GitHub Discussions](https://github.com/FlowLLM-AI/AxonX/discussions). Use [Q&A](https://github.com/FlowLLM-AI/AxonX/discussions/categories/q-a) for usage questions, [Ideas](https://github.com/FlowLLM-AI/AxonX/discussions/categories/ideas) for proposals, and [Show and tell](https://github.com/FlowLLM-AI/AxonX/discussions/categories/show-and-tell) for examples. English and Chinese are welcome.
- **Bug reports and concrete feature requests:** open an issue in [AxonX](https://github.com/FlowLLM-AI/AxonX/issues), [FlowLLM](https://github.com/FlowLLM-AI/flowllm/issues), or [Finance-MCP](https://github.com/FlowLLM-AI/finance-mcp/issues).
- **Contribute:** improve documentation, add research plugins or tools, or fix bugs. Start with the [AxonX contribution guide](https://github.com/FlowLLM-AI/AxonX/blob/main/CONTRIBUTING.md) or [FlowLLM contribution guide](https://github.com/FlowLLM-AI/flowllm/blob/main/docs/en/contributing.md).
- **Follow our work:** star the project you use and watch its repository for updates.
