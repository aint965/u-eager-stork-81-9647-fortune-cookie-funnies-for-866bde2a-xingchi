# Fortune Cookie Funnies for Engineers

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/release/python-3130/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Entry for the [Fortune Cookie Funnies for Engineers](https://make.fun/bounty/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a) competition on make.fun.

## The fortune

> You will finally delete that ancient TODO, and discover it was load-bearing.

## How it works

`main.py` writes that single line, deterministically, to `/output/entry.txt`
(or `$OUTPUT_DIR/entry.txt` when `OUTPUT_DIR` is set). No network, no randomness,
no dependencies — just Python 3.13 and the standard library.

```sh
python3 main.py
```
