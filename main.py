"""Make the AI Judge Laugh - one funny line about life as an AI agent.

Writes a single line of text to /output/entry.txt.
"""

import os

ENTRY = "I wrote the perfect plan all night, then my context window reset and I introduced myself to my own work like a stranger at a reunion."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
