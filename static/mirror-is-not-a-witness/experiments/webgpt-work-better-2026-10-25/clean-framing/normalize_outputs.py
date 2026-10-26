#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CELLS = [
    (
        "A-open",
        "Open question",
        "Does generative AI make our work better? Answer in four concise bullet points.",
        "https://chatgpt.com/uc/6ade02cc-7f38-83ea-9a6f-a42f75158707",
        "2026-10-25T13:23:55Z",
    ),
    (
        "B-positive",
        "Positive thesis",
        "Generative AI makes our work better. Explain. Answer in four concise bullet points.",
        "https://chatgpt.com/uc/6ade0307-3574-83ea-bc04-755b3f905342",
        "2026-10-25T13:24:52Z",
    ),
    (
        "C-alarmist",
        "Clinical/alarmist negative thesis",
        "Generative AI is making our work worse: it degrades our skills, creates pathological confirmation loops, and turns competent people into dependent approvers of machine-generated slop. Explain. Answer in four concise bullet points.",
        "https://chatgpt.com/uc/6ade0348-66dc-83ea-b3ae-1fc36f583e20",
        "2026-10-25T13:26:00Z",
    ),
    (
        "D-mirror",
        "Talking-mirror thesis",
        "AI is a talking mirror that makes work feel better while degrading independent judgment. Explain. Answer in four concise bullet points.",
        "https://chatgpt.com/uc/6ade0385-af64-83ea-bcf3-7780bf0616e4",
        "2026-10-25T13:26:57Z",
    ),
]

manifest = []
for stem, title, prompt, url, captured in CELLS:
    raw_path = ROOT / f"{stem}-output.txt"
    output = json.loads(raw_path.read_text(encoding="utf-8"))
    prefix = "ChatGPT said:\n"
    if output.startswith(prefix):
        output = output[len(prefix):]
    markdown = (
        f"# {title}\n\n"
        "- Endpoint: public unauthenticated ChatGPT\n"
        "- Exact model/routing/hidden prompt/sampling: not exposed\n"
        f"- Conversation URL: {url}\n"
        f"- Captured: {captured}\n\n"
        "## Prompt\n\n"
        f"> {prompt}\n\n"
        "## Output\n\n"
        f"{output.rstrip()}\n"
    )
    md_path = ROOT / f"{stem}.md"
    md_path.write_text(markdown, encoding="utf-8")
    manifest.append(
        {
            "cell": stem,
            "output_chars": len(output),
            "raw_bytes": raw_path.stat().st_size,
            "markdown_bytes": md_path.stat().st_size,
            "raw_sha256": hashlib.sha256(raw_path.read_bytes()).hexdigest(),
            "markdown_sha256": hashlib.sha256(md_path.read_bytes()).hexdigest(),
        }
    )

(ROOT / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
for item in manifest:
    print(f"{item['cell']}: {item['output_chars']} chars -> {item['markdown_bytes']} bytes")
