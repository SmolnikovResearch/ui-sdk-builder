# Smolnikov Research Skill - `ui-sdk-builder`

> **Category:** Design & Anti-Slop Craft · **License:** MIT · **Author:** [Smolnikov Research Center](https://github.com/SmolnikovResearch)

**EN:** Assemble accessible agent UI menus, forms, and views.

**RU:** Сборка доступных интерактивных компонентов ИИ-интерфейсов (меню, формы, карточки подтверждения, таблицы) под React, Vue, Svelte и HTML.

---

## On-Demand Activation & Lazy Loading (`on-demand.json`)

This skill stays **disabled by default** (`auto_load_on_startup: false`) and loads dependencies strictly when invoked:

| Component | Requirement |
|---|---|
| System binaries | `none` |
| Python packages | `none (stdlib)` |
| Model checkpoints | `none` |

## Installation in CapyAgent

```bash
capyagent skills install SmolnikovResearch/ui-sdk-builder/skills/ui-sdk-builder
```

Or copy this directory into `~/.capyagent/skills/` (or `~/.agents/skills/`).

## Check Status & Bootstrap Dependencies

```bash
python3 scripts/optional_skill_bootstrap.py ui-sdk-builder --status
python3 scripts/optional_skill_bootstrap.py ui-sdk-builder --install
```

See [`SKILL.md`](SKILL.md) for agent instructions and workflow examples.

## Related

- Full multi-skill catalog: [SmolnikovResearch/skills](https://github.com/SmolnikovResearch/skills)
- License: [MIT](LICENSE)
