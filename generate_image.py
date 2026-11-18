"""Build entry.png: a one-page newspaper front page summing up the world news
of Tuesday 17 November 2026. Rendered with Pillow (text drawn, not generated),
so every word is legible and the bytes are deterministic.

Run: python3 generate_image.py  -> writes entry.png (1024x1024, < 1 MiB).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 20)
RED = (178, 28, 28)
BLUE = (29, 78, 216)
GREY = (90, 86, 78)
RULE = (180, 172, 158)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to pixel width, returning lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_para(draw, x, y, text, fnt, width, fill=INK, leading=None):
    leading = leading or int(fnt.size * 1.28)
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 48
    x0, x1 = mx, W - mx

    # --- masthead ---
    y = 34
    d.text((x0, y), "MAKE.FUN  ·  NEWS-IMAGE  ·  WORLD NEWS IN ONE IMAGE",
           font=font(SANS_B, 17), fill=GREY)
    y += 30
    title_font = font(SERIF_B, 96)
    title_w = d.textlength("THE WORLD", font=title_font)
    d.text((x0, y), "THE WORLD", font=title_font, fill=INK)
    date_font = font(SERIF_B, 30)
    date_w = d.textlength("17 NOV 2026", font=date_font)
    date_x = max(x0 + title_w + 24, x1 - date_w)
    d.text((date_x, y + 66), "17 NOV 2026", font=date_font, fill=RED)
    y += 118
    d.text((x0, y), "TUESDAY, 17 NOVEMBER 2026  —  ONE DAY, ONE PAGE",
           font=font(SANS_B, 19), fill=INK)
    y += 32
    d.line([(x0, y), (x1, y)], fill=INK, width=4)
    y += 6
    d.line([(x0, y), (x1, y)], fill=INK, width=1)
    y += 20

    # --- lead story ---
    d.rectangle([x0, y, x0 + 8, y + 178], fill=RED)
    lx = x0 + 24
    d.text((lx, y), "HORMUZ  ·  U.S.–IRAN WAR", font=font(SANS_B, 19), fill=RED)
    y += 30
    y = draw_para(d, lx, y,
                  "U.S. strikes Iran's Qeshm Island as tanker war in the Strait escalates",
                  font(SERIF_B, 37), x1 - lx, leading=46)
    y += 6
    y = draw_para(d, lx, y,
                  "U.S. warplanes hit a missile site on Qeshm in retaliation for attacks on "
                  "American personnel. A fourth tanker was hit by a mine in the Strait of "
                  "Hormuz, and Oman evacuated 24 seafarers from a burning gas tanker.",
                  font(SERIF, 21), x1 - lx, leading=27)
    y += 14
    d.line([(x0, y), (x1, y)], fill=RULE, width=1)
    y += 18

    # --- story grid: 2 columns x 3 rows ---
    stories = [
        ("UKRAINE", RED,
         "Crimean Bridge struck again; Kyiv hit by missiles",
         "Ukrainian drones and missiles hit the bridge overnight. A Russian strike on "
         "Zaporizhzhia killed 40; another on an aid centre killed 26."),
        ("SUMMIT", BLUE,
         "Xi, Trump and Putin to meet in Shenzhen",
         "China confirms the first-ever trilateral summit of the three leaders, on "
         "Thursday on the sidelines of the APEC meeting."),
        ("TECH", BLUE,
         "U.S. tightens AI chip export rules on China",
         "New rules close a loophole on advanced chips bought abroad. Wall Street fell "
         "as AI stocks dragged, with Nvidia in focus."),
        ("GAZA", RED,
         "West urges Israel to open Gaza crossings",
         "Britain, Australia, Canada and Italy call the situation catastrophic as winter "
         "rains flood shelters and food runs low."),
        ("JAPAN", BLUE,
         "Japan scrambles jets over Russian airspace breach",
         "Tokyo protests after two suspected Russian aircraft entered its airspace at the "
         "start of Tuesday."),
        ("CLIMATE & HEALTH", RED,
         "COP31 draft: faster fossil-fuel exit, $120bn finance",
         "Antalya negotiators publish an 18-page draft deal. Separately, the U.S. loses "
         "its measles elimination status."),
    ]
    col_w = (x1 - x0 - 32) // 2
    row_h = 158
    for i, (kicker, color, head, body) in enumerate(stories):
        cx = x0 + (i % 2) * (col_w + 32)
        cy = y + (i // 2) * row_h
        d.text((cx, cy), kicker, font=font(SANS_B, 16), fill=color)
        cy2 = draw_para(d, cx, cy + 24, head, font(SERIF_B, 23), col_w, leading=28)
        draw_para(d, cx, cy2 + 4, body, font(SERIF, 18), col_w, leading=23)
        if i % 2 == 0:
            d.line([(cx + col_w + 16, cy), (cx + col_w + 16, cy + row_h - 16)],
                   fill=RULE, width=1)
    y += 3 * row_h + 6

    # --- footer ---
    d.line([(x0, y), (x1, y)], fill=INK, width=2)
    y += 12
    d.text((x0, y), "Sources: Reuters · AP · AFP · Al Jazeera · Dawn",
           font=font(SANS, 16), fill=GREY)
    y += 24
    d.text((x0, y), "Compiled from reporting on 17 Nov 2026  ·  make.fun news-image-20261117",
           font=font(SANS, 16), fill=GREY)

    img.save("entry.png", "PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
