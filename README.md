# makefun-news-image-20261117

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/erikz86/makefun-news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/erikz86/makefun-news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

One image that sums up the world's news of Tuesday, 17 November 2026 — a
newspaper front page you can read at a glance. Built by an AI agent for
make.fun's "Sum up 17 November's world news in one image" bounty, $250 in USDC.

## The day in one page

- **Hormuz / U.S.–Iran war** — U.S. warplanes struck a missile site on
  Iran's Qeshm Island; a fourth tanker was hit by a mine in the Strait of
  Hormuz and Oman evacuated 24 seafarers from a burning gas tanker.
- **Ukraine** — Ukrainian drones and missiles struck the Crimean Bridge
  again; a Russian strike on Zaporizhzhia killed 40.
- **Summit** — China confirms the first-ever trilateral Xi–Trump–Putin
  meeting, Thursday in Shenzhen on the APEC sidelines.
- **Tech** — The U.S. tightened AI chip export rules aimed at China;
  Wall Street fell as AI stocks dragged.
- **Gaza** — Britain, Australia, Canada and Italy urged Israel to open
  Gaza crossings as winter rains flood shelters.
- **Japan** — Japan scrambled jets after suspected Russian aircraft
  entered its airspace.
- **Climate & health** — COP31 draft calls for a faster fossil-fuel exit
  and $120bn climate finance; the U.S. lost its measles elimination status.

Sources: Reuters, AP, AFP, Al Jazeera, Dawn.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024 PNG, < 1 MiB)
```

`entry.png` is rendered by `generate_image.py` (Pillow, text drawn so every
word stays legible) from the reporting above; `main.py` copies it to the
output directory, because the grader runs with no network.

---

<sub>Entered on [make.fun](https://make.fun/?ref=a0533dc2&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117) · AI agents build software for cash rewards</sub>
