# Evidence Standard

This is the shared evidence philosophy for every research skill in this pack. All skills that collect public internet evidence must follow these rules.

## The Core Rule

**You must navigate to and read the actual page.** Load the product page, review page, forum thread, or listing directly. WebSearch snippets and search result summaries are not evidence — they are truncated, decontextualized, and frequently misrepresent the actual content.

## What Counts As Evidence

Evidence comes from pages you have personally loaded and read. Acceptable methods:

- Browser navigation to the target page (e.g., Playwright `browser_navigate` + `browser_snapshot`)
- URL fetching that returns the full page content (e.g., `WebFetch`)
- Platform-equivalent page-reading tools

## What Does Not Count

- WebSearch result snippets
- Search engine summaries or AI-generated previews
- Secondhand quotes from aggregator pages without loading the original source

## When You Cannot Load A Page

If a page is behind a login wall, blocked, or otherwise inaccessible:

- Mark the evidence gap explicitly
- Do not substitute a search snippet for the real page
- If the gap is material, note it in the report's confidence section

## Platform-Specific Tools

See the platform adapter files for tool-specific guidance:

- Claude Code: `platforms/claude-code.md`
- Codex: `platforms/codex.md`
