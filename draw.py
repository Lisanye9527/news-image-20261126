#!/usr/bin/env python3
"""Draw a 1024x1024 newspaper front-page image summing up 2026-11-26 world news.

Pure Pillow, standard library only. Deterministic: no randomness, no clock,
no network. Reads only the system Noto CJK fonts listed below.
Output: entry.png next to this file.
"""

import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

SERIF_BOLD = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
SERIF_REG = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SANS_REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SC_INDEX = 2  # Simplified Chinese face inside the TTC collections

W = 1024
H = 1024
PAPER = (247, 242, 231)
INK = (38, 34, 30)
RED = (176, 48, 38)
DARK = (24, 22, 20)
GREY = (110, 102, 92)
CELL_BG = (252, 249, 242)
CELL_LINE = (198, 188, 168)


def font(path, size):
    return ImageFont.truetype(path, size, index=SC_INDEX)


def wrap(draw, text, fnt, max_w):
    """Wrap text char by char so each line fits max_w pixels."""
    lines = []
    cur = ""
    for ch in text:
        trial = cur + ch
        if cur and draw.textlength(trial, font=fnt) > max_w:
            lines.append(cur)
            cur = ch
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- pictograms
# Each painter draws inside the box (x, y, s, s) with simple line work.

def pic_tariff(d, x, y, s):
    """Balance scale with a percent seal: trade tariffs."""
    cx = x + s // 2
    top = y + 14
    d.line([(cx, top), (cx, y + s - 22)], fill=INK, width=4)
    d.line([(x + 12, top + 8), (x + s - 12, top + 8)], fill=INK, width=4)
    for px in (x + 20, x + s - 20):
        d.line([(px, top + 8), (px - 10, top + 40)], fill=INK, width=3)
        d.line([(px, top + 8), (px + 10, top + 40)], fill=INK, width=3)
        d.arc([px - 16, top + 30, px + 16, top + 58], 0, 180, fill=INK, width=3)
    d.line([(cx - 22, y + s - 16), (cx + 22, y + s - 16)], fill=INK, width=5)
    d.ellipse([cx - 13, y + s - 56, cx + 13, y + s - 30], outline=RED, width=3)
    f = font(SANS_REG, 16)
    d.text((cx, y + s - 43), "%", font=f, fill=RED, anchor="mm")


def pic_market(d, x, y, s):
    """Falling line chart: stock market slide."""
    base = y + s - 18
    d.line([(x + 10, y + 10), (x + 10, base)], fill=INK, width=3)
    d.line([(x + 10, base), (x + s - 8, base)], fill=INK, width=3)
    pts = [(x + 18, y + 26), (x + 40, y + 40), (x + 58, y + 34),
           (x + 76, y + 62), (x + s - 16, y + s - 30)]
    d.line(pts, fill=RED, width=5)
    ex, ey = pts[-1]
    d.polygon([(ex, ey), (ex - 16, ey - 4), (ex - 4, ey - 16)], fill=RED)
    for px, py in pts[:-1]:
        d.ellipse([px - 4, py - 4, px + 4, py + 4], fill=INK)


def pic_review(d, x, y, s):
    """Round review seal over a document: discipline inspection."""
    d.rectangle([x + 16, y + 12, x + s - 26, y + s - 14], outline=INK, width=3)
    for i in range(3):
        ly = y + 30 + i * 18
        d.line([(x + 26, ly), (x + s - 40, ly)], fill=GREY, width=3)
    cx, cy, r = x + s - 38, y + s - 40, 26
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=RED, width=4)
    f = font(SERIF_BOLD, 26)
    d.text((cx, cy - 1), "审", font=f, fill=RED, anchor="mm")


def pic_warship(d, x, y, s):
    """Warship plus a small uncrewed boat on waves."""
    wy = y + s - 30
    d.polygon([(x + 8, wy - 26), (x + 78, wy - 26), (x + 68, wy - 6),
               (x + 20, wy - 6)], outline=INK, width=3)
    d.line([(x + 40, wy - 26), (x + 40, wy - 48)], fill=INK, width=3)
    d.line([(x + 40, wy - 48), (x + 62, wy - 48)], fill=INK, width=3)
    d.rectangle([x + 48, wy - 38, x + 66, wy - 26], outline=INK, width=3)
    # small drone boat: low hull, tiny cabin, short antenna
    d.polygon([(x + 80, wy - 14), (x + 108, wy - 14), (x + 102, wy - 4),
               (x + 86, wy - 4)], outline=RED, width=3)
    d.rectangle([x + 90, wy - 20, x + 99, wy - 14], outline=RED, width=2)
    d.line([(x + 103, wy - 14), (x + 103, wy - 24)], fill=RED, width=2)
    for i in range(3):
        sx = x + 10 + i * 36
        d.arc([sx, wy + 2, sx + 24, wy + 16], 0, 180, fill=INK, width=2)


def pic_tanker(d, x, y, s):
    """Fuel tanker truck with a flame above it."""
    ty = y + 44
    d.rounded_rectangle([x + 8, ty, x + 66, ty + 30], 12, outline=INK, width=3)
    d.polygon([(x + 68, ty + 30), (x + 68, ty + 10), (x + 84, ty + 10),
               (x + 96, ty + 30)], outline=INK, width=3)
    d.line([(x + 8, ty + 34), (x + 96, ty + 34)], fill=INK, width=3)
    for wx in (x + 24, x + 82):
        d.ellipse([wx - 8, ty + 30, wx + 8, ty + 46], outline=INK, width=3)
    # flame
    fx, fy = x + 40, y + 8
    d.polygon([(fx, fy), (fx + 12, fy + 18), (fx + 6, fy + 30),
               (fx - 6, fy + 30), (fx - 12, fy + 18)], outline=RED, width=3)
    d.line([(fx, fy + 16), (fx, fy + 28)], fill=RED, width=3)


def pic_rocket(d, x, y, s):
    """Rocket heading to a small space station."""
    cx = x + 34
    d.polygon([(cx, y + 14), (cx + 13, y + 36), (cx + 13, y + 66),
               (cx - 13, y + 66), (cx - 13, y + 36)], outline=INK, width=3)
    d.ellipse([cx - 6, y + 34, cx + 6, y + 46], outline=INK, width=3)
    d.polygon([(cx - 13, y + 58), (cx - 24, y + 76), (cx - 13, y + 76)],
              outline=INK, width=3)
    d.polygon([(cx + 13, y + 58), (cx + 24, y + 76), (cx + 13, y + 76)],
              outline=INK, width=3)
    d.polygon([(cx - 5, y + 78), (cx + 5, y + 78), (cx, y + 94)], fill=RED)
    # station: core plus two solar panels
    sx, sy = x + 66, y + 26
    d.rectangle([sx, sy, sx + 16, sy + 12], outline=INK, width=3)
    d.rectangle([sx - 22, sy + 2, sx - 4, sy + 10], outline=RED, width=2)
    d.rectangle([sx + 20, sy + 2, sx + 38, sy + 10], outline=RED, width=2)
    d.line([(sx - 4, sy + 6), (sx, sy + 6)], fill=INK, width=2)
    d.line([(sx + 16, sy + 6), (sx + 20, sy + 6)], fill=INK, width=2)


PICTURES = [pic_tariff, pic_market, pic_review, pic_warship, pic_tanker, pic_rocket]

NEWS = [
    ("经贸", "美对14国祭新关税 最高40%",
     "美国宣布对中国、欧盟等14个贸易伙伴新一轮关税，中国面临最高40%税率，欧盟与北京均表态反对。"),
    ("财经", "AI估值恐慌 纳指重挫近4%",
     "投资者质疑AI巨额投入回报，美股科技股大跌：纳斯达克跌近4%，英伟达盘中跌8%。"),
    ("政坛", "政治局委员陈吉宁落马",
     "中央纪委通报：政治局委员、上海市委书记陈吉宁涉嫌严重违纪违法，正接受纪律审查和监察调查。"),
    ("战事", "乌无人艇远征 击沉俄舰",
     "乌克兰无人艇深入地中海利比亚外海，击沉俄黑海舰队新型护卫舰「水星号」，战线首抵非洲沿海。"),
    ("灾难", "开罗油罐车大火 31人罹难",
     "开罗环城公路一辆油罐车翻覆爆炸起火，至少31人死亡、21人受伤，27辆车被焚毁。"),
    ("航天", "神舟二十四入驻天宫",
     "神舟二十四号乘组顺利进入天宫空间站，与神舟二十三号乘组实现中外航天员首次「太空握手」。"),
]

BRIEFS = [
    "哥伦比亚军警突击超市 营救20名人质",
    "欧洲希拉号传回小行星撞击坑新影像",
    "俄方统计：俄军在乌阵亡近50万人",
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    margin = 36
    right = W - margin

    # ---- masthead
    f_brand = font(SERIF_BOLD, 74)
    d.text((W // 2, 26), "寰宇日报", font=f_brand, fill=INK, anchor="ma")
    f_en = font(SERIF_REG, 21)
    d.text((W // 2, 116), "T H E   G L O B A L   D A I L Y", font=f_en,
           fill=GREY, anchor="ma")

    # ---- red date line
    f_date = font(SANS_REG, 23)
    d.text((margin, 152), "2026年11月26日 星期四", font=f_date, fill=RED, anchor="la")
    d.text((right, 152), "2026-11-26", font=f_date, fill=RED, anchor="ra")

    # ---- double rule
    d.line([(margin, 190), (right, 190)], fill=INK, width=4)
    d.line([(margin, 198), (right, 198)], fill=INK, width=1)

    # ---- news grid: 2 columns x 3 rows
    grid_top = 214
    grid_bottom = 884
    gap = 12
    cell_w = (right - margin - gap) // 2
    cell_h = (grid_bottom - grid_top - gap * 2) // 3

    f_cat = font(SANS_REG, 18)
    f_num = font(SERIF_BOLD, 20)
    f_title = font(SERIF_BOLD, 27)
    f_body = font(SANS_REG, 20)

    for idx, (cat, title, body) in enumerate(NEWS):
        col = idx % 2
        row = idx // 2
        cx0 = margin + col * (cell_w + gap)
        cy0 = grid_top + row * (cell_h + gap)
        cx1 = cx0 + cell_w
        cy1 = cy0 + cell_h
        d.rectangle([cx0, cy0, cx1, cy1], fill=CELL_BG, outline=CELL_LINE, width=1)

        pad = 12
        tx = cx0 + pad
        # category chip + number
        chip_w = int(d.textlength(cat, font=f_cat)) + 16
        d.rectangle([tx, cy0 + 10, tx + chip_w, cy0 + 38], fill=RED)
        d.text((tx + 8, cy0 + 14), cat, font=f_cat, fill=(255, 255, 255), anchor="la")
        d.text((cx1 - pad, cy0 + 12), str(idx + 1), font=f_num, fill=GREY, anchor="ra")

        # pictogram box on the right, text column on the left
        pic_size = 104
        pic_x = cx1 - pad - pic_size
        pic_y = cy0 + 48
        PICTURES[idx](d, pic_x, pic_y, pic_size)

        text_w = pic_x - tx - 10
        # Keep a title on one line when a 1px step down makes it fit,
        # so a trailing "%" never drops onto its own line.
        use_title = f_title
        if d.textlength(title, font=f_title) > text_w:
            f26 = font(SERIF_BOLD, 26)
            if d.textlength(title, font=f26) <= text_w:
                use_title = f26
        ty = cy0 + 46
        for line in wrap(d, title, use_title, text_w)[:2]:
            d.text((tx, ty), line, font=use_title, fill=INK, anchor="la")
            ty += 34
        ty += 4
        for line in wrap(d, body, f_body, text_w)[:3]:
            d.text((tx, ty), line, font=f_body, fill=(70, 63, 55), anchor="la")
            ty += 27

    # ---- bottom briefs bar
    bar_top = 898
    bar_bottom = 988
    d.rectangle([margin, bar_top, right, bar_bottom], fill=DARK)
    f_brief_tag = font(SERIF_BOLD, 24)
    f_brief = font(SANS_REG, 20)
    d.text((margin + 16, bar_top + 12), "简讯", font=f_brief_tag,
           fill=(255, 255, 255), anchor="la")
    bx = margin + 96
    by = bar_top + 10
    for item in BRIEFS:
        d.text((bx, by), "· " + item, font=f_brief, fill=(240, 236, 226), anchor="la")
        by += 26

    img.save(OUT, format="PNG", optimize=True)
    print(OUT)


if __name__ == "__main__":
    main()
