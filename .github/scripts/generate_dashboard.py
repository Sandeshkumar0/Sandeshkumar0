import json
import os
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime
from html import escape
from pathlib import Path

USERNAME = "Sandeshkumar0"
NAVY = "#0b1d3a"
PARCHMENT = "#f5e6c8"
GOLD = "#f2b705"
RED = "#c0392b"


def github_get(path):
    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    with urllib.request.urlopen(request) as response:
        return json.load(response)


def text(value):
    return escape(str(value), quote=True)


def make_svg(profile, repos):
    public_repos = [repo for repo in repos if not repo["fork"]]
    stars = sum(repo["stargazers_count"] for repo in public_repos)
    languages = Counter(
        repo["language"] for repo in public_repos if repo.get("language")
    )
    top_languages = "  •  ".join(
        f"{language} ({count})" for language, count in languages.most_common(5)
    )
    recent = sorted(
        public_repos,
        key=lambda repo: repo.get("pushed_at") or "",
        reverse=True,
    )[:3]
    recent_text = "  •  ".join(repo["name"] for repo in recent)
    generated = datetime.utcnow().strftime("%Y-%m-%d")

    cards = [
        ("PUBLIC REPOS", len(public_repos), GOLD),
        ("TOTAL STARS", stars, RED),
        ("FOLLOWERS", profile["followers"], GOLD),
    ]
    card_svg = []
    for index, (label, value, color) in enumerate(cards):
        x = 55 + index * 365
        card_svg.append(
            f'<rect x="{x}" y="48" width="325" height="105" rx="14" '
            f'fill="{NAVY}" stroke="{color}" stroke-width="3"/>'
            f'<text x="{x + 22}" y="82" fill="{PARCHMENT}" font-family="Arial,sans-serif" '
            f'font-size="15" font-weight="700" letter-spacing="2">{text(label)}</text>'
            f'<text x="{x + 22}" y="130" fill="{color}" font-family="Georgia,serif" '
            f'font-size="38" font-weight="700">{text(value)}</text>'
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360"
role="img" aria-labelledby="title desc">
<title id="title">Sandesh GitHub bounty dashboard</title>
<desc id="desc">Self-generated GitHub profile metrics showing repositories, stars, followers, primary languages, and recently updated projects.</desc>
<rect width="1200" height="360" rx="18" fill="{PARCHMENT}"/>
<rect x="10" y="10" width="1180" height="340" rx="14" fill="none" stroke="{NAVY}" stroke-width="8"/>
<text x="55" y="38" fill="{RED}" font-family="Georgia,serif" font-size="21" font-weight="700" letter-spacing="4">BOUNTY BOARD • LIVE FROM GITHUB</text>
{"".join(card_svg)}
<text x="55" y="195" fill="{NAVY}" font-family="Arial,sans-serif" font-size="16" font-weight="700">TOP LANGUAGES BY PUBLIC REPOSITORY</text>
<text x="55" y="225" fill="{NAVY}" font-family="Arial,sans-serif" font-size="19">{text(top_languages or "No language data available")}</text>
<text x="55" y="270" fill="{NAVY}" font-family="Arial,sans-serif" font-size="16" font-weight="700">RECENTLY UPDATED VOYAGES</text>
<text x="55" y="300" fill="{NAVY}" font-family="Arial,sans-serif" font-size="19">{text(recent_text or "No public projects available")}</text>
<text x="1145" y="329" text-anchor="end" fill="{RED}" font-family="Arial,sans-serif" font-size="12">GENERATED {generated} • github.com/{USERNAME}</text>
</svg>
"""


def main():
    profile = github_get(f"/users/{USERNAME}")
    repos = github_get(
        f"/users/{USERNAME}/repos?{urllib.parse.urlencode({'per_page': 100, 'type': 'owner'})}"
    )
    output = Path("dist/profile-dashboard.svg")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(make_svg(profile, repos), encoding="utf-8")


if __name__ == "__main__":
    main()
