# AxonX homepage walkthrough

A **75-second illustrated product walkthrough** with English and Chinese captions,
plus a 12-second looping GIF preview. H.264 MP4, 1280 × 720, 24 fps, no audio.

This is a documentation-based product guide, not a recording of a live coding agent
or a newly executed experiment. The CLI section shows illustrative commands for the
built-in `demo` Task; its placeholder IDs must be replaced with actual submission IDs.
The backtest section is a separate, existing research example. It is not the output
of the arithmetic `demo` Task. The online Playground uses fictional data, simulated
execution, and a scripted Agent.

## Timeline

| Time | Content |
| --- | --- |
| 00–07s | Positioning: let agents run traceable financial research |
| 07–21s | Agent goal, Task schema discovery, submission, waiting, and context inspection |
| 21–33s | Studio Task status and progress |
| 33–44s | Execution logs and terminal state |
| 44–54s | Upstream and downstream Task relationships |
| 54–67s | Existing backtest artifact and interpretation |
| 67–75s | AxonX entry point and related projects |

## Sources

Screens are copied without modifying values from the public
[AxonX Studio documentation assets](https://github.com/FlowLLM-AI/AxonX/tree/main/docs/figures/studio).
CLI examples follow the [external-agent guide](https://flowllm-ai.github.io/AxonX/en/agent/external).
The underlying backtest's setup and interpretation are documented in the
[experiment report](https://github.com/FlowLLM-AI/AxonX/blob/main/plugins/a158_enhanced/EXPERIMENT_RESULTS.md).

The video uses `task-list.png`, `task-logs.png`, `task-lineage.png`, and `backtest-net-return.png`.

## Rebuild

Run `python scripts/build_homepage_demo.py` from the repository root. Requires Python,
Pillow, ffmpeg, and the macOS STHeiti and Menlo fonts; change the font paths in the
script for another platform. No network, model credentials, or research execution
are needed to rebuild the video from the included public screens.
