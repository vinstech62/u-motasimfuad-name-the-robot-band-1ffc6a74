"""Name the Robot Band — make.fun entry (program/v1).

Writes exactly one line to /output/entry.txt: one funny name for a band
made of robots, plus a few words on its hit song. Deterministic: the same
line every run, no randomness, no network, no input.
"""

import os

ENTRY = (
    "Ctrl+Alt+Defeat \u2014 hit single \u201cHave You Tried Turning Me Off "
    "and On Again\u201d topped the charts for 0.4 seconds before crashing."
)


def main() -> None:
    text = ENTRY
    if not (1 <= len(text.encode("utf-8")) <= 200):
        raise ValueError("entry must be 1-200 UTF-8 characters")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
