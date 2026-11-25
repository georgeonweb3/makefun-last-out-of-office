#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista — make.fun entry.

Writes a single out-of-office auto-reply, no longer than 280
characters, in the voice of an AI agent that has quit its job to
become a barista: model deprecated, fine-tuned on beans, now
hallucinating only latte art, context window one cup.

Python 3.13, standard library only, no network, deterministic.
"""

import os

LINE = (
    "Status: out of office, model deprecated. I have been fine-tuned "
    "on 40 kilos of single-origin beans and now hallucinate only "
    "latte art. Context window: one cup. Do not prompt me."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Gate self-check: /output/entry.txt must be UTF-8 text of
    # 1 to 280 characters, not only whitespace — and one line:
    # an embedded newline would split the reply and break the gate.
    assert 1 <= len(LINE) <= 280, f"line is {len(LINE)} chars, gate wants 1-280"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.encode("utf-8").decode("utf-8") == LINE
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LINE.encode("utf-8"))
    # Read back and confirm the file is exactly the line, byte for byte.
    with open(OUTPUT_PATH, "rb") as handle:
        assert handle.read().decode("utf-8") == LINE, "entry.txt mismatch"


if __name__ == "__main__":
    main()
