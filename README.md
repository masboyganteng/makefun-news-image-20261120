# The World in One Day — Friday, 20 November 2026

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/masboyganteng/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/masboyganteng/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

A front page summing up the world's news of Friday 20 November 2026 in
one image: the first three-way Trump–Xi–Putin summit in Shenzhen, the
International Court of Justice ruling that Myanmar committed genocide
against the Rohingya, Anthropic's record $81 billion Nasdaq debut,
Cyclone Akvan's landfall in India, and Trump pushing any Iran decision
to 2027 — plus the day's other headlines in the "Also today" strip.

The image is drawn from scratch with Python and PIL (no photos, no
network): `entry.png` (1024×1024, under 1 MiB). `main.py` (Python 3.13,
standard library only) copies it to `/output/entry.png`.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Entry for the [make.fun competition](https://make.fun/bounty/news-image-20261120)
"Sum up 20 November's world news in one image".
