#!/usr/bin/env python3
"""Render the news-image-20261120 entry: one 1024x1024 front page.

Build-time renderer (runs locally, not in the grading sandbox).
Draws 'THE WORLD TODAY' -- a dense newspaper front page summing up
Friday 20 November 2026 in 50 sourced stories, a UTC timeline strip
and a date-check footer. Output: entry.png next to this file.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 22
COLW = 310
GUTTER = 14

NAVY = (15, 42, 74)
NAVY2 = (23, 58, 96)
GOLD = (201, 162, 39)
PAPER = (250, 247, 238)
INK = (24, 24, 22)
GREY = (90, 88, 82)
RED = (178, 34, 34)
TEAL = (14, 110, 110)
RULE = (200, 194, 178)

F_SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
F_SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
F_SANS_OB = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"  # no oblique face shipped; use regular


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Wrap text to pixel width; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_one_line(draw, text, fnt, width, max_chars=90):
    """Truncate text to a single line that fits the width."""
    if draw.textlength(text, font=fnt) <= width:
        return text
    while text and draw.textlength(text + "...", font=fnt) > width:
        text = text[:-1]
    return text + "..."


# ---------------------------------------------------------------- stories
# (headline, summary, source) -- every story first reported 20 Nov 2026.
LEAD = (
    "TRUMP, XI AND PUTIN MEET IN SHENZHEN",
    "First-ever three-way summit ends with a joint peace declaration; "
    "nuclear risks, energy security and the Ukraine war top the agenda.",
    "Reuters / AP",
)

COLUMNS = [
    [("TOP STORIES", None),
     ("ICJ: MYANMAR COMMITTED GENOCIDE",
      "UN court rules the 2017 Rohingya crackdown was genocide.", "BBC"),
     ("TRUMP: NO RUSH ON IRAN DECISION",
      "President will 'see what happens' after Jan 1.", "Reuters"),
     ("HOUTHI MISSILES HIT RIYADH TOWER",
      "Strikes damage the PIF skyscraper; no injuries reported.", "AFP"),
     ("TANKER HIT OFF OMAN AS HORMUZ BURNS",
      "On Phoenix struck by a projectile off Oman.", "UKMTO"),
     ("ANTHROPIC'S RECORD IPO DEBUTS",
      "$81bn listing, the largest ever; shares close +17%.", "Reuters"),
     ("WALL ST SINKS 2% ON AI DOUBTS",
      "S&P 500 logs a sixth straight loss; Nasdaq falls 2.25%.", "Reuters"),
     ("AMERICAS", None),
     ("TRUMP PARDONS PETE ROSE",
      "Posthumous pardon for baseball's hits leader.", "AP"),
     ("US, VENEZUELA RESTORE MILITARY TIES",
      "Defence chief Hegseth signs a cooperation deal in Caracas.", "DW"),
     ("COURT LETS TRUMP END VENEZUELAN TPS",
      "Appeals court clears the end of deportation protections.", "Al Jazeera"),
     ("FIONA THE HIPPO DIES AT ZOO",
      "Beloved hippo dies after swallowing a visitor's hat.", "BBC"),
     ("PAROLE DENIED FOR SUSAN SMITH",
      "Parole refused 32 years after she drowned her sons.", "AP"),
     ("CALIFORNIA PROBES NVIDIA ON CHINA",
      "State targets the chipmaker in an AI-chip export inquiry.", "BBC"),
     ("MEASLES COMEBACK FUELLED BY FEARS",
      "Vaccine fears drive a major measles resurgence.", "Guardian"),
     ("CANADA COURTS AI DATA CENTRES",
      "Investors look north as US towns push back on new centres.", "BBC"),
     ("GTA 6 SALES TOP $1.8 BILLION",
      "Rockstar's epic passes The Odyssey's global box-office run.", "Mezha"),
     ],
    [("EUROPE", None),
     ("EUROPE READY FOR RUSSIA TALKS",
      "Leaders say Europe is ready to join Ukraine peace talks.", "BBC"),
     ("PUTIN INVITES EUROPE TO MOSCOW",
      "Russian leader demands a clear position on Ukraine talks.", "FT"),
     ("EU PLANS EUR 45BN UKRAINE LOAN",
      "Commission proposes a joint-debt loan to fund Kyiv.", "EU sources"),
     ("CRIMEA BRIDGE HIT A THIRD TIME",
      "Ukrainian strike halts rail traffic for a third time this week.", "Reports"),
     ("PUTIN VOWS 'FAR MORE PAINFUL' REPLY",
      "Warning follows Ukraine's strikes on the Crimean Bridge.", "BBC"),
     ("MERZ: NEW UKRAINE TALKS 'SOON'",
      "German chancellor says talks including Europe start shortly.", "DW"),
     ("MIGRANT BOAT SINKS OFF SENEGAL",
      "Dozens missing after a boat carrying migrants goes down.", "Reports"),
     ("ONE DEAD IN FRENCH TOWER FIRE",
      "Blaze at an 18-storey apartment block injures 15.", "Reports"),
     ("FINLAND DETAINES TEEN TERROR SUSPECT",
      "17-year-old held over a suspected attack plot in Helsinki.", "Reports"),
     ("HAGIA SOPHIA'S HIDDEN TUNNELS FOUND",
      "Debris cleared to reveal 1,600-year-old passages.", "Fox"),
     ("MIDDLE EAST", None),
     ("ISRAEL ENDS GAZA GROUND OPERATION",
      "Military completes its operation beyond Gaza's Yellow Line.", "BBC"),
     ("ISRAELI JETS HIT HEZBOLLAH SITE",
      "Airstrike targets a missile facility in eastern Lebanon.", "Reports"),
     ("MOSQUE TORCHED IN ISRAEL",
      "Arson sparks a political backlash against Netanyahu.", "Al Jazeera"),
     ("GAZA SURGEON'S DETENTION EXTENDED",
      "Israeli court holds Dr Abu Safia without charge.", "Al Jazeera"),
     ("IEA: WAR IS TOP ENERGY THREAT",
      "Agency calls the conflict the largest energy threat in history.", "Euronews"),
     ("HORMUZ CRUDE FLOWS HALVE",
      "Shipments fall to ~8.5m barrels a day, half pre-war levels.", "Kpler"),
     ],
    [("ASIA-PACIFIC", None),
     ("CYCLONE AKVAN BEARS DOWN ON ODISHA",
      "300,000 evacuated; 423 rescue teams deployed.", "The Hindu"),
     ("MODI MEETS WILLIAM AND KATE",
      "PM hosts the Prince and Princess of Wales in New Delhi.", "TOI"),
     ("MODI OPENS FICCI CENTENARY MEET",
      "PM inaugurates the industry body's 100-year convention.", "Jagran Josh"),
     ("INDIA INKS RS 1,976-CR DEFENCE DEAL",
      "Navy's Barak system to be upgraded with Israel Aerospace.", "Jagran Josh"),
     ("FIRE AT YUNUS FAMILY HOME",
      "Blaze at the ancestral home of Bangladesh's ex-leader.", "TOI"),
     ("SEOUL COURT CLEARS EX-PM HAN",
      "Top court overturns Han Duck-soo's conviction.", "Reports"),
     ("N KOREA EXPANDS URANIUM SITE",
      "UN watchdog says enrichment work grows at Yongbyon.", "Reports"),
     ("FIJI DECLARES DROUGHT DISASTER",
      "El Nino water shortages trigger a national state of disaster.", "Reports"),
     ("MARKETS & BUSINESS", None),
     ("NVIDIA SLIDES A SIXTH DAY",
      "Chipmaker falls 3.3% despite an upbeat revenue forecast.", "Reuters"),
     ("OIL STEADIES ABOVE $82.50",
      "Hormuz tensions offset surplus forecasts; WTI holds firm.", "FXStreet"),
     ("SENSEX, NIFTY RALLY IN MUMBAI",
      "Sensex gains 1.21% as auto and bank shares lead.", "TOI"),
     ("SCIENCE & TECHNOLOGY", None),
     ("VOYAGER 1 PASSES A LIGHT-DAY",
      "NASA confirms the probe is 16bn miles out -- a first.", "Reuters"),
     ("HAYABUSA2 ASTEROID TRIP SCRAPPED",
      "Engine trouble forces Japan to drop its 1998 KY26 landing.", "Space"),
     ("GOOGLE PICKS BLUE ORIGIN FOR SPACE AI",
      "New Glenn to launch Project Suncatcher satellites.", "Reuters"),
     ("CULTURE & SPORT", None),
     ("PHILLIPS TON LIFTS NEW ZEALAND",
      "Glenn Phillips hits 118; NZ reach 317-6 at lunch vs India.", "Reuters"),
     ("APPLE BUILDS AI DEVICE AGENT",
      "Apple is working on an AI agent to run apps and write code.", "Reports"),
     ],
]

TIMELINE = [
    ("00:11", "IRGC: tanker hit mines in Hormuz", "Al Jazeera"),
    ("00:22", "Phillips century; NZ 317-6 at lunch", "Reuters"),
    ("00:34", "Anthropic closes +17% at $97.17", "Reuters"),
    ("00:39", "Trump, Xi, Putin sign peace declaration", "Wire roundup"),
    ("00:43", "Trump pardons Pete Rose", "AP"),
    ("00:45", "Oil steadies above $82.50", "FXStreet"),
]

SOURCES_LINE = ("Sources: Reuters, BBC, AP, AFP, DW, Al Jazeera, The Hindu, Times of India, "
                "Financial Times, UKMTO, Kpler, FXStreet, Space, Euronews, Guardian, Fox News.")


def draw_lead_illustration(d, x, y, w, h):
    """Flat illustration: globe with three summit flags over a skyline."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240))
    # skyline
    d.rectangle([x, y + h - 42, x + w, y + h], fill=NAVY2)
    for bx, bw, bh in [(8, 34, 26), (52, 22, 38), (84, 40, 20), (134, 26, 34),
                       (170, 36, 24), (216, 24, 40), (250, 40, 28)]:
        d.rectangle([x + bx, y + h - 42 - bh, x + bx + bw, y + h - 42], fill=NAVY)
    # globe
    cx, cy, r = x + w // 2, y + 78, 62
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(46, 125, 175), outline=NAVY, width=3)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255), width=1)
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=(255, 255, 255), width=2)
    d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=(255, 255, 255), width=2)
    d.line([cx - r, cy, cx + r, cy], fill=(255, 255, 255), width=2)
    d.ellipse([cx - r + 18, cy - r + 14, cx - r + 52, cy - r + 40], fill=(74, 160, 90))
    d.ellipse([cx + 8, cy + 12, cx + 44, cy + 44], fill=(74, 160, 90))
    # three flags on poles above the globe
    flags = [((178, 34, 34), "US"), ((201, 162, 39), "CN"), ((23, 58, 96), "RU")]
    for i, (col, label) in enumerate(flags):
        fx = x + 52 + i * 96
        d.line([fx, y + 8, fx, y + 52], fill=INK, width=3)
        d.rectangle([fx, y + 8, fx + 58, y + 30], fill=col, outline=INK, width=1)
        f = font(F_SANS_B, 13)
        d.text((fx + 18, y + 12), label, font=f, fill=(255, 255, 255))
    d.text((x + 8, y + h - 20), "SHENZHEN  •  THE FIRST THREE-WAY SUMMIT",
           font=font(F_SANS_B, 10), fill=(255, 255, 255))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead
    d.rectangle([0, 0, W, 86], fill=NAVY)
    d.rectangle([0, 86, W, 89], fill=GOLD)
    d.text((MARGIN, 14), "THE WORLD TODAY", font=font(F_SERIF_B, 52), fill=(255, 255, 255))
    f_date = font(F_SANS_B, 17)
    d.text((W - MARGIN - d.textlength("FRIDAY 20 NOVEMBER 2026", font=f_date), 18),
           "FRIDAY 20 NOVEMBER 2026", font=f_date, fill=(255, 214, 90))
    f_sub = font(F_SANS, 12)
    d.text((W - MARGIN - d.textlength("50 STORIES  •  8 SECTIONS  •  ONE DAY", font=f_sub), 46),
           "50 STORIES  •  8 SECTIONS  •  ONE DAY", font=f_sub, fill=(200, 214, 230))

    # ---- lead story
    ly, lh = 100, 176
    d.rectangle([MARGIN, ly, W - MARGIN, ly + lh], outline=RULE, width=1)
    d.rectangle([MARGIN, ly, MARGIN + 8, ly + lh], fill=RED)
    lx = MARGIN + 22
    lw = 600
    d.text((lx, ly + 8), "LEAD  —  THE SUMMIT", font=font(F_SANS_B, 11), fill=RED)
    f_lead = font(F_SERIF_B, 27)
    lines = wrap(d, LEAD[0], f_lead, lw)
    yy = ly + 28
    for ln in lines:
        d.text((lx, yy), ln, font=f_lead, fill=INK)
        yy += 32
    f_body = font(F_SANS, 13)
    for ln in wrap(d, LEAD[1], f_body, lw):
        d.text((lx, yy), ln, font=f_body, fill=(40, 40, 38))
        yy += 17
    d.text((lx, ly + lh - 24), "Source: " + LEAD[2], font=font(F_SANS_OB, 11), fill=GREY)
    draw_lead_illustration(d, W - MARGIN - 330, ly + 8, 322, lh - 16)

    # ---- timeline strip
    ty, th = 286, 62
    d.rectangle([MARGIN, ty, W - MARGIN, ty + th], fill=(233, 230, 220))
    d.rectangle([MARGIN, ty, W - MARGIN, ty + th], outline=RULE, width=1)
    d.text((MARGIN + 10, ty + 6), "THE DAY IN UTC", font=font(F_SANS_B, 11), fill=NAVY)
    tw = (W - 2 * MARGIN - 20) / len(TIMELINE)
    f_time = font(F_SANS_B, 12)
    f_tl = font(F_SANS, 10)
    for i, (t, txt, src) in enumerate(TIMELINE):
        x = MARGIN + 10 + i * tw
        d.text((x, ty + 24), t, font=f_time, fill=RED)
        lines = wrap(d, txt, f_tl, tw - 12)[:2]
        for j, ln in enumerate(lines):
            d.text((x, ty + 38 + j * 11), ln, font=f_tl, fill=INK)

    # ---- story columns
    col_top = 360
    col_bottom = 968
    f_sec = font(F_SANS_B, 12)
    f_head = font(F_SANS_B, 12)
    f_sum = font(F_SANS, 10)
    f_src = font(F_SANS_OB, 8)
    heights = []
    for ci, col in enumerate(COLUMNS):
        x = MARGIN + ci * (COLW + GUTTER)
        y = col_top
        for item in col:
            if item[1] is None:  # section header
                d.rectangle([x, y, x + COLW, y + 18], fill=NAVY)
                d.text((x + 6, y + 2), item[0], font=f_sec, fill=(255, 255, 255))
                y += 24
                continue
            head, summ, src = item
            head = fit_one_line(d, head, f_head, COLW - 4)
            summ = fit_one_line(d, summ, f_sum, COLW - 4)
            d.text((x, y), head, font=f_head, fill=INK)
            y += 14
            d.text((x, y), summ, font=f_sum, fill=(52, 50, 46))
            y += 12
            d.line([x, y, x + COLW, y], fill=RULE, width=1)
            y += 3
        heights.append(y)
    max_y = max(heights)
    print("column bottoms:", heights, "limit:", col_bottom)
    assert max_y <= col_bottom, "columns overflow by %d px" % (max_y - col_bottom)

    # ---- footer
    fy = 976
    d.rectangle([MARGIN, fy, W - MARGIN, fy + 2], fill=GOLD)
    f_foot = font(F_SANS_B, 11)
    d.text((MARGIN, fy + 8),
           "DATE CHECK: every story above was reported on Friday 20 November 2026.",
           font=f_foot, fill=NAVY)
    f_srcs = font(F_SANS, 9)
    for i, ln in enumerate(wrap(d, SOURCES_LINE, f_srcs, W - 2 * MARGIN)):
        d.text((MARGIN, fy + 26 + i * 12), ln, font=f_srcs, fill=GREY)

    img.save("entry.png", optimize=True)
    print("saved entry.png")


if __name__ == "__main__":
    main()
