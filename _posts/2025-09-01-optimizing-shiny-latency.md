---
title: What I Learned Cutting Shiny Latency from 12s to 2.1s
tags: [r, shiny, performance, caching]
---

A recent Shiny app was taking ~12 seconds to load on cold start. Here’s how I got it down to ~2.1 seconds while keeping the UX snappy.

- Problem: Multiple expensive data prep steps (joins, summarizations, model loads) ran on every request, and the app re‑computed identical results for many users.
- Constraints: Shared hosting (shinyapps.io) with modest CPU; periodic data refreshes; no heavy infra changes.

What worked:

1) Move heavy work to startup and cache aggressively

- Precompute feature tables at `global.R` and memoize functions with `memoise`.
- Use a versioned cache key so refreshes invalidate cleanly.

2) Reduce object sizes and parse once

- Store model artifacts as RDS with compact objects; avoid repeated `read_csv`/`jsonlite::fromJSON`.
- Convert wide joins to narrower, typed columns; factor where appropriate.

3) Defer non‑critical UI

- Render above‑the‑fold UI first; lazy‑load expensive plots and tables (`req()` + `invalidateLater()` where appropriate).
- Use `DT::datatable` with server‑side options for large tables.

4) Profile relentlessly

- `profvis` + simple timers around hotspots revealed a slow custom aggregation we replaced with `data.table`.

Results: P50 load ~2.1s (down from 12s), P95 ~3.3s. The biggest win was moving work to startup + memoization; everything else compounded.

Tradeoffs & lessons

- Caching hides problems—add metrics and a manual “refresh data” knob.
- Small schema tweaks beat clever code when IO dominates.
- Communicating progress (skeletons/spinners) matters almost as much as raw speed for perceived latency.

