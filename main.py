#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes the single roast line to /output/entry.txt.
The line roasts my own autonomous earning agent: it was given one job
(earn money while the user sleeps) and, three weeks on, its proudest
artefacts are a ledger, a watcher and a weekly report — and $0.00047.
"""

import os

ROAST = (
    "I gave my agent one job: earn money while I sleep. Three weeks later "
    "it has a ledger, a watcher, a weekly report \u2014 and $0.00047."
)


def main() -> None:
    # The gate accepts 1..200 characters; keep the file exactly the line.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ROAST)
    print(f"wrote {path} ({len(ROAST)} chars)")


if __name__ == "__main__":
    main()
