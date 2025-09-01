---
title: Solving Cold-Start in FlickFlow Without Killing the Fun
tags: [recsys, cold-start, ux, r, shiny]
---

FlickFlow started as a playful swipe UI for movies—but playful isn’t useful if early recs miss. Here’s how I navigated cold‑start without over‑engineering.

Goal: Keep the swipe flow fun while improving recommendation quality as quickly as possible.

Approach

- Phase 1 (0–25 swipes): Content‑based similarity (metadata + embeddings) with a diversity penalty; popularity‑adjusted priors to avoid dead‑ends.
- Phase 2 (25+ swipes): Switch to a lightweight Counts & Means CF with shrinkage; batch updates to Mongo to reduce write overhead.
- Feedback: Track explicit “would watch” as a satisfaction signal; keep the UI friction‑free to gather signal fast.

What worked

- The thresholded switch avoided premature CF noise while letting the system learn from real preferences quickly.
- The diversity penalty kept exploration high—users felt the catalog breadth without repetition.

Outcomes

- Satisfaction rose from ~30% to ~85% after the switch threshold.
- >15k swipes recorded; retention improved because users saw the system “get smarter”.

Notes

- Resist the urge to ship a complex CF first—good metadata + embeddings are plenty to start.
- A tiny bit of UX thought (microcopy, animations) goes a long way for perceived quality.

