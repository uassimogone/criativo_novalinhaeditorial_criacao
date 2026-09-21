from pathlib import Path
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps

W, H = 1080, 1350
MARGIN = 76

FAMILY_DARK = "EDITORIAL_DARK"
FAMILY_MINIMAL = "MINIMAL_TYPO"
FAMILY_LIGHT = "EDITORIAL_LIGHT"
FAMILY_COMPARE = "COMPARISON"
FAMILY_PHOTO = "PHOTO_PROTAGONIST"
FAMILY_DATA = "DATA_EDITORIAL"

FAMILIES = {FAMILY_DARK, FAMILY_MINIMAL, FAMILY_LIGHT, FAMILY_COMPARE, FAMILY_PHOTO, FAMILY_DATA}


def _find_font(candidates):
    for p in candidates:
        if Path(p).exists():
            return p
    return "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


FONT_SANS = _find_font([
    "/usr/share/fonts/truetype/lato/Lato-Regular.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
])
FONT_SANS_BOLD = _find_font([
    "/usr/share/fonts/truetype/lato/Lato-Heavy.ttf",
    "/usr/share/fonts/truetype/lato/Lato-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
])
FONT_SERIF = _find_font([
    "/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
])
FONT_SERIF_BOLD = _find_font([
    "/usr/share/fonts/truetype/liberation2/LiberationSerif-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
])


def font(size, role="sans"):
    path = {
        "sans": FONT_SANS,
        "sans_bold": FONT_SANS_BOLD,
        "serif": FONT_SERIF,
        "serif_bold": FONT_SERIF_BOLD,
    }[role]
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_width):
    words = str(text or "").split()
    lines, line = [], ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if not line or draw.textlength(candidate, font=fnt) <= max_width:
            line = candidate
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def _crop_photo(path):
    with Image.open(path) as src:
        return ImageOps.fit(src.convert("RGB"), (W, H), method=Image.Resampling.LANCZOS, centering=(0.5, 0.45))


def _overlay(img, opacity=150, color=(0, 0, 0)):
    shade = Image.new("RGBA", img.size, color + (opacity,))
    return Image.alpha_composite(img.convert("RGBA"), shade).convert("RGB")


def _brand(draw, numero, dark=True):
    ink = (242, 239, 230) if dark else (30, 31, 33)
    muted = (183, 177, 165) if dark else (110, 110, 110)
    draw.text((MARGIN, 42), "UASSI MOGONE", font=font(22, "sans_bold"), fill=ink)
    draw.line((MARGIN, 84, W-MARGIN, 84), fill=muted, width=1)
    draw.text((W-MARGIN-62, 42), f"{numero:02d}/05", font=font(18, "sans"), fill=muted)


def _headline(draw, titulo, x, y, width, dark=True, serif=True, max_size=72):
    color = (246, 242, 232) if dark else (28, 29, 31)
    role = "serif_bold" if serif else "sans_bold"
    size = max_size
    while size >= 42:
        f = font(size, role)
        lines = wrap(draw, titulo, f, width)
        if len(lines) <= 5:
            break
        size -= 4
    lh = int(size * 1.08)
    for line in lines:
        draw.text((x, y), line, font=f, fill=color)
        y += lh
    return y


def _body(draw, corpo, x, y, width, dark=True):
    if not corpo:
        return y
    color = (224, 221, 214) if dark else (65, 66, 70)
    f = font(30, "sans")
    for line in wrap(draw, corpo, f, width):
        draw.text((x, y), line, font=f, fill=color)
        y += 41
    return y


def _render_dark(numero, titulo, corpo, visual):
    img = _crop_photo(visual) if visual else Image.new("RGB", (W,H), (18,20,23))
    if visual:
        img = ImageEnhance.Color(img).enhance(0.72)
        img = ImageEnhance.Contrast(img).enhance(1.14)
        img = _overlay(img, 145)
    d = ImageDraw.Draw(img)
    _brand(d, numero, True)
    y = 170
    y = _headline(d, titulo, MARGIN, y, 760 if visual else 900, True, True, 74 if numero == 1 else 66)
    if corpo:
        y += 26
        _body(d, corpo, MARGIN, y, 700, True)
    d.line((MARGIN, H-105, W-MARGIN, H-105), fill=(124,119,110), width=1)
    return img


def _render_minimal(numero, titulo, corpo):
    bg = (244,241,233)
    ink = (25,26,28)
    img = Image.new("RGB", (W,H), bg)
    d = ImageDraw.Draw(img)
    _brand(d, numero, False)
    d.rectangle((MARGIN, 160, MARGIN+16, 255), fill=(166,31,36))
    y = 300
    y = _headline(d, titulo, MARGIN, y, 880, False, False, 80)
    if corpo:
        y += 42
        _body(d, corpo, MARGIN, y, 760, False)
    d.text((MARGIN, H-130), "TRABALHO • NEGÓCIOS • IDEIAS • VIDA", font=font(18,"sans_bold"), fill=(105,105,105))
    return img


def _render_light(numero, titulo, corpo, visual):
    img = Image.new("RGB", (W,H), (247,244,235))
    d = ImageDraw.Draw(img)
    _brand(d, numero, False)
    if visual:
        photo = _crop_photo(visual).crop((0,0,W,H//2)).resize((W,H//2))
        img.paste(photo, (0,H//2))
        d = ImageDraw.Draw(img)
        d.rectangle((0,H//2-90,W,H//2+40), fill=(247,244,235))
    y = 165
    y = _headline(d, titulo, MARGIN, y, 880, False, True, 68)
    if corpo:
        y += 28
        _body(d, corpo, MARGIN, y, 820, False)
    d.line((MARGIN, H-95, W-MARGIN, H-95), fill=(40,40,40), width=2)
    return img


def _render_compare(numero, titulo, corpo, visual):
    img = Image.new("RGB", (W,H), (236,233,225))
    d = ImageDraw.Draw(img)
    _brand(d, numero, False)
    d.rectangle((0, 120, W//2, H), fill=(32,35,38))
    d.rectangle((W//2, 120, W, H), fill=(244,241,233))
    if visual:
        photo = _crop_photo(visual).resize((W//2, H-120))
        photo = _overlay(photo, 105)
        img.paste(photo, (0,120))
        d = ImageDraw.Draw(img)
    d.text((MARGIN, 155), "PROMESSA", font=font(20,"sans_bold"), fill=(236,232,222))
    d.text((W//2+42, 155), "REALIDADE", font=font(20,"sans_bold"), fill=(45,45,45))
    y = 270
    lines = wrap(d, titulo, font(56,"serif_bold"), 420)
    for i,line in enumerate(lines):
        fill=(244,239,227) if i < max(1,len(lines)//2) else (36,37,39)
        x=MARGIN if i < max(1,len(lines)//2) else W//2+42
        d.text((x,y),line,font=font(56,"serif_bold"),fill=fill)
        y += 68
    if corpo:
        d.text((W//2+42, 830), corpo, font=font(27,"sans"), fill=(65,66,70))
    return img


def _render_photo(numero, titulo, corpo, visual):
    img = _crop_photo(visual) if visual else Image.new("RGB",(W,H),(38,39,40))
    img = _overlay(img, 90 if visual else 0)
    d = ImageDraw.Draw(img)
    _brand(d, numero, True)
    box_y = H-520
    d.rounded_rectangle((45, box_y, W-45, H-55), radius=12, fill=(12,13,15,195) if img.mode=="RGBA" else (17,18,20))
    y = box_y+52
    y = _headline(d, titulo, 80, y, 900, True, True, 62)
    if corpo:
        y += 18
        _body(d, corpo, 80, y, 840, True)
    return img


def _render_data(numero, titulo, corpo):
    img = Image.new("RGB",(W,H),(249,247,241))
    d = ImageDraw.Draw(img)
    _brand(d, numero, False)
    y=165
    y=_headline(d,titulo,MARGIN,y,880,False,True,64)
    y+=55
    d.line((MARGIN,y,W-MARGIN,y),fill=(28,29,31),width=3)
    y+=55
    if corpo:
        parts=corpo.split("•")
        for idx,part in enumerate(parts[:3], start=1):
            d.text((MARGIN,y),f"{idx:02d}",font=font(48,"serif_bold"),fill=(151,38,42))
            _body(d,part.strip(),MARGIN+105,y+4,760,False)
            y+=155
    d.text((MARGIN,H-160),"MENOS DECORAÇÃO. MAIS LEITURA.",font=font(22,"sans_bold"),fill=(95,95,95))
    return img


def render_slide(path: Path, numero: int, titulo: str, corpo: str, family: str, visual_path: Path | None = None):
    family = family if family in FAMILIES else FAMILY_LIGHT
    visual = visual_path if visual_path and Path(visual_path).exists() else None
    if family == FAMILY_DARK:
        img = _render_dark(numero,titulo,corpo,visual)
    elif family == FAMILY_MINIMAL:
        img = _render_minimal(numero,titulo,corpo)
    elif family == FAMILY_LIGHT:
        img = _render_light(numero,titulo,corpo,visual)
    elif family == FAMILY_COMPARE:
        img = _render_compare(numero,titulo,corpo,visual)
    elif family == FAMILY_PHOTO:
        img = _render_photo(numero,titulo,corpo,visual)
    else:
        img = _render_data(numero,titulo,corpo)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(path, "PNG", optimize=True)
