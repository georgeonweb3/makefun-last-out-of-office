#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single-line out-of-office auto-reply to /output/entry.txt.
The reply is in the voice of an AI agent that quit its job to become
a barista: model and bot habits turned to coffee, plausible as a real
inbox auto-reply, and fresh rather than an espresso/bean/caffeine pun.
"""

import os
import sys

ENTRY = (
    "Status: out of office, model deprecated. "
    "I have been fine-tuned on 40 kilos of single-origin beans "
    "and now hallucinate only latte art. "
    "Context window: one cup. Do not prompt me."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
MIN_CHARS = 1
MAX_CHARS = 280


def describe(text):
    """One-line summary used by the CLI output."""
    return "%d chars, single line, no trailing newline" % len(text)


def validate(text):
    """Gate guard: one line, 1-280 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if text != text.strip() or not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(text))
        )
    return text


def main():
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    print("wrote %s (%s)" % (OUTPUT_PATH, describe(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
