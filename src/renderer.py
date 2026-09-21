from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
BG = (247, 245, 239)
TEXT = (28, 31, 36)
ACCENT = (50, 73, 102)
MUTED = (219, 215, 206)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(size, bold=False):
    return ImageFont.truetype(FONT_BOLD if bold else FONT_REG, size)

def wrap(draw, text, fnt, max_width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        test = (line + " " + word).strip()
        if draw.textbbox((0,0), test, font=fnt)[2] <= max_width:
            line = test
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines

def art(draw, variant=1):
    if variant == 1:
        draw.ellipse((650, 80, 1100, 530), fill=(225, 229, 234))
        draw.rectangle((720, 310, 1040, 1080), fill=(231, 224, 214))
        draw.line((610, 170, 1010, 620), fill=ACCENT, width=16)
    else:
        for i in range(5):
            x = 650 + i * 70
            draw.rectangle((x, 180 + i*70, x+42, 980-i*60), fill=(210-i*7, 218-i*5, 226-i*3))
        draw.ellipse((720, 760, 1000, 1040), outline=ACCENT, width=18)

def render_slide(path: Path, numero: int, titulo: str, corpo: str, visual: bool):
    img = Image.new("RGB", (W,H), BG)
    d = ImageDraw.Draw(img)

    d.rectangle((0,0,W,24), fill=ACCENT)
    d.text((70,65), f"{numero:02d}", font=font(28, True), fill=ACCENT)

    if visual:
        art(d, 1 if numero == 1 else 2)
        maxw = 560
    else:
        maxw = 900

    tf = font(58 if numero == 1 else 50, True)
    y = 180
    for line in wrap(d, titulo, tf, maxw):
        d.text((70,y), line, font=tf, fill=TEXT)
        y += 72

    if corpo:
        y += 34
        bf = font(34, False)
        for line in wrap(d, corpo, bf, maxw):
            d.text((70,y), line, font=bf, fill=TEXT)
            y += 48

    d.line((70, 1220, 1010, 1220), fill=MUTED, width=2)
    d.text((70,1250), "UASSI MOGONE", font=font(24, True), fill=ACCENT)

    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, quality=95)
