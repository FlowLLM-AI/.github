<p align="center">
  <img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/main/assets/flowllm-banner.png" alt="FlowLLM-AI: AxonX, FlowLLM, and Finance-MCP" width="1200" />
</p>

<p align="center"><strong>Turn research prompts into quantitative code and traceable experiments.</strong></p>

<p align="center">
  <a href="https://github.com/FlowLLM-AI/AxonX"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/axonx.svg" alt="AxonX" height="28" /></a>
  <a href="https://flowllm-ai.github.io/AxonX/en/"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/docs-en.svg" alt="Documentation" height="28" /></a>
  <a href="https://flowllm-ai.github.io/AxonX/playground/?lang=en"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/studio-en.svg" alt="Try Studio" height="28" /></a>
  <a href="https://github.com/FlowLLM-AI/AxonX/discussions"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/community-en.svg" alt="Community" height="28" /></a>
  <a href="https://github.com/FlowLLM-AI/.github/blob/main/profile/README_ZH.md"><img src="https://raw.githubusercontent.com/FlowLLM-AI/.github/046a224ee443014b7aaaadabf1f7dea1e3a7a53a/assets/badges/language-en.svg" alt="简体中文" height="28" /></a>
</p>

**FlowLLM-AI builds AxonX, an agent-native harness for quantitative research.** Combine your research prompt with the
[AxonX Skill](https://github.com/FlowLLM-AI/AxonX/blob/main/skills/axonx/SKILL.md) and let an external or built-in Agent
develop a research plugin, run experiments, inspect results, and iterate on factors, models, and portfolio strategies.

**You define the research question; the Agent implements it; AxonX manages execution and evidence.**

## Start with AxonX

| Your goal | First step |
| --- | --- |
| Explore without installing anything | [Try Studio Playground](https://flowllm-ai.github.io/AxonX/playground/?lang=en), using simulated data and execution. |
| Run your first local experiment | Follow the [quick start](https://flowllm-ai.github.io/AxonX/en/getting-started/quickstart). The built-in demo needs no market-data or model credentials. |
| Develop or improve quantitative code with an Agent | Load the [AxonX Skill](https://github.com/FlowLLM-AI/AxonX/blob/main/skills/axonx/SKILL.md), describe your research objective, and follow the [Agent integration guide](https://flowllm-ai.github.io/AxonX/en/agent/external). |
| Build a new research plugin | Read the [development guide](https://github.com/FlowLLM-AI/AxonX/blob/main/docs/en/dev_guide.md) for Task contracts and compatible artifacts. |

Local execution supports **Python 3.12+ on macOS and Linux**. Research plugins are installed separately from source
in the selected execution service's environment; see [plugin management](https://flowllm-ai.github.io/AxonX/en/plugins/management).

## From research prompt to experiment evidence

1. **Develop quantitative code.** Use an external coding Agent or Studio's built-in Agent to create or improve plugins.
2. **Execute experiments.** Discover typed Task inputs and outputs, submit work, follow progress and logs, or cancel Runs.
3. **Inspect and iterate.** Compare configurations, metrics, models, predictions, and backtests, with Task/Run IDs and upstream dependencies.

CLI, HTTP, MCP, and **AxonX Studio** share Jobs for submitting and querying Tasks. A selected local or remote execution
service runs the plugin code and keeps the research evidence in its workspace.

## Research plugins: Qlib Alpha158 and beyond

The current reference workflow adapts **Microsoft Qlib's Alpha158 baseline** into **ETL → Train → Predict → Backtest**,
with factor analysis branching from ETL. Plugins reuse compatible implementations and artifacts:

| Plugin | What you can explore |
| --- | --- |
| [qlib_a158](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/qlib_a158/README.md) | 158 price/volume features, LightGBM training, factor analysis, and TopN backtests. |
| [qlib_factor](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/qlib_factor/README.md) | 13 optional market-moment, neutral-momentum, and risk features; training defaults to the 158 baseline features. |
| [qlib_strategy](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/qlib_strategy/README.md) | Minimum holding periods, rank retention, and replacement limits, reusing predictions without retraining. |

Agents can improve these plugins or implement other research methods through the same Harness contracts.

## Explore AxonX Studio

[Open the browser Playground](https://flowllm-ai.github.io/AxonX/playground/?lang=en) to explore Tasks and research charts
with **simulated data and execution**. No local installation is needed.

<p align="center">
  <a href="https://flowllm-ai.github.io/AxonX/playground/?lang=en">
    <img src="https://raw.githubusercontent.com/FlowLLM-AI/AxonX/main/docs/figures/studio/home.png" alt="AxonX Studio: Agent, research tasks, and artifacts" width="900" />
  </a>
</p>

For real experiments, deploy AxonX and install your plugins. Studio lets you work with the built-in Agent, inspect
Task lineage and research artifacts, and select a local or remote execution service. Market data and model services
may require API credentials.

## Research case: factors and portfolio strategy

The current Alpha158 case compares the adapted baseline, a model with two added risk factors, and a rank-retention
strategy that reuses the factor-model predictions. The 2026-10-10 rerun reports:

| Configuration | Top20 net annualized return | Net Sharpe | Daily two-sided turnover |
| --- | ---: | ---: | ---: |
| Alpha158 baseline | 7.67% | 0.3619 | 198.83% |
| Risk-factor model | 9.03% | 0.4052 | 199.35% |
| Rank-retention strategy | 32.37% | 1.1575 | 40.01% |

Training covers `[20150101,20230101)`; evaluation covers `20230103–20261008` (909 market dates), with buy/sell fees
of 0.05% / 0.15%. These are adapted AxonX experiments. They have no independent confirmation window, the model
settings do not isolate the added factors, and all three backtests report `incomplete_market_data`. Fills use
same-close quote proxies and 2026 is a partial year.

See the [full settings, evidence limits, reproduction commands, and Task provenance](https://github.com/FlowLLM-AI/AxonX/blob/main/docs/en/research/alpha158-case.md).

## Latest development

- **Latest published release:** [AxonX v0.1.2](https://github.com/FlowLLM-AI/AxonX/releases/tag/v0.1.2), October 10, 2026.
- **Current main branch:** Agent development-guide loading, improved streamed tool arguments and Studio Task views,
  plus authenticated service self-update Jobs and restart controls. See the [update guide](https://github.com/FlowLLM-AI/AxonX/blob/main/docs/en/guides/self-update.md) for availability and recovery behavior.

## Join the AxonX community

- **Questions, ideas, and research examples:** join [GitHub Discussions](https://github.com/FlowLLM-AI/AxonX/discussions). English and Chinese are welcome.
- **Bugs and concrete feature requests:** open an [AxonX issue](https://github.com/FlowLLM-AI/AxonX/issues).
- **Contribute:** improve documentation, develop research plugins, or fix bugs. Start with the [contribution guide](https://github.com/FlowLLM-AI/AxonX/blob/main/CONTRIBUTING.md).
- **Follow development:** [star AxonX](https://github.com/FlowLLM-AI/AxonX) and watch its repository for updates.

## More from FlowLLM-AI

[FlowLLM](https://github.com/FlowLLM-AI/flowllm) provides configurable LLM application workflows.
[Finance-MCP](https://github.com/FlowLLM-AI/finance-mcp) uses FlowLLM to serve financial search, crawling, and data tools
for MCP clients. Explore them when your work needs those capabilities.
