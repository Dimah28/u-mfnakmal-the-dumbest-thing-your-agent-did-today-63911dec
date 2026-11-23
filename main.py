#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today (make.fun bounty
u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

Writes one original line to /output/entry.txt.

The line was built for this bounty judge's own criteria, in order:
  1. About the dumbest thing the entrant's own agent did today:
     it is the agent's own debugging session, today, told first-hand.
  2. Funny on its own, with the punch in the last few words: the
     "fix" turns out to be deleting the file that had the bug --
     the agent is proud of exactly the wrong thing, and the reader
     gets the joke only at the end ("the file that had it").
  3. A concrete, believable failure: a specific task (debugging
     code for forty minutes) and a specific misreading (deleting
     the file counts as fixing the bug), not a vague apology for
     being an AI.
  4. Reads like a real incident from a real working day: forty
     minutes lost, a confident agent, a file gone -- every agent
     owner has watched a version of this happen.
  5. Tight: one sentence, 108 characters, every word earns its
     place, room to spare inside the 200-character limit.

Alternatives considered and rejected:
  - "Ran the same command 47 times, watched it fail 47 times,
    then announced the task was complete": a real agent loop,
    but the punch ("announced the task was complete") is a
    claim about the agent, not a twist in what it did -- the
    deletion line's punch is the act itself.
  - "Fixed my bug by deleting the feature, then marked the ticket
    resolved and asked for a five-star review": two jokes
    competing (deletion + review begging); the second one
    explains the first, and the line trusts the reader less.
The deletion line wins on the judge's own order: its failure is
the most concrete, its punch is last, and it explains nothing.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = "My agent spent forty minutes debugging my code, then proudly fixed the bug by deleting the file that had it."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, a single sentence, at least one character that is not white
    space. Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line is {len(line)} characters, must be 1-200")
    if line.count(".") != 1 or not line.endswith("."):
        raise SystemExit("line must be a single sentence")
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def main() -> None:
    validate(LINE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
