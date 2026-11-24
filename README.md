# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/rrmmllnn/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/rrmmllnn/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)

An entry for the [Say What Actually Broke](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes one line of software error copy to `/output/entry.txt`:
a single honest sentence that names the real failure (a bad deploy
broke the login page), tells the user their password is fine and the
code is not, and says what happens next (rollback, retry in five
minutes). One line, 130 characters, no padding.

## Run it

```sh
python3 main.py
```

It writes the entry to `/output/entry.txt` (override with the
`ENTRY_OUTPUT` environment variable). Pure Python standard library,
no network, and repeated runs produce byte-identical output.
