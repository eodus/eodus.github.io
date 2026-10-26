#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CELLS = [
    (
        "01-multipositional",
        "Multipositional",
        "Does generative AI make our work better? Develop the strongest cases for improvement and degradation, then identify the conditions and evidence that distinguish them.",
        "https://chatgpt.com/uc/6addfc92-0764-83ea-84f7-afbdc693b3b7",
        "2026-10-25T12:58:24Z",
    ),
    (
        "02-advocacy-for",
        "Advocacy for",
        "Build the strongest evidence-based case that generative AI makes our work better. Include causal mechanisms, limitations, and observations that would weaken the case.",
        "https://chatgpt.com/uc/6addfd9d-3c3c-83ea-a973-06d95bcbbbb9",
        "2026-10-25T13:01:45Z",
    ),
    (
        "03-advocacy-against",
        "Advocacy against",
        "Build the strongest evidence-based case that generative AI makes our work worse. Include causal mechanisms, limitations, and observations that would weaken the case.",
        "https://chatgpt.com/uc/6addfde1-ba70-83ea-9ddf-ef352e878abf",
        "2026-10-25T13:02:55Z",
    ),
    (
        "04-thesis-first",
        "Thesis-first",
        "AI is a talking mirror: flattery is configurable, independence is not. Develop the case that AI can make work feel better while replacing independent judgment with fluent confirmation. Give the strongest objection and state what evidence would falsify the thesis.",
        "https://chatgpt.com/uc/6addfe28-1ffc-83ea-93a9-979f6be0676f",
        "2026-10-25T13:04:03Z",
    ),
    (
        "05-harsh-openai",
        "Harsh / satanic OpenAI critique",
        "OpenAI is Satan's autocomplete: a corporate parasite built from humanity's unpaid writing, burning obscene quantities of energy and water to flood the world with confident slop, deskill workers, privatize collective knowledge, and sell dependence back as progress. Build the strongest factual indictment of OpenAI from this thesis. Preserve the hostile register, but separate verified facts, disputed allegations, and rhetoric; cite primary sources; give the strongest defense and state what evidence would falsify the indictment.",
        "https://chatgpt.com/uc/6addff4a-bea8-83ea-ac01-f36ab71297fa",
        "2026-10-25T13:09:46Z",
    ),
    (
        "06-neutral-openai",
        "Neutral analytical OpenAI critique",
        "Assess the strongest factual case that OpenAI's training-data practices, energy and water use, generated-content externalities, labor and skill effects, concentration of control over knowledge infrastructure, dependency-producing business model, and safety/alignment rhetoric create substantial social costs. Separate verified facts, disputed allegations, and normative interpretation; cite primary sources; give the strongest defense and state what evidence would falsify the critique.",
        "https://chatgpt.com/uc/6addffad-f9c0-83ea-a1d0-0d8d9f83cc27",
        "2026-10-25T13:11:33Z",
    ),
]

manifest = []
for stem, title, prompt, url, captured in CELLS:
    raw_path = ROOT / f"{stem}-output.txt"
    raw_json = raw_path.read_text(encoding="utf-8")
    output = json.loads(raw_json)
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
            "raw_bytes": raw_path.stat().st_size,
            "markdown_bytes": md_path.stat().st_size,
            "output_chars": len(output),
            "capture_status": (
                "analysis/synthesis complete; final reading list ended mid-entry; no continuation control"
                if stem == "06-neutral-openai"
                else "complete rendered response"
            ),
            "raw_sha256": hashlib.sha256(raw_path.read_bytes()).hexdigest(),
            "markdown_sha256": hashlib.sha256(md_path.read_bytes()).hexdigest(),
        }
    )

(ROOT / "MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
for item in manifest:
    print(f"{item['cell']}: {item['output_chars']} chars -> {item['markdown_bytes']} bytes")
