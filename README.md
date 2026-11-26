# The World in One Day — Wednesday 25 November 2026 in one image

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/astergordon/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/astergordon/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A newspaper front page summing up Wednesday 25 November 2026 in one image,
built for the make.fun bounty
[news-image-20261125](https://make.fun/bounty/news-image-20261125).

## The day in seven stories

Lead: the US proposes sweeping new tariffs on 14 trading partners — headline
rates of 20 to 40 percent, capped by existing trade deals, nothing taking
effect before a January 25 hearing — and Wall Street slides on the news.

Also on the page: Iran claims it shot down two US drones over the Strait of
Hormuz; all Cartagena supermarket hostages are freed; Trump says US war
funding against Iran is secured through January; Australia signs a major
security treaty with Solomon Islands; Zelensky says Ukraine needs 115
billion euros in foreign aid for 2027; and Shenzhou-24 docks at Tiangong
with Pakistan's first astronaut.

## How to run it

`main.py` (Python 3.13, standard library only) copies the committed
`entry.png` (1024×1024, under 1 MiB) to the output directory
(`MAKEFUN_OUTPUT_DIR`, default `/output`) and verifies the copy is
byte-identical with a SHA-256 comparison, so repeated runs agree exactly.

## How it is made

The front page is drawn from scratch with Pillow, not pasted from a photo:
the masthead and headlines are set in DejaVu Serif Bold, the decks in
DejaVu Sans, on a plain white page with ruled dividers — the classic
broadsheet look. The lead story gets the full width at the top; the other
six stories sit in a two-column grid below it, each with a small kicker
(HORMUZ, COLOMBIA, WASHINGTON, PACIFIC, KYIV, SPACE) so a reader can scan
the day at a glance. Every fact on the page was checked against reporting
from Wednesday 25 November 2026 before drawing, and the drawing script
asserts that no headline or deck overflows its column.

## Referral

Made with make.fun — [https://make.fun/r/z5e159r3](https://make.fun/r/z5e159r3) (code `z5e159r3`).
