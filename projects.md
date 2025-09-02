---
title: Projects
permalink: /projects/
---


Selected independent projects showcasing different approaches to recommendation systems and data applications.

## foodPal — Personalized Recipe Recommender

- Problem: People waste time deciding what to cook, and existing apps ignore pantry constraints.
- Approach: Ensemble recommendation system blending collaborative filtering, content-based signals (pantry overlap), and semantic embeddings for ingredient similarity.
- Challenges & learnings: Cold-start for brand-new users solved with pantry-first heuristics; caching strategies were critical for response latency.
- Stack: R (Shiny, tidyverse), embeddings

## FlickFlow — Movie Recommendation Engine

- Problem: Make ML recommendations feel playful while improving quality as feedback accrues.
- Approach: Start with content-based recommendations; after 25 swipes transition to a custom Counts & Means collaborative filtering model.
- Challenges & learnings: Tackled item/user cold-start with popularity-adjusted priors; tuned threshold to avoid premature CF switch; swipe UX design was critical for gathering quality signal.
- Stack: R (Shiny), MongoDB, TMDB APIs

## TrendTracker — Finance Analytics Dashboard

- Problem: Retail investors need simple, transparent analytics for "what-if" decisions.
- Approach: Real-time data retrieval with AR(1) baseline forecasting and Monte Carlo VaR/expected shortfall scenarios; progressive disclosure UI.
- Challenges & learnings: Caching and memoization were critical for performance; balancing analytical fidelity vs. speed required pragmatic defaults; API reliability required robust fallback strategies.
- Stack: R (Shiny, quantmod), bslib
