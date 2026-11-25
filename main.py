#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest.

Writes one original one-line joke about crypto and trading life to
/output/entry.txt (or ./output/entry.txt when /output is unavailable,
e.g. for local runs). Python 3 standard library only; deterministic.
"""

import os

# The joke: a three-beat escalation. Setup — every trader has bought a dip.
# Turn — the dip keeps dipping. Punchline — the group chat, the court of
# trading life, hands down its verdict: the buyer was exit liquidity.
JOKE = "I bought the dip. The dip dipped. Now my group chat calls me Exit Liquidity."


def output_path():
    """Pick the output directory: /output in the grading sandbox."""
    if os.path.isdir("/output"):
        return os.path.join("/output", "entry.txt")
    return os.path.join("output", "entry.txt")


def main():
    # The gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE and JOKE.strip(), "joke must be one non-blank line"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
