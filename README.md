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

## Install with `npx skills add`

This repo follows the standard `skills/<skill-name>/SKILL.md` layout, so it is compatible with the open agent skills installer.

From this repo root, install to both Codex and Claude Code:

```bash
npx skills add . --skill find-bad-review -a codex -a claude-code -g
```

Install only to Codex:

```bash
npx skills add . --skill find-bad-review -a codex -g
```

Install only to Claude Code:

```bash
npx skills add . --skill find-bad-review -a claude-code -g
```

If your environment does not support symlinks well, use copy mode:

```bash
npx skills add . --skill find-bad-review -a codex -a claude-code -g --copy
```

If you later publish this repo to GitHub, the same install pattern works with the repository URL or `owner/repo` form:

```bash
npx skills add owner/repo --skill find-bad-review -a codex -a claude-code -g
```

After installation:

- In Codex, invoke the skill with `$find-bad-review`
- In Claude Code, invoke the skill with `/find-bad-review`

## Manual install for Codex

This repo is currently a skill project, not a full plugin package. The fastest way to use it in Codex is to expose the skill folder through your local Codex skills directory.

From this repo root:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$(pwd)/skills/find-bad-review" "${CODEX_HOME:-$HOME/.codex}/skills/find-bad-review"
```

If you prefer a copy instead of a symlink:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R "$(pwd)/skills/find-bad-review" "${CODEX_HOME:-$HOME/.codex}/skills/find-bad-review"
```

Then in Codex:

1. Open or restart Codex if it was already running.
2. Open a thread.
3. Invoke the skill with `$find-bad-review` or press `$` and pick the skill.

Example:

```text
$find-bad-review Analyze the public bad reviews for a dog leash across Amazon, Chewy, Walmart, Reddit, TikTok, and brand sites.
```

## Manual install for Claude Code

Claude Code supports standalone skills in either a user-level or project-level `.claude/skills/` directory. Since this repo already contains the skill folder, the easiest setup is a symlink.

### User scope

```bash
mkdir -p "$HOME/.claude/skills"
ln -s "$(pwd)/skills/find-bad-review" "$HOME/.claude/skills/find-bad-review"
```

### Project scope

Run this inside the repo where you want Claude Code to see the skill:

```bash
mkdir -p .claude/skills
ln -s "/Users/victor/F_Repository/find-bad-review/skills/find-bad-review" .claude/skills/find-bad-review
```

Then restart Claude Code in that project, or reload your session if you already had it open. Invoke the skill with:

```text
/find-bad-review Analyze the public bad reviews for a dog leash across Amazon, Chewy, Walmart, Reddit, TikTok, and brand sites.
```

## If you want to package it later

- For Codex, keep this skill as-is if you only need a reusable process.
- For Claude Code, convert it into a plugin when you want namespaced distribution, marketplace install, or additional components such as agents, hooks, or MCP servers.
- The core workflow should continue to live in [skills/find-bad-review/SKILL.md](skills/find-bad-review/SKILL.md), with platform-specific wrappers kept thin.
