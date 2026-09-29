#!/usr/bin/env python3
"""Refresh the auto-updated sections of README.md.

Fills the text between marker comments:
  <!-- BLOG:START -->    ... <!-- BLOG:END -->     newest posts from greg.heffner.live
  <!-- SHIPPED:START --> ... <!-- SHIPPED:END -->  newest merged PRs in public repos

Stdlib only. Any fetch or parse failure exits non-zero and leaves README.md
untouched, so a bad run never publishes an empty section.
"""
import json
import os
import re
import sys
import urllib.request

README = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "README.md")
BLOG_URL = "https://greg.heffner.live/blog.html"
USER = "gregheffner"
SHIP_REPOS = ["cicd", "ansible-collection-ubuntu-patching"]
BLOG_COUNT = 5
SHIP_COUNT = 6
UA = "gregheffner-readme-bot (+https://github.com/gregheffner/gregheffner)"


def fetch(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def blog_rows():
    html = fetch(BLOG_URL)
    posts = []
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            data = json.loads(block)
        except ValueError:
            continue
        for node in data if isinstance(data, list) else [data]:
            posts += node.get("blogPost", []) if isinstance(node, dict) else []
    posts = [p for p in posts if p.get("headline") and p.get("url") and p.get("datePublished")]
    if not posts:
        sys.exit("FAIL: no blogPost entries found in " + BLOG_URL)
    posts.sort(key=lambda p: p["datePublished"], reverse=True)
    rows = ["| Date | Post |", "| :-- | :-- |"]
    for p in posts[:BLOG_COUNT]:
        rows.append(f"| {p['datePublished']} | [**{md(p['headline'])}**]({p['url']}) |")
    return "\n".join(rows)


def shipped_rows():
    headers = {"Accept": "application/vnd.github+json"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    prs = []
    for repo in SHIP_REPOS:
        url = f"https://api.github.com/repos/{USER}/{repo}/pulls?state=closed&sort=updated&direction=desc&per_page=30"
        for pr in json.loads(fetch(url, headers)):
            if pr.get("merged_at") and pr["user"]["type"] != "Bot":
                prs.append((pr["merged_at"], repo, pr["number"], pr["title"], pr["html_url"]))
    if not prs:
        sys.exit("FAIL: no merged PRs found in " + ", ".join(SHIP_REPOS))
    prs.sort(reverse=True)
    rows = ["| Merged | Repo | Change |", "| :-- | :-- | :-- |"]
    for merged, repo, num, title, link in prs[:SHIP_COUNT]:
        rows.append(f"| {merged[:10]} | {repo} | [{md(title)}]({link}) |")
    return "\n".join(rows)


def md(text):
    # keep titles from breaking the table
    return text.replace("|", "\\|").replace("\n", " ").strip()


def splice(doc, name, body):
    pat = re.compile(rf"(<!-- {name}:START -->\n)(?:.*?\n)?(<!-- {name}:END -->)", re.S)
    if not pat.search(doc):
        sys.exit(f"FAIL: {name} markers missing from README.md")
    return pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), doc)


def main():
    with open(README, encoding="utf-8") as f:
        old = f.read()
    new = splice(old, "BLOG", blog_rows())
    new = splice(new, "SHIPPED", shipped_rows())
    if new == old:
        print("README.md already current")
        return
    with open(README, "w", encoding="utf-8") as f:
        f.write(new)
    print("README.md updated")


if __name__ == "__main__":
    main()
