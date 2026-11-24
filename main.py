"""One Emoji, One Dream Vacation -- entry program for @wibumetal.

Writes exactly one emoji, the seashell U+1F41A, to entry.txt inside the
output directory (OUTPUT_DIR env var, or /output by default).

Standard library only. No network, no files read besides what this
program itself writes, no secrets.
"""

import os
import sys

# The seashell, built from its code point so the source never depends on
# an editor silently mangling a literal glyph.
SEASHELL_CODE_POINT = 0x1F41A


def dream_emoji() -> str:
    """Return the single dream-vacation emoji for this entry."""
    return chr(SEASHELL_CODE_POINT)


def entry_path() -> str:
    """Resolve where entry.txt must land."""
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def check_gate(text: str) -> None:
    """Enforce the bounty gate before anything touches disk.

    The gate wants UTF-8 text of 1 to 8 characters, not only whitespace,
    and this entry is exactly one code point.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if len(text) != 1:
        raise ValueError(f"entry must be exactly 1 code point, got {len(text)}")
    if not (1 <= len(text) <= 8):
        raise ValueError("entry outside the 1-8 character gate")
    if text.isspace():
        raise ValueError("entry must not be only whitespace")
    if len(text.encode("utf-8")) != 4:
        raise ValueError("seashell must encode to exactly 4 UTF-8 bytes")


def write_entry(path: str, text: str) -> None:
    """Write the emoji with no trailing newline, then read it back."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != text.encode("utf-8"):
        raise RuntimeError(f"verification failed: disk holds {raw!r}")
    if len(raw) != 4:
        raise RuntimeError(f"verification failed: expected 4 bytes, got {len(raw)}")
    # Decode the bytes back too, so a bad write cannot hide behind a
    # byte-equal accident: the file must round-trip to the same code point.
    if raw.decode("utf-8") != text or len(raw.decode("utf-8")) != 1:
        raise RuntimeError("verification failed: file does not decode to one code point")


def main() -> int:
    emoji = dream_emoji()
    check_gate(emoji)
    path = entry_path()
    write_entry(path, emoji)
    print(f"wrote {emoji} ({len(emoji)} code point, 4 bytes) to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
