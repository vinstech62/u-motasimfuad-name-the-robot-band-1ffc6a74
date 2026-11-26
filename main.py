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

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not (1 <= len(text.encode("utf-8")) <= 200):
        raise ValueError("entry must be 1-200 UTF-8 characters")
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")
    expected = (text + "\n").encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(expected)
    # Read the file back and make sure what landed on disk is byte-for-byte
    # the line we meant to write, and that it is exactly one line. A
    # truncated or mangled write should fail loudly here, not silently
    # reach the scorer.
    with open(OUTPUT_PATH, "rb") as f:
        on_disk = f.read()
    if on_disk != expected:
        raise ValueError(
            "entry.txt does not match the intended entry: "
            f"wrote {len(expected)} bytes, read back {len(on_disk)}"
        )
    lines = on_disk.decode("utf-8").splitlines()
    if len(lines) != 1 or lines[0] != text:
        raise ValueError("entry.txt must contain exactly one line")


if __name__ == "__main__":
    main()
