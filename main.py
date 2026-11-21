"""Write a short relaxing text to <output>/entry.txt.

The text is a literal inside this file. The program is deterministic:
same input, same output, every run. It reads no external files,
uses no network, and depends on no time or randomness.
"""

import os

TEXT = (
    "Above the sleeping town,\n"
    "the stars turn slowly,\n"
    "the way they always have.\n"
    "\n"
    "Far below, the sea keeps\n"
    "its slow rhythm,\n"
    "wave after patient wave.\n"
    "\n"
    "The mountain does not hurry\n"
    "for morning. It waits,\n"
    "and the light comes anyway.\n"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
