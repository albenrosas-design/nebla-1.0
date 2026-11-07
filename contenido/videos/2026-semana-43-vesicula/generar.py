"""Genera el proyecto HyperFrames del Reel de vesícula (semana 43), v2.

Uso: python3 generar.py <carpeta-del-proyecto>
Después: npx hyperframes media-treatment ... (grade cálido) y npx hyperframes render.
"""
import pathlib, sys

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

SHADOW = "0 2px 4px rgba(20,12,6,0.55), 0 4px 22px rgba(20,12,6,0.55)"

# Texto sin recuadro: anclado abajo (termina en y≈1265, justo arriba de los subtítulos de CapCut),
# con un degradado suave detrás solo mientras hay texto.
TEXT_CSS = f"""
    #root {{ position: absolute; inset: 0; }}
    .scrim {{ position: absolute; left: 0; top: 760px; width: 1080px; height: 600px;
              background: linear-gradient(to bottom, rgba(28,18,12,0) 0%, rgba(28,18,12,0.5) 50%, rgba(28,18,12,0.42) 82%, rgba(28,18,12,0) 100%); }}
    .txt {{ position: absolute; left: 64px; right: 64px; bottom: 655px; display: flex; flex-direction: column;
            color: #FAFAF8; font-family: 'Jost', sans-serif; text-shadow: {SHADOW}; }}
    .kicker {{ font-weight: 600; font-size: 32px; letter-spacing: 0.14em; text-transform: uppercase; color: #F0C877; margin: 0 0 6px; }}
    .title  {{ font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 86px; line-height: 1.0; margin: 0; }}
    .item   {{ display: flex; align-items: baseline; gap: 18px; font-size: 46px; font-weight: 500; line-height: 1.18; margin-top: 14px; }}
    .dot    {{ flex: none; width: 16px; height: 16px; border-radius: 50%; background: #F0C877; transform: translateY(-7px);
               box-shadow: 0 2px 8px rgba(20,12,6,0.6); }}
    .em     {{ font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 500; font-size: 64px;
               color: #F7DDA8; margin-top: 12px; line-height: 1.04; }}
"""


def text(cid, start, dur, kicker="", title="", items=(), visible_at_zero=False):
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
    a = 1 if visible_at_zero else 0
    return cid, start, dur, "text", f"""<template>
  <style>{FONTS}{TEXT_CSS}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}">
    <div id="{cid}-wrap" class="clip" data-start="0" data-duration="{dur}" data-layout-allow-caption-zone>
      <div id="{cid}-scrim" class="scrim"></div>
      <div id="{cid}-txt" class="txt">
        {''.join(head)}
        {''.join(rows)}
      </div>
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo("#{cid}-wrap", {{ opacity: {a} }}, {{ opacity: 1, duration: {0.01 if a else 0.4}, ease: "power2.out" }}, 0);
    {' '.join(tweens)}
    tl.to("#{cid}-wrap", {{ opacity: 0, duration: 0.35, ease: "power2.in" }}, {round(dur - 0.4, 2)});
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""


def nametag(cid, start, dur):
    return cid, start, dur, "text", f"""<template>
  <style>{FONTS}
    #root {{ position: absolute; inset: 0; }}
    .tag {{ position: absolute; left: 52px; top: 196px; text-shadow: {SHADOW}; }}
    .tag-name {{ font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 54px; color: #FAFAF8; line-height: 1; }}
    .tag-role {{ font-family: 'Jost', sans-serif; font-weight: 500; font-size: 30px; color: #F0C877;
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


# ---------- B-roll ilustrado (panel superior; deja visibles los subtítulos de abajo) ----------

BR_CSS = """
    #root { position: absolute; inset: 0; }
    .br { position: absolute; left: 0; top: 0; width: 1080px; height: 1300px; overflow: hidden;
          background: radial-gradient(ellipse at 50% 38%, #5A3E2C 0%, #34241A 62%, #261A12 100%);
          -webkit-mask-image: linear-gradient(to bottom, #000 86%, transparent 100%);
          mask-image: linear-gradient(to bottom, #000 86%, transparent 100%); }
    .br svg { position: absolute; left: 0; top: 0; width: 1080px; height: 1300px; }
    .lbl { font-family: 'Jost', sans-serif; font-weight: 500; font-size: 34px; fill: #F5EDE3; letter-spacing: 0.02em; }
    .lbl-k { font-family: 'Jost', sans-serif; font-weight: 600; font-size: 30px; fill: #F0C877; letter-spacing: 0.14em; }
    .mono { font-family: 'IBM Plex Mono', monospace; font-size: 28px; fill: #CFC6B8; }
"""


def broll(cid, start, dur, svg, tweens):
    return cid, start, dur, "broll", f"""<template>
  <style>{FONTS}{BR_CSS}
  </style>
  <div id="root" data-composition-id="{cid}" data-width="{W}" data-height="{H}">
    <div id="{cid}-panel" class="clip br" data-start="0" data-duration="{dur}" data-layout-allow-overflow>
      {svg}
    </div>
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    tl.fromTo("#{cid}-panel", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.25, ease: "power2.out" }}, 0);
    tl.fromTo("#{cid}-art", {{ scale: 1.0, transformOrigin: "540px 650px" }}, {{ scale: 1.06, duration: {dur}, ease: "none" }}, 0);
    {tweens}
    tl.to("#{cid}-panel", {{ opacity: 0, duration: 0.25, ease: "power2.in" }}, {round(dur - 0.3, 2)});
    window.__timelines["{cid}"] = tl;
  </script>
</template>
"""


def ft(sel, frm, to, t, d=0.5, ease="power3.out", ir=True):
    extra = "" if ir else ", immediateRender: false"
    return f'tl.fromTo("{sel}", {frm}, {{ ...{to}, duration: {d}, ease: "{ease}"{extra} }}, {t});'


def br_pastillas(start=13.0, dur=4.6):
    c = "brpast"
    bubbles = "".join(
        f'<circle id="{c}-b{n}" cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#F5EDE3" stroke-width="3" opacity="0.8"/>'
        for n, (x, y, r) in enumerate([(470, 780, 10), (520, 820, 7), (560, 760, 12), (600, 830, 8), (505, 870, 6), (575, 880, 9)])
    )
    svg = f"""<svg viewBox="0 0 1080 1300"><g id="{c}-art">
      <text class="lbl-k" x="540" y="250" text-anchor="middle">¿INDIGESTIÓN?</text>
      <path d="M400 560 L680 560 L650 960 Q646 990 616 990 L464 990 Q434 990 430 960 Z" fill="rgba(245,237,227,0.06)" stroke="#C4922A" stroke-width="6" stroke-linejoin="round"/>
      <path d="M418 690 L662 690 L646 960 Q643 978 620 978 L460 978 Q437 978 434 960 Z" fill="rgba(42,107,124,0.35)"/>
      {bubbles}
      <g id="{c}-cap1"><rect x="160" y="700" width="180" height="70" rx="35" fill="#F5EDE3"/><path d="M250 700 L305 700 Q340 700 340 735 Q340 770 305 770 L250 770 Z" fill="#8B3A2A"/></g>
      <g id="{c}-cap2"><rect x="760" y="800" width="170" height="66" rx="33" fill="#F5EDE3"/><path d="M845 800 L897 800 Q930 800 930 833 Q930 866 897 866 L845 866 Z" fill="#C4922A"/></g>
      <g id="{c}-tab"><circle cx="820" cy="640" r="58" fill="#F5EDE3"/><line x1="772" y1="640" x2="868" y2="640" stroke="#C9BBA8" stroke-width="5"/></g>
      <text id="{c}-l" class="lbl" x="540" y="1120" text-anchor="middle">Sal de uvas · antiácidos · analgésicos</text>
    </g></svg>"""
    tw = [ft(f"#{c}-cap1", "{ opacity: 0, x: -60, rotation: -20 }", "{ opacity: 1, x: 0, rotation: -8 }", 0.2, 0.6),
          ft(f"#{c}-cap2", "{ opacity: 0, x: 60, rotation: 20 }", "{ opacity: 1, x: 0, rotation: 10 }", 0.4, 0.6),
          ft(f"#{c}-tab", "{ opacity: 0, scale: 0.6, transformOrigin: '820px 640px' }", "{ opacity: 1, scale: 1 }", 0.55, 0.5),
          ft(f"#{c}-l", "{ opacity: 0, y: 20 }", "{ opacity: 1, y: 0 }", 1.0, 0.5)]
    for n in range(6):
        tw.append(ft(f"#{c}-b{n}", "{ y: 0, opacity: 0.85 }", "{ y: -200, opacity: 0 }", round(0.2 + n * 0.35, 2), 2.4, "none"))
    return broll(c, start, dur, svg, " ".join(tw))


def br_anatomia(start=29.0, dur=6.2):
    c = "branat"
    svg = f"""<svg viewBox="0 0 1080 1300"><g id="{c}-art"><g transform="translate(108 40) scale(0.8)">
      <path d="M455 190 Q460 285 330 312 Q236 336 228 440 L262 930 Q276 1040 350 1120 L730 1120 Q804 1040 818 930 L852 440 Q844 336 750 312 Q620 285 625 190"
            fill="rgba(245,237,227,0.05)" stroke="#E8DCCB" stroke-width="5" stroke-linecap="round"/>
      <path d="M330 520 Q540 430 750 520 M318 600 Q540 500 762 600 M310 680 Q540 575 770 680" fill="none" stroke="rgba(232,220,203,0.35)" stroke-width="4"/>
      <path d="M335 720 Q430 650 540 590 Q650 650 745 720" fill="none" stroke="#E8DCCB" stroke-width="5" stroke-linecap="round"/>
      <path id="{c}-liver" d="M300 650 Q330 600 470 610 Q610 618 660 660 Q570 735 430 760 Q330 772 300 712 Z"
            fill="#6A4A24" stroke="#C4922A" stroke-width="5"/>
      <path id="{c}-gb" d="M408 742 Q380 800 416 828 Q456 845 460 800 Q458 760 434 742 Z" fill="#8B3A2A" stroke="#F0C877" stroke-width="4"/>
      <circle id="{c}-r1" cx="422" cy="790" r="40" fill="none" stroke="#F0C877" stroke-width="5"/>
      <circle id="{c}-r2" cx="422" cy="790" r="40" fill="none" stroke="#F0C877" stroke-width="5"/>
      <path id="{c}-arrow" d="M395 770 C 290 660 250 500 312 352" fill="none" stroke="#F0C877" stroke-width="6" stroke-dasharray="18 14" stroke-linecap="round"/>
      <path id="{c}-head" d="M292 372 L312 336 L338 368" fill="none" stroke="#F0C877" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
      <text id="{c}-l1" class="lbl" x="490" y="905" style="font-size:40px">Vesícula</text>
      <line id="{c}-ln" x1="440" y1="830" x2="485" y2="880" stroke="#F5EDE3" stroke-width="3"/>
      <text id="{c}-l2" class="lbl" x="350" y="270" style="font-size:40px">Hombro derecho</text>
    </g></g></svg>"""
    tw = [ft(f"#{c}-liver", "{ opacity: 0 }", "{ opacity: 1 }", 0.2, 0.5),
          ft(f"#{c}-gb", "{ opacity: 0, scale: 0.5, transformOrigin: '430px 790px' }", "{ opacity: 1, scale: 1 }", 0.6, 0.5, "back.out(2)"),
          ft(f"#{c}-l1", "{ opacity: 0 }", "{ opacity: 1 }", 1.0, 0.4), ft(f"#{c}-ln", "{ opacity: 0 }", "{ opacity: 1 }", 1.0, 0.4)]
    for n, t in enumerate([1.0, 1.9, 2.8, 3.7]):
        r = f"#{c}-r{1 + n % 2}"
        tw.append(ft(r, "{ scale: 1, opacity: 0.9, transformOrigin: '422px 790px' }", "{ scale: 2.6, opacity: 0 }", t, 1.1, "power2.out", ir=n < 2))
    tw += [ft(f"#{c}-arrow", "{ strokeDashoffset: 420, opacity: 1 }", "{ strokeDashoffset: 0, opacity: 1 }", 3.3, 1.2, "power2.inOut", ir=False),
           ft(f"#{c}-head", "{ opacity: 0 }", "{ opacity: 1 }", 4.4, 0.3),
           ft(f"#{c}-l2", "{ opacity: 0, y: 12 }", "{ opacity: 1, y: 0 }", 4.4, 0.4)]
    # la flecha empieza oculta
    svg = svg.replace(f'id="{c}-arrow"', f'id="{c}-arrow" opacity="0"')
    return broll(c, start, dur, svg, " ".join(tw))


def br_ultra(start=46.0, dur=5.6):
    c = "brus"
    svg = f"""<svg viewBox="0 0 1080 1300">
      <defs>
        <filter id="{c}-speckle" x="0" y="0" width="100%" height="100%">
          <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="7" result="n"/>
          <feColorMatrix type="matrix" values="0 0 0 0 0.85  0 0 0 0 0.82  0 0 0 0 0.78  0 0 0 0.75 -0.18"/>
        </filter>
        <clipPath id="{c}-sector"><path d="M540 240 L60 1000 A 900 900 0 0 0 1020 1000 Z"/></clipPath>
        <linearGradient id="{c}-shadow" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stop-color="#0B0806" stop-opacity="0.95"/><stop offset="1" stop-color="#0B0806" stop-opacity="0.55"/>
        </linearGradient>
      </defs>
      <rect x="0" y="0" width="1080" height="1300" fill="#0E0B09"/>
      <g id="{c}-art">
        <g clip-path="url(#{c}-sector)">
          <rect x="0" y="200" width="1080" height="1100" fill="#2B2722"/>
          <rect x="0" y="200" width="1080" height="1100" filter="url(#{c}-speckle)"/>
          <ellipse cx="540" cy="700" rx="215" ry="120" fill="#0A0807" stroke="#E9E2D6" stroke-width="7" transform="rotate(-12 540 700)"/>
          <rect x="488" y="790" width="150" height="400" fill="url(#{c}-shadow)"/>
          <g id="{c}-stones">
            <ellipse cx="520" cy="785" rx="26" ry="18" fill="#FFFFFF"/>
            <ellipse cx="566" cy="792" rx="22" ry="16" fill="#F3EEE6"/>
            <ellipse cx="608" cy="780" rx="18" ry="13" fill="#FFFFFF"/>
          </g>
        </g>
        <path d="M540 240 L60 1000 A 900 900 0 0 0 1020 1000 Z" fill="none" stroke="rgba(233,226,214,0.25)" stroke-width="2"/>
        <g id="{c}-cal">
          <line x1="480" y1="740" x2="650" y2="740" stroke="#F0C877" stroke-width="4" stroke-dasharray="10 8"/>
          <path d="M480 728 L480 752 M650 728 L650 752" stroke="#F0C877" stroke-width="4"/>
          <text class="lbl" x="670" y="752" style="fill:#F0C877">Litos</text>
        </g>
        <text id="{c}-vb" class="lbl" x="330" y="610">Vesícula</text>
      </g>
      <text class="mono" data-layout-ignore x="60" y="210">ABD SUP · 3.5 MHz · VB long</text>
      <text class="mono" data-layout-ignore x="1020" y="210" text-anchor="end">La Paz, BCS</text>
    </svg>"""
    tw = [ft(f"#{c}-vb", "{ opacity: 0 }", "{ opacity: 1 }", 0.6, 0.4),
          ft(f"#{c}-stones", "{ opacity: 0.3 }", "{ opacity: 1 }", 1.2, 0.5),
          ft(f"#{c}-cal", "{ opacity: 0, x: -20 }", "{ opacity: 1, x: 0 }", 2.0, 0.5)]
    return broll(c, start, dur, svg, " ".join(tw))


def br_alarma(start=84.6, dur=10.6):
    c = "bralm"
    svg = f"""<svg viewBox="0 0 1080 1300"><g id="{c}-art">
      <text class="lbl-k" x="540" y="260" text-anchor="middle">DATOS DE ALARMA</text>
      <g id="{c}-row1">
        <path d="M150 470 Q245 385 340 470 Q245 555 150 470 Z" fill="#E7C24A" stroke="#F5EDE3" stroke-width="5"/>
        <circle cx="245" cy="470" r="34" fill="#4A3426"/><circle cx="245" cy="470" r="14" fill="#140D09"/>
        <text class="lbl" x="400" y="482" style="font-size:52px">Piel u ojos amarillos</text>
      </g>
      <g id="{c}-row2">
        <path d="M245 610 Q300 690 300 735 A55 55 0 0 1 190 735 Q190 690 245 610 Z" fill="#9A5A12" stroke="#F5EDE3" stroke-width="5"/>
        <text class="lbl" x="400" y="742" style="font-size:52px">Orina muy oscura</text>
      </g>
      <g id="{c}-row3">
        <rect x="228" y="860" width="34" height="120" rx="17" fill="none" stroke="#F5EDE3" stroke-width="5"/>
        <circle cx="245" cy="1000" r="34" fill="#C2452D" stroke="#F5EDE3" stroke-width="5"/>
        <rect id="{c}-merc" x="238" y="900" width="14" height="80" rx="7" fill="#C2452D"/>
        <text class="lbl" x="400" y="1000" style="font-size:52px">Dolor con fiebre</text>
      </g>
    </g></svg>"""
    tw = [ft(f"#{c}-row1", "{ opacity: 0, x: -40 }", "{ opacity: 1, x: 0 }", 0.4, 0.5),
          ft(f"#{c}-row2", "{ opacity: 0, x: -40 }", "{ opacity: 1, x: 0 }", 4.0, 0.5),
          ft(f"#{c}-row3", "{ opacity: 0, x: -40 }", "{ opacity: 1, x: 0 }", 8.0, 0.5),
          ft(f"#{c}-merc", "{ scaleY: 0.2, transformOrigin: '245px 980px' }", "{ scaleY: 1 }", 8.3, 1.2, "power2.out")]
    return broll(c, start, dur, svg, " ".join(tw))


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
    return cid, start, dur, "end", f"""<template>
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
    .ec-handle {{ font-family: 'Jost', sans-serif; font-weight: 500; font-size: 34px; color: #A87A1E; margin-top: 40px; letter-spacing: 0.04em; }}
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
    text("hook", 0.0, 5.6, title="¿Dolor después de comer?", items=[(0.0, "Podría ser tu vesícula", "em")], visible_at_zero=True),
    nametag("nombre", 6.0, 7.0),
    br_pastillas(),
    text("mito", 19.5, 8.0, kicker="No siempre es gastritis",
         items=[(20.6, "Antiácidos y analgésicos", "item"), (24.0, "solo enmascaran el síntoma", "em")]),
    text("senales", 28.5, 13.3, kicker="Señales de vesícula",
         items=[(29.6, "Dolor bajo la costilla derecha", "item"),
                (32.4, "Se va a la espalda o al hombro", "item"),
                (36.4, "Después de comida grasosa", "item")]),
    br_anatomia(),
    text("ultra", 43.0, 13.5, kicker="¿Cómo saberlo?", title="Un ultrasonido",
         items=[(46.8, "de hígado y vías biliares", "item"), (50.4, "y llévaselo a tu cirujano", "item")]),
    br_ultra(),
    text("piedras", 57.0, 3.4, title="Piedras + dolor", items=[(57.6, "= momento de operarse", "em")]),
    text("sindolor", 61.0, 18.4, kicker="¿Piedras sin dolor?",
         items=[(63.2, "Te las encontraron, pero nunca te han dolido", "item"),
                (70.6, "Tranquilo: no siempre se opera", "item"),
                (74.6, "Vigilancia con un cirujano de confianza", "item")]),
    text("alarma", 80.6, 4.1, title="Datos de alarma"),
    br_alarma(),
    text("urgencia", 95.3, 8.7, kicker="Datos de urgencia quirúrgica", items=[(95.6, "Acude a urgencias", "em")]),
    text("dudas", 105.5, 12.5, kicker="¿Tienes dudas?", title="Déjalas en comentarios"),
    endcard("cierre", END, TOTAL - END),
]

# Zoom (punch-ins rápidos en frases clave, alejamientos en momentos de calma): (t, escala, duración, ease)
ZOOM = [
    (2.4, 1.12, 0.18, "power2.out"), (6.0, 1.2, 0.18, "power2.out"), (8.0, 1.0, 0.18, "power2.out"),
    (17.6, 1.08, 0.01, "none"), (17.62, 1.14, 9.6, "none"), (27.8, 1.0, 0.18, "power2.out"),
    (35.2, 1.12, 0.18, "power2.out"), (38.5, 1.2, 0.18, "power2.out"), (42.0, 1.0, 0.18, "power2.out"),
    (51.6, 1.1, 0.18, "power2.out"), (57.0, 1.2, 0.18, "power2.out"), (60.5, 1.0, 0.25, "power2.out"),
    (61.0, 1.1, 9.0, "none"), (70.4, 1.0, 0.9, "power2.inOut"),
    (79.5, 1.15, 0.18, "power2.out"), (95.3, 1.2, 0.18, "power2.out"), (99.0, 1.1, 0.6, "power2.inOut"),
    (104.5, 1.0, 0.18, "power2.out"), (106.0, 1.1, 12.0, "none"), (121.8, 1.18, 0.18, "power2.out"),
]

z_order = {"broll": 20, "text": 40, "end": 90}
hosts = []
for n, (cid, start, dur, kind, html) in enumerate(scenes):
    (P / "compositions" / f"{cid}.html").write_text(html)
    track = {"broll": 1, "text": 2 + n % 3, "end": 5}[kind]
    hosts.append(
        f'      <div id="{cid}" data-composition-id="{cid}" data-composition-src="compositions/{cid}.html" '
        f'data-start="{start}" data-duration="{dur}" data-track-index="{track}" data-track-kind="graphics" '
        f'data-width="{W}" data-height="{H}" style="z-index: {z_order[kind] + n}"></div>'
    )
for old in (P / "compositions").glob("*.html"):
    if old.stem not in {s[0] for s in scenes}:
        old.unlink()

zoom_js, prev = [], 1.0
for n, (t, s, d, ease) in enumerate(ZOOM):
    ir = "" if n == 0 else ", immediateRender: false"
    zoom_js.append(f'tl.fromTo("#cam", {{ scale: {prev} }}, {{ scale: {s}, duration: {d}, ease: "{ease}"{ir} }}, {t});')
    prev = s

index = f"""<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <title>Reel vesícula · semana 43</title>
    <script src="vendor/gsap.min.js"></script>
    <style>
      html, body {{ margin: 0; background: #000; }}
      #cam {{ position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; overflow: hidden; z-index: 1;
              transform-origin: 540px 800px; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="{W}" data-height="{H}">
      <div id="cam">
        <video id="reel" class="clip" src="assets/reel.mp4" data-start="0" data-duration="{END}" data-track-index="0"
          playsinline data-has-audio="true"
          style="position: absolute; left: 0; top: 0; width: {W}px; height: {H}px; object-fit: contain"></video>
      </div>
{chr(10).join(hosts)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true }});
      {chr(10).join('      ' + z for z in zoom_js).lstrip()}
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
"""
(P / "index.html").write_text(index)
print(f"{len(scenes)} escenas, {len(ZOOM)} movimientos de cámara, duración {TOTAL}s")
