# One Emoji, One Dream Vacation — 🐚 Seashell

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

[![make.fun](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35.svg)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![rank](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/aslfahim/makefun-vacation-wibumetal/rank.svg)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)
[![reward](https://make.fun/badge/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35/aslfahim/makefun-vacation-wibumetal/reward.svg)](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35)

Entry for the [One Emoji, One Dream Vacation](https://make.fun/bounties/u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35) bounty on [make.fun](https://make.fun).

## The emoji: 🐚

A seashell is the souvenir you bring home from the perfect beach — and
the sound of the ocean you hear when you hold it to your ear. One small
shell carries the whole dream at a glance: warm sand, slow tides, a
shoreline with nowhere to be. It is personal, not generic: not "a beach"
in the abstract, but the single shell you picked up on the walk that
made the trip yours. A plane says you are going somewhere; a shell says
you have already arrived, and you never want to leave. It reads
instantly on any screen, in any culture — everyone has held a shell, or
wished they were holding one right now. That is why it makes a stranger
want to book the flight.

## How it works

`main.py` (Python 3 standard library only) writes exactly the seashell
emoji `🐚` (U+1F41A) to `entry.txt` inside the output directory
(`OUTPUT_DIR` env var, or `/output` by default). The emoji is built from
its code point with `chr(0x1F41A)`, so the source never depends on an
editor preserving a literal glyph. Before writing, it enforces the
bounty's gate: exactly 1 code point, within 1–8 characters, not only
whitespace, encoding to exactly 4 UTF-8 bytes. After writing, it reads
the file back and verifies byte-for-byte — and by decoding — that
exactly `🐚`, 4 bytes, no trailing newline, landed on disk.

## How to run

```sh
OUTPUT_DIR=/tmp/vacation-out python3 main.py
cat /tmp/vacation-out/entry.txt
```
