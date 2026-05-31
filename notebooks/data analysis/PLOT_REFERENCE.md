# 📊 California Housing — Complete Plot Reference Guide

## For use in PPTX / Essay presentations

---

## How to use this guide

Each row maps a **plot file → slide description → what to say**.  
Run notebooks in order (01 → 02 → 03 → 04); all plots save to `data/visualize/`.

---

## NOTEBOOK 03 · Rich Data Analysis

> *Theme for slides: "Understanding the Data the Model Was Trained On"*

| # | File | Slide Title Suggestion | What the plot shows | Key thing to say |
|---|------|------------------------|---------------------|------------------|
| 03-1 | `plot03_01_missing_values.png` | Missing Data: Only One Column Affected | Heatmap + bar of NaN locations | Only `total_bedrooms` has missing values (~207 rows, <1%); solution: drop those rows |
| 03-2 | `plot03_02_target_distribution.png` | The Target Variable: Right-Skewed with a Hard Ceiling | Histogram before and after ÷100 000 scaling | ~4% of districts hit the $500K hard cap — this artefact directly causes under-prediction in expensive regions |
| 03-3 | `plot03_03_feature_distributions.png` | All 8 Input Features: Highly Skewed | Histogram + KDE for all 8 numeric features | Count-based features (total_rooms, population) are heavily right-skewed — this is why StandardScaler is essential before feeding them to the MLP |
| 03-4 | `plot03_04_scaler_effect.png` | StandardScaler: Levelling the Playing Field | Before vs after scaling (mean and std per feature) | Without scaling, large-magnitude features (total_rooms ~2600 avg) would dominate gradient updates; after scaling all features have mean≈0, std≈1 |
| 03-5 | `plot03_05_correlation_matrix.png` | Feature Correlations: Income Dominates | Pearson correlation heatmap of 8 features + target | `median_income` r=0.69 is the single strongest predictor; the four count features (rooms/bedrooms/population/households) are all highly correlated with each other |
| 03-6 | `plot03_06_target_correlations.png` | Which Features Matter Most? | Sorted bar of Pearson r with target | `median_income` is far ahead; `latitude` and `longitude` together encode the geographic price premium; count features contribute little |
| 03-7 | `plot03_07_feature_vs_target_scatter.png` | Every Feature vs House Value | 8 scatter panels, one per feature | The $500K ceiling appears as a horizontal band in every plot — it distorts the relationship every feature has with the target |
| 03-8 | `plot03_08_hexbin_income_value.png` | The Core Relationship: Income → Price | Density hexbin of median_income vs house value | The strongest single predictor; the hard ceiling at $500K is unmistakable as a flat horizontal band of dense points |
| 03-9 | `plot03_09_ocean_proximity.png` | Ocean Proximity: Class Imbalance + Price Gap | Count bar + price boxplot side by side | INLAND = 43% of data; ISLAND < 1%; each category has a distinct price profile that the 5 one-hot columns encode for the MLP |
| 03-10 | `plot03_10_onehot_mean_values.png` | What Each One-Hot Column Signals | Mean house value when each dummy = 1 vs 0 | The 5 binary columns carry very different average price signals — e.g. NEAR BAY average ~$260K vs INLAND ~$125K |
| 03-11 | `plot03_11_geo_price_map.png` | California Price Map | Geographic scatter coloured by value, sized by population | Bay Area (~37-38°N) and LA (~34°N) are the high-price clusters — this spatial structure is what `latitude` and `longitude` encode |
| 03-12 | `plot03_12_standardised_boxplots.png` | Outliers Survive Scaling | Box plots of all features after StandardScaler | Count features still have extreme outliers (>10 std) after scaling — these become extreme MLP inputs that can harm training stability |
| 03-13 | `plot03_13_train_test_distributions.png` | Train/Test Split Is Representative | KDE of income and price for train vs test | Both distributions overlap tightly — the 80/20 random split (random_state=42) is fair and test evaluation is valid |

---

## NOTEBOOK 04 · Statistical Analysis of Training Data
> *Theme for slides: "Statistical Properties That Explain Model Behaviour"*

| # | File | Slide Title Suggestion | What the plot shows | Key thing to say |
|---|------|------------------------|---------------------|------------------|
| 04-1 | `plot04_01_distribution_fitting.png` | House Values Follow a Log-Normal Distribution | Histogram with Normal and Log-Normal PDF fits | Log-normal fits the data much better; MSE loss treats over- and under-prediction symmetrically but the target is not symmetric — this mismatch affects training |
| 04-2 | `plot04_02_qq_plots.png` | The Target Is Not Normal | Q-Q plots before and after log transform | The flat right tail in the original Q-Q plot IS the $500K cap; log transform fixes most of the non-normality |
| 04-3 | `plot04_03_price_cap_analysis.png` | The $500K Cap: A Systematic Bias in the Data | 3-panel: histogram with cap zone, count per category, % per category | NEAR BAY and NEAR OCEAN categories have the highest proportion of capped districts — directly explains why the model under-predicts coastal homes |
| 04-4 | `plot04_04_capped_geo_map.png` | Capped Districts Are Clustered Geographically | California map: red = capped (≥$500K), blue = normal | Capped districts concentrate in Bay Area and LA — matching the regional under-prediction pattern found in the evaluation notebook |
| 04-5 | `plot04_05_anova_ocean_proximity.png` | Location Categories Are Statistically Distinct | Violin plot + ANOVA F-stat and p-value | F-statistic is very large, p << 0.001 — the five ocean proximity groups have genuinely different price distributions, not just noise; justifies using them as features |
| 04-6 | `plot04_06_iqr_outliers.png` | High Outlier Rate in Count Features | Bar of IQR outlier % per feature | `total_rooms`, `population`, `households` have 20-30% of rows as IQR outliers — the MLP receives extreme input values even after scaling |
| 04-7 | `plot04_07_features_by_proximity.png` | How Each Feature Differs Across Regions | 8-panel box plots split by ocean proximity | Shows what the one-hot columns help the MLP discriminate — ISLAND and NEAR BAY districts have distinct feature profiles in nearly every dimension |
| 04-8 | `plot04_08_price_heatmap_grid.png` | California's Non-Linear Price Surface | Grid heatmap coloured by mean price per lat/lon bin | The price surface is highly non-linear and spatially concentrated — a single linear layer could never capture this, justifying the deep 3-layer MLP architecture |
| 04-9 | `plot04_09_lat_lon_price_profile.png` | Two Price Peaks Along Latitude | Mean price along latitude and longitude separately | Two distinct peaks along latitude (~34°N LA and ~37-38°N Bay Area); the model must learn this non-linear curve using only the raw coordinate as input |
| 04-10 | `plot04_10_descriptive_stats_heatmap.png` | Training Data: Before and After Scaling | Colour-coded stats table (original vs standardised) | After StandardScaler: every feature has mean≈0, std≈1 — the equal-scale input space is what allows SGD to converge stably |
| 04-11 | `plot04_11_age_analysis.png` | Housing Age Has Weak Predictive Power | Histogram of age + mean price per age bin | r≈0.11 with price — age barely correlates with value because location effects dominate; a 40-year-old house in SF is worth more than a new one inland |
| 04-12 | `plot04_12_multicollinearity_pairplot.png` | Four Features Say Nearly the Same Thing | Pairplot scatter matrix of the four count features | All four pairs have r > 0.9 — they are near-redundant inputs; the MLP's weights for these features will be unstable and interchangeable |

---

## Total Plot Count: 25 plots across notebooks 03 and 04

---

## Recommended Presentation Narrative Order

```
INTRO
  └── 03-11  California Price Map (visual hook)
  └── 03-2   Target distribution + $500K cap (sets up the core problem)

DATA OVERVIEW
  └── 03-1   Missing values (preprocessing justification)
  └── 03-3   Feature distributions (skewness → why scaling needed)
  └── 03-4   StandardScaler effect (preprocessing payoff)

FEATURE ANALYSIS
  └── 03-6   Correlation bar (which features matter)
  └── 03-8   Income vs price hexbin (strongest signal)
  └── 03-5   Correlation matrix (full picture + multicollinearity)
  └── 03-9   Ocean proximity (class imbalance + price gap)
  └── 03-10  One-hot mean values (what the dummy columns encode)

STATISTICAL DEPTH
  └── 04-1   Distribution fitting (log-normal nature)
  └── 04-5   ANOVA (location groups are real, not noise)
  └── 04-8   Price heatmap (non-linear surface → justifies deep MLP)
  └── 04-9   Lat/lon price profiles (two geographic peaks)
  └── 04-12  Multicollinearity pairplot (redundant inputs)

THE $500K PROBLEM (connects EDA → evaluation findings)
  └── 04-3   Cap analysis (3-panel: where, how many, which category)
  └── 04-4   Capped districts map (geographic concentration)
  └── 03-7   Feature vs target scatter (cap visible in every feature)

DATA QUALITY WRAP-UP
  └── 03-12  Standardised boxplots (outliers survive scaling)
  └── 03-13  Train/test split check (evaluation is fair)
  └── 04-11  Age analysis (weak feature — shows not all features are equal)
```
