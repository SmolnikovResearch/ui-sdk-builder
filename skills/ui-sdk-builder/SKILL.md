---
name: ui-sdk-builder
description: Assemble accessible agent UI menus, forms, and views.
version: 1.0.0
author: Smolnikov Research
license: MIT
platforms: [linux, macos, windows]
metadata:
  capyagent:
    tags: [ui-sdk, components, react, vue, svelte, html, forms, menus]
    category: creative
    related_skills: [design-md, unslop, hallmark-styles]
---

# Agent UI SDK Primitive Assembler Skill

Assemble deterministic, keyboard-accessible interactive UI components for AI agents (`menu`, `form`, `command-palette`, `approval-card`, `artifact-table`, `streaming-turn`, `tool-badge`) with state logic already wired for React, Vue, Svelte, and vanilla HTML/CSS.

## When to Use

Use this skill when building or extending agent chat views, tool approval cards, parameter forms, command menus, or structured result tables, ensuring behavior matches WAI-ARIA keyboard rules and the project's `DESIGN.md`.

## Primitive Catalog

- `menu`: Roving-tabindex dropdown / context menu (`ArrowUp`/`ArrowDown`/`Escape`/`Home`/`End`, ARIA roles `menu`/`menuitem`).
- `form`: Constraint-validated schema form with inline field error announcement (`aria-live="polite"`, `tabular-nums` numeric inputs).
- `approval-card`: Explicit human-in-the-loop approval banner (`approve_once`, `approve_session`, `deny`) with scope summary and focus trap safety.
- `artifact-table`: Sortable table with sticky header, `tabular-nums`, and empty-state guidance.
- `command-palette`: Filterable action launcher with shortcut hints (`Ctrl/Cmd+K`).
- `streaming-turn`: Accessible live assistant turn with tool-call accordion (`status: pending|done|error`).

## CLI Usage (`SKILL_DIR/scripts/ui_sdk_scaffold.py`)

```bash
python3 SKILL_DIR/scripts/ui_sdk_scaffold.py list
python3 SKILL_DIR/scripts/ui_sdk_scaffold.py scaffold --component approval-card --framework react
python3 SKILL_DIR/scripts/ui_sdk_scaffold.py scaffold --component menu --framework html --out ./menu.html
```

This skill loads lazily from `optional-skills` (`auto_load_on_startup: false`) with zero external dependencies.
