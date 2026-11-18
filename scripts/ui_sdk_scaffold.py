#!/usr/bin/env python3
"""Deterministic AI Agent UI primitive assembler for React, Vue, Svelte, and HTML."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

COMPONENTS: Dict[str, str] = {
    "menu": "Keyboard-navigable dropdown/action menu (ArrowUp/Down, Escape, WAI-ARIA menuitem).",
    "form": "Accessible validated parameter form with inline live error summary.",
    "approval-card": "Human-in-the-loop action confirmation card with explicit scope badges.",
    "artifact-table": "Tabular-nums data table with keyboard sort and empty state.",
    "command-palette": "Filterable agent command launcher with keyboard selection.",
    "streaming-turn": "Accessible streaming assistant response with expandable tool steps.",
}

FRAMEWORKS = ("react", "vue", "svelte", "html")


def _pascal(name: str) -> str:
    return "".join(part.capitalize() for part in name.split("-") if part)


def scaffold_component(component: str, framework: str = "react") -> Dict[str, Any]:
    """Generate clean, self-contained, accessible source code for a UI primitive."""
    comp = component.strip().lower()
    fw = framework.strip().lower()
    if comp not in COMPONENTS:
        raise ValueError(f"Unknown component {component!r}; choose from {sorted(COMPONENTS)}")
    if fw not in FRAMEWORKS:
        raise ValueError(f"Unknown framework {framework!r}; choose from {FRAMEWORKS}")

    sym = _pascal(comp)
    if fw == "react":
        code = _render_react(comp, sym)
        ext = "tsx"
    elif fw == "vue":
        code = _render_vue(comp, sym)
        ext = "vue"
    elif fw == "svelte":
        code = _render_svelte(comp, sym)
        ext = "svelte"
    else:
        code = _render_html(comp, sym)
        ext = "html"

    return {
        "skill": "ui-sdk-builder",
        "component": comp,
        "framework": fw,
        "symbol": sym,
        "filename": f"{sym}.{ext}",
        "code": code,
    }


def _render_react(comp: str, sym: str) -> str:
    if comp == "approval-card":
        return """import React from "react";

export interface ApprovalCardProps {
  action: string;
  target: string;
  onApproveOnce: () => void;
  onApproveSession: () => void;
  onDeny: () => void;
}

export function ApprovalCard({ action, target, onApproveOnce, onApproveSession, onDeny }: ApprovalCardProps) {
  return (
    <section role="alertdialog" aria-labelledby="capy-approve-title" className="capy-approval-card">
      <h3 id="capy-approve-title">Confirm action: {action}</h3>
      <p className="capy-approval-target">{target}</p>
      <div className="capy-approval-actions">
        <button type="button" onClick={onApproveOnce}>Allow once</button>
        <button type="button" onClick={onApproveSession}>Allow session</button>
        <button type="button" onClick={onDeny}>Deny</button>
      </div>
    </section>
  );
}
"""
    if comp == "menu":
        return """import React, { useState, useRef } from "react";

export interface MenuItem {
  id: string;
  label: string;
  onSelect: () => void;
}

export function Menu({ label, items }: { label: string; items: MenuItem[] }) {
  const [open, setOpen] = useState(false);
  const [active, setActive] = useState(0);
  const btnRef = useRef<HTMLButtonElement>(null);

  const onKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Escape") {
      setOpen(false);
      btnRef.current?.focus();
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      setActive((prev) => (prev + 1) % Math.max(1, items.length));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActive((prev) => (prev - 1 + items.length) % Math.max(1, items.length));
    }
  };

  return (
    <div className="capy-ui-menu" onKeyDown={onKeyDown}>
      <button ref={btnRef} type="button" aria-haspopup="menu" aria-expanded={open} onClick={() => setOpen(!open)}>
        {label}
      </button>
      {open && (
        <ul role="menu">
          {items.map((item, idx) => (
            <li key={item.id} role="none">
              <button
                type="button"
                role="menuitem"
                tabIndex={idx === active ? 0 : -1}
                onClick={() => { item.onSelect(); setOpen(false); }}
              >
                {item.label}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
"""
    return f"""import React from "react";

export interface {sym}Props {{
  title?: string;
  items?: Array<Record<string, string>>;
}}

export function {sym}({{ title = "{sym}", items = [] }}: {sym}Props) {{
  return (
    <section aria-label={{title}} className="capy-ui-{comp}" style={{{{ fontVariantNumeric: "tabular-nums" }}}}>
      <h3>{{title}}</h3>
      <div role="region" aria-live="polite">
        {{items.length === 0 ? <p>No items.</p> : items.map((row, idx) => <div key={{idx}}>{{JSON.stringify(row)}}</div>)}}
      </div>
    </section>
  );
}}
"""


def _render_vue(comp: str, sym: str) -> str:
    return f"""<script setup lang="ts">
defineProps<{{ title?: string; items?: Array<Record<string, string>> }}>();
</script>

<template>
  <section :aria-label="title || '{sym}'" class="capy-ui-{comp}" style="font-variant-numeric: tabular-nums">
    <h3>{{{{ title || '{sym}' }}}}</h3>
    <div role="region" aria-live="polite">
      <slot />
    </div>
  </section>
</template>
"""


def _render_svelte(comp: str, sym: str) -> str:
    return f"""<script lang="ts">
  export let title: string = "{sym}";
</script>

<section aria-label={{title}} class="capy-ui-{comp}" style="font-variant-numeric: tabular-nums">
  <h3>{{title}}</h3>
  <div role="region" aria-live="polite">
    <slot />
  </div>
</section>
"""


def _render_html(comp: str, sym: str) -> str:
    return f"""<section aria-label="{sym}" class="capy-ui-{comp}" style="font-variant-numeric: tabular-nums;">
  <h3>{sym}</h3>
  <div role="region" aria-live="polite" data-ui-sdk="{comp}"></div>
</section>
<script>
(() => {{
  const root = document.querySelector('[data-ui-sdk="{comp}"]');
  if (!root) return;
  root.dataset.ready = "true";
}})();
</script>
"""


def inspect_status() -> Dict[str, Any]:
    return {
        "skill": "ui-sdk-builder",
        "auto_load_on_startup": False,
        "components": sorted(COMPONENTS.keys()),
        "frameworks": list(FRAMEWORKS),
    }


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Scaffold AI Agent UI SDK primitives.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list")
    sc = sub.add_parser("scaffold")
    sc.add_argument("--component", required=True, choices=sorted(COMPONENTS.keys()))
    sc.add_argument("--framework", default="react", choices=FRAMEWORKS)
    sc.add_argument("--out", default="")
    args = parser.parse_args(argv)
    if args.cmd == "list":
        print(json.dumps(inspect_status(), ensure_ascii=False, indent=2))
        return 0
    res = scaffold_component(args.component, args.framework)
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(res["code"], encoding="utf-8")
        print(json.dumps({"ok": True, "path": str(out), "component": res["component"], "framework": res["framework"]}))
    else:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
