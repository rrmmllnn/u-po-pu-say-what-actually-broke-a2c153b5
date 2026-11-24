#!/usr/bin/env python3
"""Say What Actually Broke: write one honest error line.

The program writes a single line of software error copy to
/output/entry.txt: it names the real failure in plain words,
tells the user what to do next, and keeps the joke to one line.
Pure standard library, no network, deterministic output.
"""

import os

LINE = "Today's deploy locked everyone out of sign-in. Your password is innocent \u2014 our release is guilty as charged. We're rolling it back; come back in five minutes."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("entry must be 1 to 200 characters")
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
