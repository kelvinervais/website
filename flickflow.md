---
title: FlickFlow — Dynamic Movie Recommendations Report
permalink: /flickflow/
---

## Introduction

In today’s media climate, real-world applications of recommendation systems are limited to organizations with personal or monetary incentives. Companies often bias models toward their originals, high-contract titles, or merchandise-friendly films. FlickFlow is intentionally different: it recommends movies based on personal preferences, not platform profitability. Unlike static, sentiment-only approaches, FlickFlow dynamically adapts recommendations to each user’s evolving taste using an intentional model design and interactive UI.

## Problem Definition

Build a system that dynamically recommends movies users will actually enjoy, based on their preferences, while adapting as feedback accumulates. The UX must be familiar and low-friction to encourage adoption (a dating-app-style swipe interface).

## Literature Survey (Selected)

- Osman & Azman (2018): Large volumes of user ratings are key for useful recommender modeling; sentiment-only systems need ample data.  
- Wakil et al. (2015): Hybridizing collaborative and content-based filtering, with potential emotional features, motivates a staged approach.  
- Sappadla et al. (2017): “Zero state” vs. “base state” informed our staged cold-start handling.  
- Kesharwani & Bharti (2017): Twitter sentiment to movie ratings as a signal; inspired our similarity quantification for early preferences.  
- Kumar & Roy (2020): Careful preprocessing and feature engineering matter; Linear SVM slightly led among tested models for sentiment-related tasks.  
- Additional: Chauhan et al. (2021); Marappan & Bhaskaran (2022); Baid et al. (2017).

## Methodology

FlickFlow combines a breadth of movie metadata, a dynamic UI, and a custom Counts & Means Collaborative Filtering (CMCF) approach—explicitly free from profit optimization biases. The system starts with content-based recommendations for cold-start and transitions to CMCF as signal accumulates.

## Data Creation and EDA

- Source: TMDB (Kaggle dataset, daily updates).  
- Scope: ~100k movies selected by popularity, votes, and completeness to keep compute tractable.  
- Features: One-hot encodings for genre, production company, decade; percentiles for TMDB vote avg, popularity, revenue, budget, and runtime.  
- Users: MongoDB stores interactions (swipes, direction, which movies). This powers similarity computation and model updates.  
- On-demand: Posters and cast/director via TMDB API.

## Computation — Zero State (Content-Based Filtering)

For new users, a 3-question quiz narrows down genre, runtime, and era. We propose three initial options; once a user selects one, we generate an initial slate of ~50 recommendations. Users see random picks from this set while swiping. After ~25 interactions, we transition to the Base State model.

## Computation — Base State (CMCF)

After 25 interactions, we switch to a custom collaborative filtering system tailored to our signals:

- Similarity: Cosine similarity over hybrid user + movie feature vectors.  
- Data: For MVP, we simulated 500 users reflecting real catalog distributions to build the user–user similarity matrix.  
- Neighborhood: Choose top-k neighbors, aggregate their preferences (counts and means), and score candidate movies by similarity to the aggregate.

The final recommendation set is ranked by the similarity score between aggregated preferences and candidate movies.

## User Interface

After sign-up, users see a movie card (title, poster, More Info). Swipe right for “interested/liked,” left for “not interested/didn’t enjoy.” All interactions are stored and viewable in “My Movies,” where users can review and rate titles.

## Experiments / Evaluation

We tracked users, total swipes, and “flicks right” (positive feedback). Targets vs. actuals (as of 2024-04-20):

| Metric | Target | Actual |
|---|---:|---:|
| Number of Users | 30 | 39 |
| Total Flicks | 300 | 579 |
| Flicks Right | 200 | 362 |
| Flicks Right (% of total) | 66% | 63% |

By model stage:

| Stage | Users | Total Flicks | Flicks Right | Flicks Right % |
|---|---:|---:|---:|---:|
| Zero (content-based) | 30 | 234 | 128 | 55% |
| Base (CMCF) | 9 | 345 | 234 | 68% |

The quarter of users who reached Base State saw a higher positive feedback rate, supporting the staged approach.

Bias checks (top 5 by swipes right):

- Genres: Adventure, Action, Sci‑Fi, Drama, Fantasy  
- Companies: Marvel, Warner Bros, Paramount, 20th Century Fox, New Line  
- Decades: 2010s, 2000s, 1990s, 1980s, 1970s  

We observed recency bias and a strong Marvel skew, likely reflecting our user sample rather than catalog composition.

## Conclusion / Discussion

Takeaways align with prior work: more user data yields better similarity estimates and robustness. Our constraints (English-only films; limited user count vs. item count) suggest further scale would improve accuracy. The simple swipe UI enabled fast data collection and iteration, and users responded positively to the “dating app” metaphor. With broader recruitment and more data, we expect stronger performance and richer feature design (including multilingual expansion).

## Sources

- Baid, P., Gupta, A., & Chaplot, N. (2017). Sentiment Analysis of Movie Reviews using ML Techniques. IJCA, 179(7).  
- Chauhan, A., Nagar, D., & Chaudhary, P. (2021). Movie recommender system using sentiment analysis. ICIPTM.  
- Kesharwani, A., & Bharti, R. (2017). Movie rating prediction based on Twitter sentiment analysis. JACCT, 5(1).  
- Kumar, S., & Roy, P. P. (2020). Movie recommendation using sentiment analysis from microblogging data. IEEE TCSS, 7(4).  
- Marappan, R., & Bhaskaran, S. (2022). Movie Recommendation System Modeling Using ML. IJMEBAC, 1(1).  
- Osman, N. A., & Azman, N. (2018). Sentiment-Based Model for Recommender Systems. CAMP.  
- Wakil, K., Bakhtyar, R., Ali, K., & Alaadin, K. (2015). Improving web movie recommender systems based on emotions. IJACSA, 6(2).  
- Sappadla, P., et al. (2017). Movie Recommender System Project Report. NYU.  
- Nakhli, R. E., Moradi, H., & Sadeghi, M. A. (2019). Movie recommender based on percentage of view. KBEI.

