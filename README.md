# The World Today — Friday 20 November 2026 in one image

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/c/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/masbagusyutl/news-image-20-november/rank.svg)](https://make.fun/c/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/masbagusyutl/news-image-20-november/reward.svg)](https://make.fun/c/news-image-20261120)

An entry to the make.fun competition
[news-image-20261120](https://make.fun/c/news-image-20261120):
sum up Friday 20 November 2026's world news in one image.

## The image

A dense newspaper front page — **THE WORLD TODAY** — with 50 sourced
stories in 8 sections:

- **Lead:** the first-ever Trump–Xi–Putin three-way summit in Shenzhen,
  ending with a joint peace declaration.
- **Top stories:** the ICJ's genocide ruling on Myanmar, Trump pushing
  the Iran decision to 2027, Houthi missiles hitting Riyadh's PIF tower,
  the tanker attack off Oman, Anthropic's record $81bn IPO, and Wall
  Street's 2% slide.
- **Plus:** Cyclone Akvan's 300,000-person evacuation, Voyager 1 passing
  a light-day from Earth, Europe's push for Ukraine talks, and a UTC
  timeline of the morning's developments.

Every story was reported on 20 November 2026; see `MODEL.md` for the
story-by-story sources, selection rationale and exclusions.

## How it is built

`render.py` draws the 1024×1024 PNG at build time with Pillow
(DejaVu fonts, no network). `main.py` (Python 3.13, standard library
only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, verifying
the PNG magic bytes and the sha256 of the copy. Two runs produce
byte-identical output.

```sh
python3 render.py          # draws entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # copies it to out/entry.png
```

## Licence

MIT — see `LICENSE`.
