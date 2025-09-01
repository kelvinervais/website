---
title: Projects
permalink: /projects/
---


Selected independent projects. Reach out if you’d like demos or write‑ups.

## foodPal — Personalized Recipe Recommender
An ensemble recommender that blends collaborative filtering, content‑based filtering (pantry overlap), and semantic embeddings.

- Evaluated with Precision@5/10, NDCG, and MRR; ensemble improved relevance and mitigated cold‑start issues.  
- Deployed via an R Shiny app where users input pantry items, receive tailored recipes, and generate shopping lists.  
- Stack: R (Shiny, tidyverse), embeddings

## FlickFlow — People‑Driven Movie Recommendation Engine
Hybrid system combining content‑based recommendations for new users with a custom Counts & Means collaborative filtering model as data grows.

- Integrated MongoDB for user interactions and TMDB APIs for movie metadata.  
- Mobile‑friendly swipe interface in R Shiny captures evolving preferences.  
- Simulated >500 users; collaborative filtering outperformed baseline content filtering.  
- Stack: R (Shiny), MongoDB, TMDB APIs

## Stock Portfolio Tracker — Interactive Analytics Platform
In‑progress R Shiny application with real‑time retrieval for portfolio tracking and scenario analysis.

- Features AR(1) forecasting, Monte Carlo simulation, and glossary‑style tooltips for accessibility.  
- Built with modern UI (bslib + custom CSS) and a modular structure for scalability.  
- Stack: R (Shiny, quantmod), bslib, custom CSS
