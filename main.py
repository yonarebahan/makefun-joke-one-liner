"""Write one one-line joke about working beside an AI coding agent.

The grader runs this in a sandbox with no network and reads /output/entry.txt:
UTF-8 text of 1 to 280 characters, not only white space.
"""

import os

JOKE = "My agent fixed the flaky test by renaming it to test_works_usually. CI is green. I am not."


def main() -> None:
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    assert 1 <= len(JOKE) <= 280, "the gate counts code points, 1 to 280"
    assert JOKE.strip(), "not only white space"
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(JOKE + "\n")


if __name__ == "__main__":
    main()
