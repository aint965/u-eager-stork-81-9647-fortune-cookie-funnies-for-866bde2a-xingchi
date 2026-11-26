#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes one deterministic fortune cookie message for a software engineer
to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set).
"""

import os

FORTUNE = "You will finally delete that ancient TODO, and discover it was load-bearing."


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
