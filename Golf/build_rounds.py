"""Convert an 18Birdies data export into the small, public-safe rounds.json the site reads.

Usage:
    python3 Golf/build_rounds.py ~/Downloads/18Birdies_archive.json

The raw export contains account details (phone number, email) and must not be committed.
Only round dates, strokes, per-hole strokes, and course names are written out.
"""
import datetime
import json
import os
import sys


def main(path):
    with open(path) as f:
        data = json.load(f)["myData"]

    courses = {c["clubId"]: c["name"] for c in data["clubData"]["playedClubs"]}
    rounds = []
    for r in data["activityData"]["rounds"]:
        holes = r.get("holeStrokes") or []
        if not holes or any(s == 0 for s in holes) or not r.get("strokes"):
            continue  # abandoned or partial round
        if len(holes) not in (9, 18):
            continue
        rounds.append({
            "date": datetime.datetime.fromtimestamp(r["timestamp"] / 1000).strftime("%Y-%m-%d"),
            "strokes": r["strokes"],
            "holes": holes,
            "course": courses.get(r["clubId"]["id"], ""),
        })
    rounds.sort(key=lambda r: r["date"])

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rounds.json")
    with open(out, "w") as f:
        json.dump({"rounds": rounds}, f, separators=(",", ":"))
    print(f"wrote {len(rounds)} rounds to {out} ({rounds[0]['date']} to {rounds[-1]['date']})")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
