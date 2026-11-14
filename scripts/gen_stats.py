#!/usr/bin/env python3
"""Render a themed GitHub stats card (dark + light) from the GraphQL API.

Usage: GITHUB_TOKEN=... python3 scripts/gen_stats.py <login> <out_dir>
Stdlib only, so it runs on a bare Actions runner.
"""
import datetime as dt
import json
import os
import sys
import urllib.request
from html import escape

NOISE = {"Makefile", "CMake", "Dockerfile", "Shell", "HTML", "CSS", "Batchfile", "PowerShell", "Nix"}

THEMES = {
    "dark": dict(bg="#0d1117", panel="#161b22", border="#1dc7a540", line="#30363d",
                 text="#e6fffa", muted="#8b949e", accent="#1dc7a5", glow="#1dc7a5"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", border="#0f8f7840", line="#d0d7de",
                  text="#1f2328", muted="#59636e", accent="#0f8f78", glow="#1dc7a5"),
}
LANG_COLORS = ["#1dc7a5", "#3fa9f5", "#8b7cf6", "#f2b84b", "#ef6f8f", "#5fd6bf"]


def gql(query, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-stats"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if "errors" in body:
        raise SystemExit(json.dumps(body["errors"], indent=2))
    return body["data"]


def fetch(login, token):
    base = gql(f"""{{ user(login: "{login}") {{
        createdAt
        followers {{ totalCount }}
        repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {{
          totalCount
          nodes {{ stargazerCount
            languages(first: 10, orderBy: {{field: SIZE, direction: DESC}}) {{ edges {{ size node {{ name }} }} }} }}
        }}
    }} }}""", token)["user"]

    first = int(base["createdAt"][:4])
    now = dt.datetime.now(dt.timezone.utc)
    parts = []
    for y in range(first, now.year + 1):
        start = f"{y}-01-01T00:00:00Z"
        end = now.strftime("%Y-%m-%dT%H:%M:%SZ") if y == now.year else f"{y}-12-31T23:59:59Z"
        parts.append(f'y{y}: contributionsCollection(from: "{start}", to: "{end}") '
                     "{ contributionCalendar { weeks { contributionDays { date contributionCount } } } }")
    years = gql(f'{{ user(login: "{login}") {{ {" ".join(parts)} }} }}', token)["user"]

    days = {}
    for col in years.values():
        for w in col["contributionCalendar"]["weeks"]:
            for d in w["contributionDays"]:
                days[d["date"]] = d["contributionCount"]
    return base, dict(sorted(days.items()))


def streaks(days):
    dates = list(days)
    longest = run = 0
    for d in dates:
        run = run + 1 if days[d] else 0
        longest = max(longest, run)
    current = 0
    i = len(dates) - 1
    if i >= 0 and days[dates[i]] == 0:  # today not counted yet
        i -= 1
    while i >= 0 and days[dates[i]]:
        current += 1
        i -= 1
    return current, longest


def languages(repos):
    totals = {}
    for r in repos:
        for e in r["languages"]["edges"]:
            n = e["node"]["name"]
            if n not in NOISE:
                totals[n] = totals.get(n, 0) + e["size"]
    s = sum(totals.values()) or 1
    top = sorted(totals.items(), key=lambda kv: -kv[1])[:6]
    return [(n, 100 * v / s) for n, v in top]


def fmt(n):
    return f"{n/1000:.1f}k" if n >= 10000 else f"{n:,}"


def render(theme, login, stats, weeks, langs):
    t = THEMES[theme]
    W, H, P = 840, 344, 20
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
           f'role="img" aria-label="GitHub stats for {escape(login)}">',
           f"""<style>
  text {{ font-family: 'JetBrains Mono','SFMono-Regular',ui-monospace,Menlo,Consolas,monospace; }}
  .sans {{ font-family: 'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif; }}
  .num {{ font-size: 26px; font-weight: 700; fill: {t['text']}; }}
  .lbl {{ font-size: 10.5px; letter-spacing: .08em; fill: {t['muted']}; }}
  .ttl {{ font-size: 13px; font-weight: 600; fill: {t['accent']}; }}
  .sm  {{ font-size: 11px; fill: {t['muted']}; }}
  .ln  {{ font-size: 12px; fill: {t['text']}; }}
  .fade {{ opacity: 0; animation: fade .7s ease forwards; }}
  .draw {{ stroke-dasharray: 2000; stroke-dashoffset: 2000; animation: draw 2.2s ease forwards .4s; }}
  .grow {{ transform-box: fill-box; transform-origin: left; transform: scaleX(0); animation: grow 1s cubic-bezier(.2,.8,.2,1) forwards; }}
  @keyframes fade {{ to {{ opacity: 1; }} }}
  @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
  @keyframes grow {{ to {{ transform: scaleX(1); }} }}
</style>""",
           f"""<defs>
  <linearGradient id="area" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="{t['glow']}" stop-opacity=".35"/><stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="halo" cx="1" cy="0" r="1"><stop offset="0" stop-color="{t['glow']}" stop-opacity=".14"/><stop offset="1" stop-color="{t['glow']}" stop-opacity="0"/></radialGradient>
</defs>""",
           f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{t["bg"]}" stroke="{t["border"]}"/>',
           f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="url(#halo)"/>',
           f'<text x="{P}" y="34" class="ttl">~/stats</text>',
           f'<text x="{W-P}" y="34" class="sm" text-anchor="end">@{escape(login)} · updated {dt.date.today():%d %b %Y}</text>']

    # stat tiles
    n, gap = len(stats), 10
    tw = (W - 2 * P - gap * (n - 1)) / n
    for i, (label, value) in enumerate(stats):
        x = P + i * (tw + gap)
        out.append(f'<g class="fade" style="animation-delay:{.08*i:.2f}s">'
                   f'<rect x="{x:.1f}" y="50" width="{tw:.1f}" height="76" rx="10" fill="{t["panel"]}" stroke="{t["line"]}"/>'
                   f'<rect x="{x:.1f}" y="62" width="3" height="52" rx="1.5" fill="{t["accent"]}"/>'
                   f'<text x="{x+16:.1f}" y="94" class="num sans">{escape(value)}</text>'
                   f'<text x="{x+16:.1f}" y="114" class="lbl">{escape(label.upper())}</text></g>')

    # weekly contributions chart
    cx, cy, cw, ch = P, 150, 500, 158
    out.append(f'<g class="fade" style="animation-delay:.3s">'
               f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch+24}" rx="10" fill="{t["panel"]}" stroke="{t["line"]}"/>'
               f'<text x="{cx+14}" y="{cy+22}" class="ttl">contributions · last 52 weeks</text></g>')
    gx, gy, gw, gh = cx + 14, cy + 36, cw - 28, ch - 46
    peak = max(c for _, c in weeks) or 1
    pts = [(gx + gw * i / (len(weeks) - 1), gy + gh - gh * c / peak) for i, (_, c) in enumerate(weeks)]
    line = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    out.append(f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{t["line"]}"/>')
    out.append(f'<polygon class="fade" style="animation-delay:1.2s" points="{gx},{gy+gh} {line} {gx+gw},{gy+gh}" fill="url(#area)"/>')
    out.append(f'<polyline class="draw" points="{line}" fill="none" stroke="{t["accent"]}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>')
    lx, ly = pts[-1]
    out.append(f'<circle class="fade" style="animation-delay:2.4s" cx="{lx:.1f}" cy="{ly:.1f}" r="3.5" fill="{t["accent"]}"/>')
    prev = None
    for i, (wk, _) in enumerate(weeks):
        m = wk[5:7]
        if m != prev and i > 1:
            x = pts[i][0]
            out.append(f'<text x="{x:.1f}" y="{gy+gh+16}" class="sm" text-anchor="middle">'
                       f'{dt.date.fromisoformat(wk):%b}</text>')
        prev = m

    # languages
    lxp, lw = cx + cw + 12, W - P - (cx + cw + 12)
    out.append(f'<g class="fade" style="animation-delay:.4s">'
               f'<rect x="{lxp}" y="{cy}" width="{lw}" height="{ch+24}" rx="10" fill="{t["panel"]}" stroke="{t["line"]}"/>'
               f'<text x="{lxp+14}" y="{cy+22}" class="ttl">top languages</text></g>')
    bw = lw - 28
    for i, (name, pct) in enumerate(langs):
        y = cy + 48 + i * 24
        col = LANG_COLORS[i % len(LANG_COLORS)]
        d = f"{.5 + .1*i:.2f}s"
        out.append(f'<g class="fade" style="animation-delay:{d}">'
                   f'<text x="{lxp+14}" y="{y}" class="ln">{escape(name)}</text>'
                   f'<text x="{lxp+14+bw}" y="{y}" class="sm" text-anchor="end">{pct:.1f}%</text>'
                   f'<rect x="{lxp+14}" y="{y+6}" width="{bw}" height="4" rx="2" fill="{t["line"]}"/></g>'
                   f'<rect class="grow" style="animation-delay:{d}" x="{lxp+14}" y="{y+6}" '
                   f'width="{max(bw*pct/100, 4):.1f}" height="4" rx="2" fill="{col}"/>')

    out.append("</svg>")
    return "\n".join(out)


def main():
    login, out_dir = sys.argv[1], sys.argv[2]
    token = os.environ["GITHUB_TOKEN"]
    base, days = fetch(login, token)
    cur, longest = streaks(days)
    repos = base["repositories"]
    stars = sum(r["stargazerCount"] for r in repos["nodes"])

    recent = list(days.items())[-364:]
    weeks = [(recent[i][0], sum(c for _, c in recent[i:i + 7])) for i in range(0, len(recent), 7)]

    stats = [("contributions", fmt(sum(days.values()))),
             ("current streak", f"{cur}d"),
             ("longest streak", f"{longest}d"),
             ("public repos", fmt(repos["totalCount"])),
             ("stars earned", fmt(stars))]
    langs = languages(repos["nodes"])

    os.makedirs(out_dir, exist_ok=True)
    for theme in THEMES:
        suffix = "" if theme == "light" else "-dark"
        with open(os.path.join(out_dir, f"stats{suffix}.svg"), "w") as f:
            f.write(render(theme, login, stats, weeks, langs))
    print(json.dumps({"stats": stats, "langs": langs}))


if __name__ == "__main__":
    main()
