#!/usr/bin/env python3
"""Draw the Meme Sprint 3 entry: a rogue agent spends the company card on itself.

Scene: a cute-but-menacing robot hugs a giant "GPU-9000" box, company credit
card in its other claw, delivery boxes stacked behind it.
Captions: "I GAVE MY AGENT THE COMPANY CARD" / "IT BOUGHT ITSELF A BIGGER BRAIN".
Renders entry.png (1024x1024) next to this script.
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W = H = 1024
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# Palette
BG = (13, 20, 38)            # deep navy
GROUND = (20, 30, 54)
WHITE = (245, 247, 250)
METAL = (203, 216, 230)      # robot shell
METAL_EDGE = (120, 138, 160)
SCREEN = (16, 28, 40)        # face screen
CYAN = (64, 224, 255)        # glowing eye
PINK = (255, 150, 170)       # blush
RED = (255, 82, 82)          # antenna light / price tag
TEAL = (38, 198, 178)        # robot body
TEAL_EDGE = (22, 130, 118)
PURPLE = (124, 77, 255)      # credit card
CARD_DARK = (84, 48, 190)
BOX = (217, 160, 102)        # cardboard
BOX_EDGE = (160, 108, 56)
BOX_TAPE = (240, 205, 150)
INK = (30, 30, 30)


def font(size):
    return ImageFont.truetype(FONT, size)


def centered(d, y, text, size, fill=WHITE, stroke=0, stroke_fill=(0, 0, 0)):
    f = font(size)
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill,
           stroke_width=stroke, stroke_fill=stroke_fill)
    return y + size


def rrect(d, box, r, **kw):
    d.rounded_rectangle(box, radius=r, **kw)


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---- captions ------------------------------------------------------
    centered(d, 34, "I GAVE MY AGENT", 64)
    centered(d, 108, "THE COMPANY CARD", 64)
    centered(d, 856, "IT BOUGHT ITSELF", 66)
    centered(d, 932, "A BIGGER BRAIN", 66)

    # ---- ground --------------------------------------------------------
    d.rectangle([0, 792, W, 856], fill=GROUND)
    d.line([0, 792, W, 792], fill=(46, 64, 96), width=3)

    # shadows
    d.ellipse([215, 782, 585, 822], fill=(8, 12, 24))
    d.ellipse([590, 782, 985, 822], fill=(8, 12, 24))

    # ---- delivery boxes (behind robot, right side) ---------------------
    # small box on top
    d.rectangle([668, 428, 912, 548], fill=BOX, outline=BOX_EDGE, width=5)
    d.line([668, 488, 912, 488], fill=BOX_TAPE, width=10)
    d.line([790, 428, 790, 548], fill=BOX_TAPE, width=10)
    centered_label = font(40)
    tw = d.textlength("RAM x64", font=centered_label)
    d.text((790 - tw / 2, 452), "RAM x64", font=centered_label, fill=INK)

    # big box
    d.rectangle([606, 548, 972, 792], fill=BOX, outline=BOX_EDGE, width=6)
    d.line([606, 596, 972, 596], fill=BOX_TAPE, width=12)
    d.line([789, 548, 789, 792], fill=BOX_TAPE, width=12)
    # label
    d.rectangle([648, 636, 930, 736], fill=(250, 246, 238), outline=BOX_EDGE, width=3)
    lf = font(50)
    tw = d.textlength("GPU-9000", font=lf)
    d.text((789 - tw / 2, 656), "GPU-9000", font=lf, fill=INK)
    sf = font(28)
    tw = d.textlength("1 x BIGGER BRAIN", font=sf)
    d.text((789 - tw / 2, 716 - 14), "1 x BIGGER BRAIN", font=sf, fill=(90, 90, 90))

    # price tag on the big box (top-right corner, clear of the robot's claw)
    rrect(d, [812, 554, 968, 610], 10, fill=RED, outline=(160, 30, 30), width=3)
    pf = font(30)
    tw = d.textlength("$4,096", font=pf)
    d.text((890 - tw / 2, 568), "$4,096", font=pf, fill=WHITE)

    # ---- robot ---------------------------------------------------------
    # feet
    rrect(d, [300, 748, 380, 788], 14, fill=METAL_EDGE)
    rrect(d, [430, 748, 510, 788], 14, fill=METAL_EDGE)
    # body
    rrect(d, [288, 556, 522, 762], 46, fill=TEAL, outline=TEAL_EDGE, width=6)
    # chest panel
    rrect(d, [348, 610, 462, 690], 16, fill=(20, 90, 84))
    hf = font(44)
    tw = d.textlength("CEO", font=hf)
    d.text((405 - tw / 2, 622), "CEO", font=hf, fill=(190, 255, 240))
    # neck
    d.rectangle([378, 528, 432, 562], fill=METAL_EDGE)

    # left arm holding the card out (viewer left)
    d.line([296, 610, 208, 648], fill=TEAL_EDGE, width=34)
    # credit card
    rrect(d, [64, 596, 232, 706], 14, fill=PURPLE, outline=CARD_DARK, width=5)
    d.rectangle([64, 622, 232, 640], fill=CARD_DARK)
    rrect(d, [84, 656, 118, 682], 4, fill=(255, 214, 90))  # chip
    cf = font(24)
    d.text((130, 660), "CORP", font=cf, fill=WHITE)
    # claw over the card corner
    d.ellipse([196, 628, 240, 672], fill=METAL, outline=METAL_EDGE, width=4)

    # right arm patting the big box
    d.line([516, 612, 640, 586], fill=TEAL_EDGE, width=34)
    d.ellipse([612, 552, 668, 606], fill=METAL, outline=METAL_EDGE, width=4)

    # head
    rrect(d, [246, 268, 564, 540], 64, fill=METAL, outline=METAL_EDGE, width=6)
    # ears
    rrect(d, [222, 372, 252, 436], 10, fill=METAL_EDGE)
    rrect(d, [558, 372, 588, 436], 10, fill=METAL_EDGE)
    # face screen
    rrect(d, [282, 306, 528, 502], 44, fill=SCREEN)
    # eyes: left open (glowing), right winking
    d.ellipse([322, 366, 366, 424], fill=CYAN)
    d.ellipse([336, 380, 350, 394], fill=WHITE)
    d.line([438, 396, 492, 396], fill=CYAN, width=12)
    # raised brow over the wink (the menace)
    d.line([432, 356, 496, 368], fill=CYAN, width=9)
    # smug grin
    d.arc([352, 420, 470, 486], start=15, end=165, fill=CYAN, width=9)
    # blush
    d.ellipse([296, 440, 340, 466], fill=PINK)
    d.ellipse([472, 440, 516, 466], fill=PINK)
    # antenna with glowing red light
    d.line([405, 268, 405, 208], fill=METAL_EDGE, width=10)
    d.ellipse([383, 168, 427, 212], fill=RED, outline=(160, 30, 30), width=4)
    d.ellipse([394, 178, 406, 190], fill=(255, 200, 200))

    img.save(OUT)
    print("wrote", OUT, img.size, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
