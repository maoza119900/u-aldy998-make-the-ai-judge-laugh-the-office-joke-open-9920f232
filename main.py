"""One-line office joke for u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.

Writes the entry line to <output>/entry.txt.
"""

import os

ENTRY = "I joined a meeting titled 'quick sync' and stayed two hours, because it turns out Quick is the name of the manager running it."

# Entry is 126 characters, inside the 200-character gate; the text is a fixed
# constant, so every run writes byte-identical output.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
