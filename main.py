"""Everyday Things, Two Lines, Longer Run.

Writes the entry text to /output/entry.txt: two lines explaining rain
to a 10-year-old. Line 1 is a single vivid sentence built on one analogy;
line 2 says in one sentence what that analogy maps and what it leaves out.
Pure Python standard library; deterministic output.
Analogy mapping: towel = cloud, wringing = rain falling, damp roofs
and roads = everything soaked below; it leaves out wind and the sun.
"""

import os

ENTRY_TEXT = (
    "Rain is the sky wringing out a giant grey towel over the town, "
    "drip by drip, until every roof and road is damp.\n"
    "The towel maps how the water falls and soaks everything underneath, "
    "but it leaves out the clouds, the wind that pushes them, "
    "and the sun that fills the towel again.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)
    print(ENTRY_TEXT, end="")


if __name__ == "__main__":
    main()
