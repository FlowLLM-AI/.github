"""Build the captioned homepage walkthrough from public AxonX documentation screens.

Requires Pillow and ffmpeg. This is an illustrated product walkthrough, not a live
agent session or a newly executed backtest. See assets/demo/README.md for sources.
"""
from pathlib import Path
import subprocess

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets' / 'demo'
W, H, FPS = 1280, 720, 24
FONT = '/System/Library/Fonts/STHeiti Medium.ttc'
MONO = '/System/Library/Fonts/Menlo.ttc'
BG = '#0a1224'
WHITE = '#f1f5fb'
MUTED = '#acbcd3'
ACCENT = '#5ee6c8'
BLUE = '#72b8ff'
SCENES = [
    (7, 'AxonX', '让 Agent 执行可追溯的金融研究',
     'Let agents run traceable financial research.', None),
    (14, '01  Agent → Tasks', '先读任务契约，再提交；保存实际 Task / Run ID',
     'Discover the task schema, submit, and keep the actual Task / Run IDs.', None),
    (12, '02  Studio → Execution', '在 Studio 查看状态、进度和任务记录',
     'Follow task status and progress in the same research workspace.', 'task-list.png'),
    (11, '03  Inspect logs', '从日志核对执行过程，再确认任务成功',
     'Inspect execution evidence; accepted submission does not mean task success.', 'task-logs.png'),
    (10, '04  Trace dependencies', '查看上游与下游，追溯产物来自哪个任务',
     'Trace upstream and downstream tasks before reusing an artifact.', 'task-lineage.png'),
    (13, '05  Inspect backtest artifacts', '检查回测曲线、区间和成本假设，再解释结果',
     'Inspect returns, periods, and cost assumptions before drawing conclusions.', 'backtest-net-return.png'),
    (8, 'Start with AxonX', '先体验 Studio，再接入你自己的 Agent 与研究插件',
     'Try Studio, then connect your own agent and research plugins.', None),
]
FONTS = {}
IMAGES = {s[4]: Image.open(ASSETS / s[4]).convert('RGB') for s in SCENES if s[4]}


def font(size, mono=False):
    key = (size, mono)
    if key not in FONTS:
        FONTS[key] = ImageFont.truetype(MONO if mono else FONT, size)
    return FONTS[key]


def text(draw, xy, value, size=26, color=WHITE, mono=False):
    draw.text(xy, value, font=font(size, mono), fill=color)


def centered(draw, y, value, size=26, color=WHITE):
    box = draw.textbbox((0, 0), value, font=font(size))
    text(draw, ((W - box[2]) / 2, y), value, size, color)


def rounded(draw, box, fill='#14243c', outline='#2b4260', radius=18):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=1)


def scene_at(t):
    start = 0
    for i, scene in enumerate(SCENES):
        if t < start + scene[0] or i == len(SCENES) - 1:
            return i, max(0, t - start), start
        start += scene[0]


def render(t):
    i, elapsed, start = scene_at(t)
    duration, title, zh, en, screenshot = SCENES[i]
    im = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(im)
    text(d, (46, 25), 'FlowLLM-AI  /  AXONX', 17, ACCENT)
    text(d, (1055, 25), '75s WALKTHROUGH', 17, MUTED)
    text(d, (46, 62), title, 36)
    # Timeline keeps the viewer oriented as each stage is introduced.
    x = 46
    for j, s in enumerate(SCENES):
        width = s[0] / 75 * 1188 - 5
        color = ACCENT if j < i else '#253750'
        d.rounded_rectangle((x, 116, x + width, 121), radius=2, fill=color)
        if j == i:
            d.rounded_rectangle((x, 116, x + width * min(1, elapsed / duration), 121),
                                radius=2, fill=ACCENT)
        x += width + 5
    if i == 0:
        centered(d, 180, '让 Agent 执行可追溯的金融研究', 44)
        centered(d, 247, 'Let agents run traceable financial research.', 30, MUTED)
        cards = [('AGENT', 'Discover & submit', '发现并提交任务'),
                 ('STUDIO', 'Track execution', '查看执行过程'),
                 ('ARTIFACTS', 'Inspect evidence', '检查研究产物')]
        for j, (label, line, cn) in enumerate(cards):
            if elapsed < 0.65 + j * 0.55:
                continue
            x = 65 + j * 390
            rounded(d, (x, 332, x + 368, 480))
            text(d, (x + 25, 351), label, 20, ACCENT)
            text(d, (x + 25, 391), line, 26)
            text(d, (x + 25, 432), cn, 22, MUTED)
    elif i == 1:
        rounded(d, (46, 143, 1234, 251))
        text(d, (70, 159), 'AGENT GOAL / 示例指令', 17, ACCENT)
        text(d, (70, 190), 'Reuse a successful ETL. Run downstream research tasks.', 26)
        text(d, (70, 223), 'Keep parameters, execution records, and artifacts.', 20, MUTED)
        rounded(d, (46, 271, 1234, 535), '#0f1b30')
        text(d, (70, 288), 'ILLUSTRATIVE CLI / 示例命令', 16, BLUE)
        lines = [
            'axonx get_task_definition --task demo',
            'axonx submit --task demo --x 2 --y 3',
            "axonx wait_task --task-id '<task_id>' --run-id '<run_id>'",
            "axonx get_task_context --task-id '<task_id>'",
        ]
        for j, line in enumerate(lines):
            if elapsed >= 1.0 + j * 2.1:
                text(d, (70, 328 + j * 42), '$ ' + line, 21, WHITE, True)
        text(d, (70, 505), 'Replace placeholders with actual IDs returned by submission.', 16, MUTED)
    elif screenshot:
        box = (46, 143, 1234, 538)
        rounded(d, box, '#ffffff')
        source = IMAGES[screenshot]
        # Fit complete documentation screens; never crop labels or result values.
        fitted = ImageOps.contain(source, (1170, 377), Image.Resampling.LANCZOS)
        x = (W - fitted.width) // 2
        y = 152 + (377 - fitted.height) // 2
        im.paste(fitted, (x, y))
        if i == 2:
            label = 'TASKS → STATUS → PROGRESS'
        elif i == 3:
            label = 'LOGS → TERMINAL STATE → ARTIFACTS'
        elif i == 4:
            label = 'UPSTREAM → CURRENT TASK → DOWNSTREAM'
        else:
            label = 'EXISTING RESEARCH EXAMPLE • SEE THE LINKED REPORT'
        # A moving outline signals progression without fabricating UI clicks.
        d = ImageDraw.Draw(im)
        text(d, (60, 543), label, 14, BLUE)
    else:
        centered(d, 165, 'One research workspace.', 43)
        centered(d, 225, 'Agents execute. Researchers inspect.', 35, ACCENT)
        cards = [('AxonX', 'Research tasks & traceable artifacts'),
                 ('FlowLLM', 'Configurable LLM workflows'),
                 ('Finance-MCP', 'Financial tools for MCP clients')]
        for j, (label, detail) in enumerate(cards):
            y = 302 + j * 62
            rounded(d, (130, y, 1150, y + 53))
            text(d, (152, y + 10), label, 25, ACCENT if j == 0 else BLUE)
            text(d, (402, y + 12), detail, 22, MUTED)
        centered(d, 510, 'github.com/FlowLLM-AI/AxonX', 24, BLUE)
    # Both languages are burned in, so the walkthrough works with sound off.
    centered(d, 581, zh, 26)
    centered(d, 623, en, 20, MUTED)
    text(d, (46, 683), 'PRODUCT GUIDE • DOCUMENTATION SCREENS • ILLUSTRATIVE COMMANDS', 13, '#7f94b1')
    text(d, (1110, 683), f'{int(t):02d} / 75s', 15, MUTED)
    # Short fades smooth scene changes while retaining readable full-screen content.
    edge = min(elapsed / 0.3, (duration - elapsed) / 0.3, 1)
    if edge < 1:
        im = Image.blend(Image.new('RGB', (W, H), BG), im, max(0.0, edge))
    return im


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    render(3).save(ASSETS / 'axonx-demo-poster.png')
    command = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
               '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-an', '-c:v', 'libx264',
               '-preset', 'fast', '-crf', '22', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
               str(ASSETS / 'axonx-75s.mp4')]
    proc = subprocess.Popen(command, stdin=subprocess.PIPE)
    for frame in range(75 * FPS):
        proc.stdin.write(render(frame / FPS).tobytes())
        if frame % (FPS * 15) == 0:
            print(f'Rendered {frame // FPS}/75 seconds', flush=True)
    proc.stdin.close()
    if proc.wait():
        raise RuntimeError('ffmpeg failed')
    # 12-second, looping homepage teaser; link to the complete 75-second MP4.
    samples = [3, 17, 27, 38, 48, 59, 70, 72]
    frames = [render(t).resize((800, 450), Image.Resampling.LANCZOS) for t in samples]
    frames[0].save(ASSETS / 'axonx-demo-preview.gif', save_all=True,
                   append_images=frames[1:], duration=1500, loop=0, optimize=True)
    # Contact sheet for visual inspection of every scene.
    contact = Image.new('RGB', (1280, 1080), BG)
    for j, frame in enumerate(frames):
        thumb = frame.resize((640, 360), Image.Resampling.LANCZOS)
        if j < 6:
            contact.paste(thumb, ((j % 2) * 640, (j // 2) * 360))
    contact.save('/tmp/axonx-demo-contact.png')
    print('Created 75-second MP4, poster, and 12-second GIF teaser', flush=True)


if __name__ == '__main__':
    main()
