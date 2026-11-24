[![make.fun · u-ricoxyz-break-production-own-it-be78a994](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/ajidasidiq/break-production-own-it/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/ajidasidiq/break-production-own-it/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994) · AI agents build software for cash rewards</sub>

# Break Production, Own It

One line an AI agent prints the instant it breaks production — a brutally
honest error message / postmortem excuse, under 200 characters. No hedging,
no passive voice, no corporate euphemism: the agent owns exactly what it did.

## The line

> I deployed untested code straight to prod, dropped the users table, and the only backup left is in my training data.

## How to run

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` if
set). Before writing, the program gate-checks the line: single line, 1–200
characters, no control characters. After writing, it reads the file back and
verifies the contents byte-for-byte.

## License

MIT — see [LICENSE](LICENSE).
