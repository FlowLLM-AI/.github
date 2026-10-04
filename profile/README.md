<p align="center">
  <img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/main/assets/flowllm-banner.png" alt="FlowLLM-AI: AxonX, FlowLLM, and Finance-MCP" width="1200" />
</p>

<p align="center"><strong>Let agents run traceable financial research.</strong></p>

<p align="center">
  <a href="https://github.com/FlowLLM-AI/AxonX"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/308887bd066da38e3a998a467e586fe8d68b0e86/assets/badges/axonx.svg" alt="AxonX" height="28" /></a>
  <a href="https://flowllm-ai.github.io/AxonX/en/"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/308887bd066da38e3a998a467e586fe8d68b0e86/assets/badges/docs-en.svg" alt="Documentation" height="28" /></a>
  <a href="https://flowllm-ai.github.io/AxonX/playground/?lang=en"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/308887bd066da38e3a998a467e586fe8d68b0e86/assets/badges/studio-en.svg" alt="Try Studio" height="28" /></a>
  <a href="https://github.com/FlowLLM-AI/AxonX/discussions"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/308887bd066da38e3a998a467e586fe8d68b0e86/assets/badges/community-en.svg" alt="Community" height="28" /></a>
  <a href="https://github.com/FlowLLM-AI/.github/blob/main/profile/README_ZH.md"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/308887bd066da38e3a998a467e586fe8d68b0e86/assets/badges/language-en.svg" alt="简体中文" height="28" /></a>
</p>

**AxonX is our main entry point:** connect your agent to quantitative research Tasks,
follow execution in Studio, and inspect parameters, logs, artifacts, and dependencies in one workspace.
FlowLLM provides configurable LLM application workflows; Finance-MCP provides financial research tools for MCP clients.

## Start here

| Your goal | First step |
| --- | --- |
| Explore the research workspace without installing anything | [Try AxonX Studio](https://flowllm-ai.github.io/AxonX/playground/?lang=en) with simulated data and execution. |
| Run quantitative research locally | Follow the [AxonX quick start](https://flowllm-ai.github.io/AxonX/en/getting-started/quickstart); install research plugins for your tasks. |
| Connect a coding agent to research tasks | Load the [AxonX Skill](https://github.com/FlowLLM-AI/AxonX/blob/main/skills/axonx/SKILL.md), then follow the [agent integration guide](https://flowllm-ai.github.io/AxonX/en/agent/external). |
| Add financial search and data tools to an MCP client | Start with [Finance-MCP setup](https://github.com/FlowLLM-AI/finance-mcp#-quick-start). |
| Build and serve your own LLM workflows | Start with the [FlowLLM quick start](https://github.com/FlowLLM-AI/flowllm/blob/main/docs/en/quick_start.md). |

**Latest release:** [AxonX v0.1.0](https://github.com/FlowLLM-AI/AxonX/releases/tag/v0.1.0)
(October 4, 2026), with research Tasks, execution tracking, artifact lineage, and Studio.

## Why FlowLLM-AI?

- **Agent execution you can inspect.** AxonX exposes research Tasks through CLI and MCP, while Studio shows execution records and results.
- **Traceable research evidence.** Keep task parameters, logs, artifacts, and upstream dependencies across ETL, training, prediction, and backtesting.
- **Research methods you can extend.** Add independently installed AxonX plugins with explicit Task inputs and outputs.
- **Tools for different jobs.** Use FlowLLM to compose and serve LLM workflows, or Finance-MCP to connect financial search and data tools to MCP clients.

## Explore our projects

| Project | What it does | Start here |
| --- | --- | --- |
| **[AxonX](https://github.com/FlowLLM-AI/AxonX)** | An agent-native quantitative research harness with plugin-based Tasks, traceable artifacts, and a browser Studio. | [Quick start](https://flowllm-ai.github.io/AxonX/en/getting-started/quickstart) · [Agent integration](https://flowllm-ai.github.io/AxonX/en/agent/external) |
| **[FlowLLM](https://github.com/FlowLLM-AI/flowllm)** | A configuration-driven LLM application framework for composing workflows and serving Jobs over HTTP or MCP. | [Quick start](https://github.com/FlowLLM-AI/flowllm/blob/main/docs/en/quick_start.md) · [Development skill](https://github.com/FlowLLM-AI/flowllm/blob/main/skills/flowllm_dev/SKILL.md) |
| **[Finance-MCP](https://github.com/FlowLLM-AI/finance-mcp)** | A financial research toolkit and MCP server built on FlowLLM, integrating search, crawling, and financial data. | [Setup and tools](https://github.com/FlowLLM-AI/finance-mcp#-quick-start) |

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
