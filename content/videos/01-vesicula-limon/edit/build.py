#!/usr/bin/env python3
"""Video 01 — vesícula/limón. Builds edit/final.mp4 (1080x1920, 30fps).

Pipeline (video-use hard rules): per-segment extract with zoom + grade + 30ms
fades -> lossless concat -> one full-length RGBA graphics track overlaid from
t=0 -> two-pass loudnorm. Cuts sit in silence gaps measured with silencedetect
(no transcript available yet), padded ~100ms.

Usage: python3 build.py [--preview]
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

EDIT = Path(__file__).resolve().parent
RAW = EDIT.parent / "raw"
W, H, FPS = 1080, 1920, 30
PREVIEW = "--preview" in sys.argv

# Brand (brand-profile.json)
TERRACOTA = (139, 58, 42)
GOLD = (196, 146, 42)
PETROLEO = (42, 107, 124)
CAFE = (61, 43, 31)
CREMA = (245, 237, 227)
WHITE = (250, 250, 248)

FONT_BLACK = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
FONT_BOLD = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
FONT_MED = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
FONT_EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"

GRADE = "eq=contrast=1.06:saturation=1.06:brightness=0.01,unsharp=5:5:0.5:5:5:0"

# (source, start, end, zoom keyframes [(src_time, zoom)], beat)
# Zoom alternates across every cut so jump cuts read as intentional.
SEGMENTS = [
    ("clip01", 1.06, 5.03, [(0, 1.00)], "HOOK pregunta"),
    ("clip01", 5.38, 8.14, [(0, 1.22)], "HOOK 'No.' punch-in"),
    ("clip02", 1.12, 8.28, [(0, 1.00)], "MITO"),
    ("clip03", 0.68, 10.35, [(0, 1.12), (6.05, 1.00)], "COMO SABER (abre al señalar)"),
    ("clip04", 0.95, 6.30, [(0, 1.12)], "ALARMA signos"),
    ("clip04", 6.86, 8.67, [(0, 1.25)], "ALARMA 'urgencias' punch-in"),
    ("clip05", 0.51, 7.34, [(0, 1.00)], "SOLUCION"),
    ("clip06", 0.65, 5.95, [(0, 1.12)], "CIERRE"),
]
END_HOLD = 1.5  # freeze last frame under the end card


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, **kw)


def zoom_chain(label_in, z):
    """Crop toward the face (upper-center) then scale to 1080x1920."""
    if z == 1.0:
        crop = ""
    else:
        crop = f"crop=iw/{z}:ih/{z}:(iw-iw/{z})/2:(ih-ih/{z})*0.32,"
    return f"[{label_in}]{crop}scale={W}:{H}:flags=lanczos,setsar=1,{GRADE}"


def extract(i, seg, out):
    src, start, end, keys, _ = seg
    dur = end - start
    last = i == len(SEGMENTS) - 1
    n = len(keys)
    parts = [f"[0:v]split={n}" + "".join(f"[v{k}]" for k in range(n))] if n > 1 else []
    if n == 1:
        parts.append(zoom_chain("0:v", keys[0][1]) + "[vz]")
    else:
        for k, (_, z) in enumerate(keys):
            parts.append(zoom_chain(f"v{k}", z) + f"[z{k}]")
        cur = "z0"
        for k in range(1, n):
            t = keys[k][0] - start
            parts.append(f"[{cur}][z{k}]overlay=enable='gte(t,{t:.3f})'[o{k}]")
            cur = f"o{k}"
        parts.append(f"[{cur}]null[vz]")
    vtail = f"[vz]tpad=stop_mode=clone:stop_duration={END_HOLD}[vout]" if last else "[vz]null[vout]"
    parts.append(vtail)
    af = f"afade=t=in:st=0:d=0.03,afade=t=out:st={dur - 0.03:.3f}:d=0.03"
    if last:
        af += f",apad=pad_dur={END_HOLD}"
    parts.append(f"[0:a]{af}[aout]")
    crf = "22" if PREVIEW else "18"
    run([
        "ffmpeg", "-v", "error", "-y", "-ss", f"{start:.3f}", "-t", f"{dur:.3f}",
        "-i", str(RAW / f"{src}.mov"), "-filter_complex", ";".join(parts),
        "-map", "[vout]", "-map", "[aout]",
        "-c:v", "libx264", "-preset", "medium", "-crf", crf, "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(out),
    ])


def probe_dur(p):
    return float(subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)]))


# ---------------------------------------------------------------- graphics --

def font(path, size):
    return ImageFont.truetype(path, size)


def emoji(ch, size):
    f = ImageFont.truetype(FONT_EMOJI, 109)
    im = Image.new("RGBA", (136, 128), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((0, 0), ch, font=f, embedded_color=True)
    im = im.crop(im.getbbox())
    return im.resize((round(im.width * size / im.height), size), Image.LANCZOS)


def text_size(fnt, s):
    l, t, r, b = fnt.getbbox(s)
    return r - l, b - t, l, t


def pill(lines, bg, pad=(44, 26), radius=34, gap=12, icon=None, max_w=980):
    """lines: [(text, font, color)]; optional left icon (RGBA image)."""
    sizes = [text_size(f, s) for s, f, _ in lines]
    tw = max(s[0] for s in sizes)
    th = sum(s[1] for s in sizes) + gap * (len(lines) - 1)
    iw = icon.width + 22 if icon else 0
    w = min(max_w, tw + iw + pad[0] * 2)
    h = max(th, icon.height if icon else 0) + pad[1] * 2
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius, fill=bg + (240,))
    if icon:
        im.alpha_composite(icon, (pad[0], (h - icon.height) // 2))
    y = (h - th) // 2
    for (s, f, c), (sw, sh, ox, oy) in zip(lines, sizes):
        d.text((pad[0] + iw - ox, y - oy), s, font=f, fill=c)
        y += sh + gap
    return im


def hook_card():
    f = font(FONT_BLACK, 92)
    s = "¿LIMÓN Y ACEITE?"
    sw, sh, ox, oy = text_size(f, s)
    im = Image.new("RGBA", (sw + 80, sh + 70), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, im.width - 1, im.height - 1), 30, fill=WHITE + (245,))
    d.text((40 - ox, 35 - oy), s, font=f, fill=CAFE)
    return im


def hook_card_struck():
    im = hook_card()
    d = ImageDraw.Draw(im)
    y = im.height // 2 + 4
    d.line((28, y, im.width - 28, y), fill=TERRACOTA, width=12)
    return im


def x_stamp():
    return emoji("❌", 120)


def myth_card():
    f1, f2 = font(FONT_BLACK, 60), font(FONT_BOLD, 46)
    top = pill([("“LIMPIEZA” DE VESÍCULA", f1, WHITE)], TERRACOTA)
    d = ImageDraw.Draw(top)
    d.line((30, top.height // 2 + 4, top.width - 30, top.height // 2 + 4), fill=GOLD, width=9)
    bot = pill([("= grumos de aceite,", f2, CAFE), ("NO piedras", font(FONT_BLACK, 56), TERRACOTA)], CREMA)
    lem, oli = emoji("🍋", 92), emoji("🫒", 92)
    w = max(top.width, bot.width)
    im = Image.new("RGBA", (w, lem.height + top.height + bot.height + 40), (0, 0, 0, 0))
    im.alpha_composite(lem, (w // 2 - lem.width - 10, 0))
    im.alpha_composite(oli, (w // 2 + 10, 0))
    im.alpha_composite(top, ((w - top.width) // 2, lem.height + 14))
    im.alpha_composite(bot, ((w - bot.width) // 2, lem.height + top.height + 30))
    return im


def list_items():
    f = font(FONT_BOLD, 56)
    items = [("📍", "Arriba a la derecha"), ("🍔", "Después de comer grasa"), ("⏱️", "+30 min o hacia la espalda")]
    return [pill([(t, f, CAFE)], CREMA, pad=(34, 20), icon=emoji(e, 70)) for e, t in items]


def alert_card():
    f1, f2 = font(FONT_BLACK, 54), font(FONT_BOLD, 48)
    return pill([
        ("ACUDE A URGENCIAS SI:", f1, GOLD),
        ("Fiebre", f2, WHITE), ("Piel o ojos amarillos", f2, WHITE), ("Dolor que no cede", f2, WHITE),
    ], TERRACOTA, pad=(48, 34), gap=18, icon=emoji("⚠️", 110))


def urgencias_card():
    return pill([("URGENCIAS", font(FONT_BLACK, 96), WHITE)], TERRACOTA, pad=(50, 30), icon=emoji("🚑", 110))


def solution_card():
    return pill([
        ("LAPAROSCOPÍA", font(FONT_BLACK, 64), GOLD),
        ("Heridas pequeñas", font(FONT_BOLD, 52), WHITE),
        ("Casi siempre: a casa en 1–2 días", font(FONT_MED, 46), WHITE),
    ], PETROLEO, pad=(48, 32), gap=14)


def name_tag():
    return pill([("Dr. Alben Rosas", font(FONT_BLACK, 48), WHITE),
                 ("Cirujano General · La Paz, BCS", font(FONT_MED, 34), CREMA)],
                PETROLEO, pad=(36, 20), gap=8)


def end_card():
    im = Image.new("RGBA", (W, H), CREMA + (255,))
    d = ImageDraw.Draw(im)
    d.ellipse((W // 2 - 130, 430, W // 2 + 130, 690), outline=GOLD, width=10)
    fA = font("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 150)
    sw, sh, ox, oy = text_size(fA, "A")
    d.text((W // 2 - sw // 2 - ox, 560 - sh // 2 - oy), "A", font=fA, fill=TERRACOTA)

    def center(s, f, y, c):
        sw, sh, ox, oy = text_size(f, s)
        d.text(((W - sw) // 2 - ox, y - oy), s, font=f, fill=c)

    center("Dr. Alben Rosas", font(FONT_BLACK, 92), 780, CAFE)
    center("CIRUJANO GENERAL", font(FONT_BOLD, 50), 905, TERRACOTA)
    center("La Paz, Baja California Sur", font(FONT_MED, 42), 985, CAFE)
    d.line((W // 2 - 160, 1075, W // 2 + 160, 1075), fill=GOLD, width=5)
    wa = pill([("WhatsApp  663 437 0584", font(FONT_BLACK, 56), WHITE)], PETROLEO, pad=(50, 30), icon=emoji("💬", 70))
    im.alpha_composite(wa, ((W - wa.width) // 2, 1130))
    center("Vesícula · Hernias · Cirugía laparoscópica", font(FONT_MED, 38), 1310, CAFE)
    center("Céd. Prof. 11017193", font(FONT_BOLD, 40), 1395, CAFE)
    return im


def ease_out_back(t, s=1.70158):
    t -= 1
    return t * t * ((s + 1) * t + s) + 1


def ease_out_cubic(t):
    return 1 - (1 - t) ** 3


class Layer:
    """Element shown from t0 to t1, centered at (cx, cy) with a pop-in."""

    def __init__(self, img, t0, t1, cx, cy, pop=0.28, fade_out=0.15, kind="pop"):
        self.img, self.t0, self.t1, self.cx, self.cy = img, t0, t1, cx, cy
        self.pop, self.fade_out, self.kind = pop, fade_out, kind

    def draw(self, canvas, t):
        if not (self.t0 <= t < self.t1):
            return
        a = 1.0
        if t > self.t1 - self.fade_out:
            a = max(0.0, (self.t1 - t) / self.fade_out)
        p = min(1.0, (t - self.t0) / self.pop)
        if self.kind == "fade":
            a *= ease_out_cubic(p)
            scale = 1.0
        else:
            scale = 0.55 + 0.45 * ease_out_back(p)
            a *= min(1.0, p * 2.5)
        img = self.img
        if abs(scale - 1) > 1e-3:
            img = img.resize((max(1, round(img.width * scale)), max(1, round(img.height * scale))), Image.BILINEAR)
        if a < 1:
            img = img.copy()
            img.putalpha(img.getchannel("A").point(lambda v: round(v * a)))
        canvas.alpha_composite(img, (round(self.cx - img.width / 2), round(self.cy - img.height / 2)))


def build_layers(starts, total):
    s = starts  # output start time of each segment
    items = list_items()
    speech_end_s8 = s[7] + (4.77 - 0.65)
    return [
        Layer(hook_card(), 0.15, s[1], W / 2, 330, fade_out=0.001),
        Layer(hook_card_struck(), s[1], s[2], W / 2, 330, pop=0.001),
        Layer(x_stamp(), s[1] + 0.05, s[2], W / 2 + 430, 250, pop=0.22),
        Layer(name_tag(), 0.6, s[1] - 0.1, W / 2, 1330, kind="fade"),
        Layer(myth_card(), s[2] + 0.5, s[3] - 0.05, W / 2, 1480),
        Layer(items[0], s[3] + 0.7, s[4] - 0.05, W / 2, 260),
        Layer(items[1], s[3] + 2.7, s[4] - 0.05, W / 2, 410),
        Layer(items[2], s[3] + 4.7, s[4] - 0.05, W / 2, 560),
        Layer(alert_card(), s[4] + 0.6, s[5], W / 2, 1250),
        Layer(urgencias_card(), s[5] + 0.02, s[6] - 0.02, W / 2, 1250, pop=0.2),
        Layer(solution_card(), s[6] + 0.8, s[7] - 0.05, W / 2, 1250),
        Layer(end_card(), speech_end_s8 + 0.15, total + 1, W / 2, H / 2, pop=0.35, fade_out=0.001, kind="fade"),
    ]


def render_graphics(layers, total, out):
    n = round(total * FPS)
    p = subprocess.Popen([
        "ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}",
        "-r", str(FPS), "-i", "-", "-c:v", "qtrle", str(out)], stdin=subprocess.PIPE)
    blank = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for i in range(n):
        t = i / FPS
        c = blank.copy()
        for L in layers:
            L.draw(c, t)
        p.stdin.write(c.tobytes())
    p.stdin.close()
    p.wait()


# ------------------------------------------------------------------- main --

def main():
    seg_dir = EDIT / "clips_graded"
    seg_dir.mkdir(exist_ok=True)
    paths = []
    for i, seg in enumerate(SEGMENTS):
        out = seg_dir / f"seg_{i:02d}.mp4"
        extract(i, seg, out)
        paths.append(out)
    starts, t = [], 0.0
    for p in paths:
        starts.append(t)
        t += probe_dur(p)
    total = t
    lst = seg_dir / "concat.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in paths))
    base = EDIT / "base.mp4"
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(base)])

    gfx = EDIT / "graphics.mov"
    render_graphics(build_layers(starts, total), total, gfx)

    # Two-pass loudnorm to -14 LUFS / -1 dBTP (social).
    pre = "highpass=f=80,acompressor=threshold=-20dB:ratio=2.5:attack=10:release=150"
    m = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(base), "-af",
                        f"{pre},loudnorm=I=-14:TP=-1:LRA=9:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1:LRA=9:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
          f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")

    out = EDIT / ("preview.mp4" if PREVIEW else "final.mp4")
    run(["ffmpeg", "-v", "error", "-y", "-i", str(base), "-i", str(gfx), "-filter_complex",
         f"[1:v]format=rgba,setpts=PTS-STARTPTS[g];[0:v][g]overlay=0:0:format=auto,format=yuv420p[v];"
         f"[0:a]{pre},{ln},aresample=48000[a]",
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "slow", "-crf", "19",
         "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)])

    print(json.dumps({"output": str(out), "total_s": round(total, 2),
                      "segment_starts": [round(x, 2) for x in starts]}, indent=1))


if __name__ == "__main__":
    main()
