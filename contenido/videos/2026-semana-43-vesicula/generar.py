"""Genera el proyecto HyperFrames del Reel de vesícula (semana 43)."""
import json, pathlib, sys

P = pathlib.Path(sys.argv[1])
W, H = 1080, 1920
END = 124.0          # corte del video (antes de bloopers y outro de CapCut)
TOTAL = END + 4.5    # + tarjeta de cierre

FONTS = """
    @font-face { font-family: 'Cormorant Garamond'; font-weight: 500; src: url('assets/fonts/cormorant-garamond-latin-500-normal.woff2'); }
    @font-face { font-family: 'Cormorant Garamond'; font-weight: 600; src: url('assets/fonts/cormorant-garamond-latin-600-normal.woff2'); }
    @font-face { font-family: 'Cormorant Garamond'; font-style: italic; font-weight: 500; src: url('assets/fonts/cormorant-garamond-latin-500-italic.woff2'); }
    @font-face { font-family: 'Jost'; font-weight: 300; src: url('assets/fonts/jost-latin-300-normal.woff2'); }
    @font-face { font-family: 'Jost'; font-weight: 400; src: url('assets/fonts/jost-latin-400-normal.woff2'); }
    @font-face { font-family: 'Jost'; font-weight: 500; src: url('assets/fonts/jost-latin-500-normal.woff2'); }
    @font-face { font-family: 'Jost'; font-weight: 600; src: url('assets/fonts/jost-latin-600-normal.woff2'); }
"""

BASE_CSS = """
    #root { position: absolute; inset: 0; }
    .card {
      position: absolute; left: 60px; right: 60px; top: 790px;
      padding: 34px 40px 38px; border-radius: 30px;
      background: rgba(250, 250, 248, 0.95);
      border-left: 10px solid #C4922A;
      box-shadow: 0 18px 50px rgba(20, 30, 40, 0.28);
      color: #3D2B1F; font-family: 'Jost', sans-serif;
    }
    .kicker { font-family: 'Jost', sans-serif; font-weight: 600; font-size: 30px; letter-spacing: 0.14em;
              text-transform: uppercase; color: #A87A1E; margin: 0 0 10px; }
    .title  { font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 74px; line-height: 1.02;
              color: #2A6B7C; margin: 0; }
    .item   { display: flex; align-items: baseline; gap: 18px; font-size: 42px; font-weight: 400;
              line-height: 1.2; margin-top: 18px; }
    .dot    { flex: none; width: 16px; height: 16px; border-radius: 50%; background: #C4922A;
              transform: translateY(-6px); }
    .em     { font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 500; font-size: 56px;
              color: #8B3A2A; margin-top: 20px; line-height: 1.05; }
    .alarm  { background: rgba(139, 58, 42, 0.96); border-left-color: #F5EDE3; color: #FAFAF8; }
    .alarm .kicker { color: #F5EDE3; }
    .alarm .title  { color: #FAFAF8; }
    .alarm .dot    { background: #F5EDE3; }
    .alarm .em     { color: #F5EDE3; font-family: 'Jost', sans-serif; font-style: normal; font-weight: 600; font-size: 46px; }
"""


def card(cid, start, dur, kicker, title, items=(), variant="", visible_at_zero=False):
    """items: lista de (tiempo_absoluto, html, clase)."""
    rows, tweens = [], []
    for n, (t_abs, html, cls) in enumerate(items, 1):
        iid = f"{cid}-i{n}"
        if cls == "item":
            rows.append(f'<div id="{iid}" class="item"><span class="dot"></span><span>{html}</span></div>')
        else:
            rows.append(f'<div id="{iid}" class="{cls}">{html}</div>')
        t = max(0.0, round(t_abs - start, 2))
        tweens.append(
            f'tl.fromTo("#{iid}", {{ opacity: 0, y: 26 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "power3.out" }}, {t});'
        )
    head = []
    if kicker:
        head.append(f'<p id="{cid}-k" class="kicker">{kicker}</p>')
    if title:
        head.append(f'<h2 id="{cid}-t" class="title">{title}</h2>')
    fade_in = (
        f'tl.fromTo("#{cid}-card", {{ opacity: 1 }}, {{ opacity: 1, duration: 0.01 }}, 0);'
        if visible_at_zero
        else f'tl.fromTo("#{cid}-card", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power2.out" }}, 0);'
    )
    return cid, start, dur, f"""<template>
  <style>{FONTS}{BASE_CSS}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}">
    <div id="{cid}-card" class="clip card {variant}" data-start="0" data-duration="{dur}">
      {''.join(head)}
      {''.join(rows)}
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {fade_in}
    {' '.join(tweens)}
    tl.to("#{cid}-card", {{ opacity: 0, duration: 0.35, ease: "power2.in" }}, {round(dur - 0.4, 2)});
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""


def nametag(cid, start, dur):
    return cid, start, dur, f"""<template>
  <style>{FONTS}
    #root {{ position: absolute; inset: 0; }}
    .tag {{ position: absolute; left: 44px; top: 190px; padding: 18px 26px 20px; border-radius: 22px;
            background: rgba(61, 43, 31, 0.86); border-left: 6px solid #C4922A; }}
    .tag-name {{ font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 46px; color: #FAFAF8; line-height: 1; }}
    .tag-role {{ font-family: 'Jost', sans-serif; font-weight: 400; font-size: 30px; color: #C4922A;
                 letter-spacing: 0.06em; margin-top: 8px; }}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}">
    <div id="{cid}-box" class="clip tag" data-start="0" data-duration="{dur}">
      <div id="{cid}-name" class="tag-name">Dr. Alben Rosas</div>
      <div id="{cid}-role" class="tag-role">Cirujano General · La Paz, BCS</div>
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo("#{cid}-box", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: "power2.out" }}, 0);
    tl.fromTo("#{cid}-name", {{ opacity: 0, x: -20 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, 0.1);
    tl.fromTo("#{cid}-role", {{ opacity: 0, x: -20 }}, {{ opacity: 1, x: 0, duration: 0.5, ease: "power3.out" }}, 0.3);
    tl.to("#{cid}-box", {{ opacity: 0, duration: 0.35, ease: "power2.in" }}, {round(dur - 0.4, 2)});
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""


def endcard(cid, start, dur):
    lines = [
        ("ec-l1", "ec-small", "Soy el"),
        ("ec-l2", "ec-name", "Dr. Alben Rosas"),
        ("ec-l3", "ec-role", "Cirujano General · Céd. Prof. 11017193"),
        ("ec-l4", "ec-rule", ""),
        ("ec-l5", "ec-cta", "Agenda tu valoración"),
        ("ec-l6", "ec-info", "WhatsApp 663 437 0584"),
        ("ec-l7", "ec-info", "Médica del Cortés · La Paz, BCS"),
        ("ec-l8", "ec-handle", "@dralbenrosas"),
    ]
    rows = "\n      ".join(f'<div id="{i}" class="{c}">{t}</div>' for i, c, t in lines)
    tweens = " ".join(
        f'tl.fromTo("#{i}", {{ opacity: 0, y: 24 }}, {{ opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }}, {round(0.15 + n * 0.12, 2)});'
        for n, (i, _, _) in enumerate(lines)
    )
    return cid, start, dur, f"""<template>
  <style>{FONTS}
    #root {{ position: absolute; inset: 0; }}
    .ec {{ position: absolute; inset: 0; background: #F5EDE3; display: flex; flex-direction: column;
           align-items: center; justify-content: center; text-align: center; padding: 0 80px; }}
    .ec-small  {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 500; font-size: 52px; color: #3D2B1F; }}
    .ec-name   {{ font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 104px; color: #8B3A2A; line-height: 1; margin-top: 6px; }}
    .ec-role   {{ font-family: 'Jost', sans-serif; font-weight: 400; font-size: 32px; color: #3D2B1F; letter-spacing: 0.04em; margin-top: 22px; }}
    .ec-rule   {{ width: 160px; height: 3px; background: #C4922A; margin: 54px 0 48px; }}
    .ec-cta    {{ font-family: 'Jost', sans-serif; font-weight: 600; font-size: 46px; color: #FAFAF8; background: #2A6B7C;
                  padding: 22px 46px; border-radius: 999px; }}
    .ec-info   {{ font-family: 'Jost', sans-serif; font-weight: 400; font-size: 36px; color: #3D2B1F; margin-top: 26px; }}
    .ec-handle {{ font-family: 'Jost', sans-serif; font-weight: 500; font-size: 34px; color: #C4922A; margin-top: 40px; letter-spacing: 0.04em; }}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}">
    <div id="{cid}-bg" class="clip ec" data-start="0" data-duration="{dur}">
      {rows}
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo("#{cid}-bg", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.35, ease: "power2.out" }}, 0);
    {tweens}
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""


scenes = [
    card("hook", 0.0, 5.6, "", "¿Dolor después de comer?",
         [(0.0, "Podría ser tu vesícula", "em")], visible_at_zero=True),
    nametag("nombre", 6.0, 7.0),
    card("mito", 19.5, 8.0, "No siempre es gastritis", "",
         [(20.6, "Sal de uvas, antiácidos, analgésicos…", "item"),
          (24.0, "solo enmascaran el síntoma", "em")]),
    card("senales", 28.5, 13.3, "Señales de vesícula", "",
         [(29.6, "Dolor bajo la costilla derecha", "item"),
          (32.4, "Se va a la espalda o al hombro", "item"),
          (36.4, "Después de comida grasosa", "item")]),
    card("ultra", 43.0, 13.5, "¿Cómo saberlo?", "Un ultrasonido",
         [(46.8, "de hígado y vías biliares", "item"),
          (50.4, "y llévaselo a tu cirujano", "item")]),
    card("piedras", 57.0, 3.4, "", "Piedras + dolor",
         [(57.6, "= momento de operarse", "em")]),
    card("sindolor", 61.0, 18.4, "¿Piedras sin dolor?", "",
         [(63.2, "Te las encontraron, pero nunca te han dolido", "item"),
          (70.6, "Tranquilo: no siempre se opera", "item"),
          (74.6, "Vigilancia con un cirujano de confianza", "item")]),
    card("alarma", 81.6, 22.4, "Datos de alarma", "",
         [(85.0, "Piel u ojos amarillos", "item"),
          (88.6, "Orina muy oscura", "item"),
          (92.6, "Dolor con fiebre", "item"),
          (95.4, "→ Acude a urgencias", "em")], variant="alarm"),
    card("dudas", 105.5, 12.5, "¿Tienes dudas?", "Déjalas en comentarios", []),
    endcard("cierre", END, TOTAL - END),
]

hosts = []
for n, (cid, start, dur, html) in enumerate(scenes):
    (P / "compositions" / f"{cid}.html").write_text(html)
    track = 1 + n % 3 if cid != "cierre" else 4
    hosts.append(
        f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" '
        f'data-start="{start}" data-duration="{dur}" data-track-index="{track}" data-track-kind="graphics" '
        f'data-width="{W}" data-height="{H}" style="z-index: {n + 2}"></div>'
    )

index = f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <title>Reel vesícula · semana 43</title>
    <script src="vendor/gsap.min.js"></script>
    <style>
      html, body {{ margin: 0; background: #000; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="{W}" data-height="{H}">
      <video id="reel" class="clip" src="assets/reel.mp4" data-start="0" data-duration="{END}" data-track-index="0"
        playsinline data-has-audio="true"
        style="position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; object-fit: contain; z-index: 1"></video>
{chr(10).join(hosts)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
(P / "index.html").write_text(index)
print(f"{len(scenes)} escenas, duración {TOTAL}s")
