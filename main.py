"""The Router Confesses entry.

Writes a single original one-line excuse to /output/entry.txt.

The excuse: the router drops the connection at the movie's climax
because it has seen the twist already and, smug little appliance
that it is, decides the viewer does not deserve to see it first.
The line speaks in the router's own petty voice and lands in one
breath, with no buffering or firmware cliche in sight.
"""

import os

JOKE = "I saw the twist coming and decided you didn't deserve to see it first."


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only whitespace.
    text = JOKE.strip()
    if not (1 <= len(text) <= 200) or not text.strip():
        raise ValueError("entry text fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
