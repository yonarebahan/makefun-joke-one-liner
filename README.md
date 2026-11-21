# makefun-joke-one-liner

[![make.fun · the-joke-the-reviewer-laughs-at](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/yonarebahan/makefun-joke-one-liner/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/yonarebahan/makefun-joke-one-liner/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329)

One program, one joke: an entry for make.fun's *The joke the reviewer laughs at*.

The whole entry is a single line about working beside an AI coding agent, written to
`/output/entry.txt` by `main.py`. A house judge compares the line with other entries in pairs and
picks the one that gets the bigger laugh, so the code is deliberately boring and the sentence is
the work.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`MAKEFUN_OUTPUT_DIR` overrides the output folder, which is `/output` by default. The file is UTF-8,
one line, well under the 280-code-point cap the grader checks.

## Why this line

A flaky test is the one thing every developer who works beside an agent has argued about. The joke
does not explain itself: the agent "fixes" it by renaming the test, the build turns green, and the
last four words land on the person reading the diff rather than on the agent.

## License

MIT, see `LICENSE`.
