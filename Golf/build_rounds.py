"""Convert an 18Birdies data export into the public-safe rounds.json the site reads.

Usage:
    python3 Golf/build_rounds.py Golf/18Birdies_archive.json

The raw export contains account details (phone number, email) and is gitignored.
Only rounds and course names are kept, in the same shape the site's JavaScript expects.
"""
import json
import os
import sys


def main(path):
    with open(path) as f:
        data = json.load(f)["myData"]

    rounds = []
    for r in data["activityData"]["rounds"]:
        holes = r.get("holeStrokes") or []
        if not holes or any(s == 0 for s in holes) or not r.get("strokes"):
            continue  # abandoned or partial round
        rounds.append({
            "timestamp": r["timestamp"],
            "strokes": r["strokes"],
            "score": r.get("score"),
            "holeStrokes": holes,
            "clubId": {"id": r["clubId"]["id"]},
            "roundHandicap": r.get("roundHandicap"),
            "stats": {k: (r.get("stats") or {}).get(k, 0)
                      for k in ("eagles", "birdies", "pars", "bogeys", "doubleBogeyOrWorse")},
        })
    rounds.sort(key=lambda r: r["timestamp"])

    clubs = [{"clubId": c["clubId"], "name": c["name"]} for c in data["clubData"]["playedClubs"]]

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rounds.json")
    with open(out, "w") as f:
        json.dump({"myData": {"activityData": {"roundCount": len(rounds), "rounds": rounds},
                              "clubData": {"playedClubs": clubs}}}, f, separators=(",", ":"))
    print(f"wrote {len(rounds)} rounds to {out}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
