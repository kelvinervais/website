---
title: Projects
permalink: /projects/
---


Selected independent projects. Each write‑up includes the problem, approach, key decisions, impact, and what I learned.

## foodPal — Personalized Recipe Recommender

- Problem: People waste time deciding what to cook, and existing apps ignore pantry constraints.
- Approach: Ensemble recommender blending collaborative filtering, content‑based signals (pantry overlap), and semantic embeddings for ingredient similarity.
- Key decisions: Prioritized pantry overlap early in ranking; switched to embeddings when metadata sparse; added diversity penalty to avoid near‑duplicates.
- Impact: Reduced user search time by ~60%; Precision@10: 0.73, NDCG: 0.81 on validation set.
- Challenges & learnings: Cold‑start for brand‑new users solved with pantry‑first heuristics; caching cut response latency by ~40%.
- Stack: R (Shiny, tidyverse), embeddings

## FlickFlow — People‑Driven Movie Recommendation Engine

- Problem: Make ML recommendations feel playful while improving quality as feedback accrues.
- Approach: Start with content‑based recs; after ~25 swipes transition to a custom Counts & Means collaborative filtering model.
- Key decisions: Tracked satisfaction as an explicit metric; designed swipe UX to gather signal without friction; batched writes to Mongo for reliability.
- Impact: Satisfaction rose from ~30% to ~85% after the CF transition; >15k swipes captured.
- Challenges & learnings: Tackled item/user cold‑start with popularity‑adjusted priors; tuned threshold to avoid premature CF switch.
- Stack: R (Shiny), MongoDB, TMDB APIs

## Stock Portfolio Tracker — Interactive Analytics Platform

- Problem: Retail investors need simple, transparent analytics for “what‑if” decisions.
- Approach: Real‑time retrieval + AR(1) baseline forecasting + Monte Carlo VaR/expected shortfall scenarios; progressive disclosure UI.
- Key decisions: Used modules for performance isolation; added glossary tooltips to improve onboarding; guarded fallbacks for API hiccups.
- Impact: Faster iteration on scenarios; reduced time‑to‑insight in user tests; clear communication of uncertainty.
- Challenges & learnings: Caching and memoization were critical; balancing fidelity vs. speed required pragmatic defaults.
- Stack: R (Shiny, quantmod), bslib, custom CSS
