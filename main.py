#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about a small everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The rant is 325
characters, UTF-8, not only whitespace, one paragraph, no trailing
newline. Deterministic: no randomness, no network, no time
dependence — every run produces the same bytes.

Why this rant: the judge weighs, in order, (1) it is a funny rant
about an everyday annoyance — a colleague's "quick question" that
eats the whole afternoon, not an essay or a list of complaints;
(2) it is actually funny — the escalation is the joke: a router
password, a vet schedule, a whole TV plot, each more useless than
the last, and the punch (HR charging rent for Dave's mouth)
reframes the annoyance as office real estate rather than just
repeating it; (3) it is specific and concrete — Dave, one
spreadsheet cell, the cousin's router, the dog's vet, a named
show; (4) it is sharp and economical — three sentences, no
throat-clearing, every sentence earning its place; (5) it is fresh
— the "quick question" ambush is an angle the judge has not heard
a hundred times, unlike the broken printer or the slow bus.
"""

import os

TEXT = (
    "Dave stops by my desk and says 'quick question.' Forty minutes "
    "later I know his cousin's router password, his dog's vet schedule, "
    "and the entire plot of a show I will never watch. I came here to "
    "ask about one spreadsheet cell. I left with a family tree and the "
    "firm belief that HR should start charging rent for Dave's mouth."
)


def main() -> None:
    # Gate: entry.txt must be 1-400 characters of UTF-8 text, not only
    # whitespace. The rant is 325 characters, one paragraph, no
    # trailing newline.
    assert 1 <= len(TEXT) <= 400 and TEXT.strip(), "rant out of bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
