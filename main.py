#!/usr/bin/env python3
"""Say What Actually Broke: write one honest error line.

The program writes a single line of software error copy to
/output/entry.txt: it names the real failure in plain words,
tells the user what to do next, and keeps the joke to one line.
Pure standard library, no network, deterministic output.
"""

import os

LINE = "Our latest update broke the login page. Your password is fine. Our code is not. We're rolling it back \u2014 try again in five minutes."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
