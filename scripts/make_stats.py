#!/usr/bin/env python3
"""Draw the profile stats cards as static SVGs (replaces github-readme-stats.vercel.app).

Writes stats/overview.svg and stats/languages.svg. Needs GITHUB_TOKEN (GraphQL
requires auth). Public, non-fork repos only. Stdlib only; any API error exits
non-zero before a file is written.
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone
from html import escape

USER = "gregheffner"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "stats")
LANG_COUNT = 8
# tokyonight, matching the old cards
BG, TITLE, TEXT, ICON, MUTED = "#1a1b27", "#70a5fd", "#38bdae", "#bf91f3", "#a9b1d6"

QUERY = """
query($login: String!, $after: String) {
  user(login: $login) {
    createdAt
    contributionsCollection { totalCommitContributions }
    pullRequests { totalCount }
    repositories(first: 100, after: $after, ownerAffiliations: OWNER, privacy: PUBLIC, isFork: false) {
      pageInfo { hasNextPage endCursor }
      nodes {
        stargazerCount
        languages(first: 20, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name color } } }
      }
    }
  }
}"""


def gql(variables):
    token = os.environ.get("GITHUB_TOKEN") or sys.exit("FAIL: GITHUB_TOKEN not set")
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={"Authorization": "Bearer " + token, "Content-Type": "application/json",
                 "User-Agent": "gregheffner-readme-bot"})
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.loads(r.read())
    if body.get("errors"):
        sys.exit("FAIL: " + json.dumps(body["errors"])[:500])
    return body["data"]["user"]


def collect():
    after, repos, user = None, [], None
    while True:
        user = gql({"login": USER, "after": after})
        page = user["repositories"]
        repos += page["nodes"]
        if not page["pageInfo"]["hasNextPage"]:
            break
        after = page["pageInfo"]["endCursor"]
    langs = {}
    for repo in repos:
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            size, color = langs.get(name, (0, edge["node"]["color"] or "#858585"))
            langs[name] = (size + edge["size"], color)
    cc = user["contributionsCollection"]
    return {
        "stars": sum(r["stargazerCount"] for r in repos),
        "commits": cc["totalCommitContributions"],
        "prs": user["pullRequests"]["totalCount"],
        "since": user["createdAt"][:4],
        "repos": len(repos),
        "langs": sorted(langs.items(), key=lambda kv: kv[1][0], reverse=True),
    }


def card(width, height, title, inner):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">
<title>{escape(title)}</title>
<style>
.t{{font:600 18px 'Segoe UI',Ubuntu,Sans-Serif;fill:{TITLE}}}
.l{{font:600 14px 'Segoe UI',Ubuntu,Sans-Serif;fill:{TEXT}}}
.v{{font:700 14px 'Segoe UI',Ubuntu,Sans-Serif;fill:{TEXT}}}
.s{{font:400 11px 'Segoe UI',Ubuntu,Sans-Serif;fill:{MUTED}}}
</style>
<rect width="{width}" height="{height}" rx="4.5" fill="{BG}"/>
<text x="25" y="35" class="t">{escape(title)}</text>
{inner}
</svg>
"""


def overview(s, year):
    rows = [("Total Stars Earned", s["stars"]), (f"Commits ({year})", s["commits"]),
            ("Total PRs", s["prs"]), ("Public Repos", s["repos"]),
            ("On GitHub Since", s["since"])]
    inner = []
    for i, (label, value) in enumerate(rows):
        y = 70 + i * 25
        inner.append(f'<circle cx="31" cy="{y - 5}" r="4" fill="{ICON}"/>'
                     f'<text x="45" y="{y}" class="l">{escape(label)}:</text>'
                     f'<text x="230" y="{y}" class="v">{value if isinstance(value, str) else f"{value:,}"}</text>')
    return card(340, 195, "Greg Heffner's GitHub Stats", "\n".join(inner))


def languages(s):
    top = s["langs"][:LANG_COUNT]
    total = sum(size for _, (size, _) in top) or 1
    bar, x = [], 25.0
    for name, (size, color) in top:
        w = 250 * size / total
        bar.append(f'<rect x="{x:.2f}" y="50" width="{w:.2f}" height="8" fill="{color}"/>')
        x += w
    items = []
    for i, (name, (size, color)) in enumerate(top):
        cx, cy = 25 + (i % 2) * 130, 80 + (i // 2) * 22
        items.append(f'<circle cx="{cx + 5}" cy="{cy - 4}" r="5" fill="{color}"/>'
                     f'<text x="{cx + 15}" y="{cy}" class="s" style="font-size:12px">{escape(name)} {100 * size / total:.1f}%</text>')
    clip = '<clipPath id="c"><rect x="25" y="50" width="250" height="8" rx="4"/></clipPath>'
    inner = clip + '<g clip-path="url(#c)">' + "".join(bar) + "</g>\n" + "\n".join(items)
    return card(300, 80 + ((len(top) + 1) // 2) * 22, "Most Used Languages", inner)


def main():
    s = collect()
    if not s["langs"]:
        sys.exit("FAIL: no languages returned")
    year = datetime.now(timezone.utc).year
    os.makedirs(OUT, exist_ok=True)
    for name, svg in (("overview.svg", overview(s, year)), ("languages.svg", languages(s))):
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(svg)
    print(json.dumps({k: v for k, v in s.items() if k != "langs"}), "top:", [n for n, _ in s["langs"][:LANG_COUNT]])


if __name__ == "__main__":
    main()
