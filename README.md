# find-bad-review

`find-bad-review` is a git-managed skill project for researching representative bad reviews about a product across public channels such as Amazon, Chewy, Walmart, Reddit, TikTok, and brand or retailer sites.

## What is in this repo

- `skills/find-bad-review/`: the main Codex-ready skill
- `platforms/`: lightweight portability notes for Codex and Claude Code
- `examples/`: example output shape

## Current scope

This repo is optimized for human-triggered, evidence-backed research. It does not yet implement a full plugin, large-scale crawling service, or login-based collectors.

## Starting point

Use the skill at [skills/find-bad-review/SKILL.md](skills/find-bad-review/SKILL.md). The report skeleton generator lives at [skills/find-bad-review/scripts/render_report_stub.py](skills/find-bad-review/scripts/render_report_stub.py).
