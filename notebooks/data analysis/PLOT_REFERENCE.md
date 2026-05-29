# 📊 California Housing — Complete Plot Reference Guide
## For use in PPTX / Essay presentations

---

## How to use this guide
Each row maps a **plot file → slide description → what to say**.  
Run notebooks 03→06 in order; all plots are saved to `outputs/`.

---

## NOTEBOOK 03 · Feature Engineering & Advanced EDA
> *Theme for slides: "Understanding the Data"*

| # | File | Slide Title Suggestion | What the plot shows | Key thing to say |
|---|------|------------------------|---------------------|------------------|
| 03-1 | `plot03_01_derived_distributions.png` | Engineered Feature Distributions | Histograms of rooms/household, bedroom ratio, population density | Raw counts are misleading — per-household ratios reveal true density |
| 03-2 | `plot03_02_full_correlation_heatmap.png` | Full Feature Correlation Matrix | Heatmap of all pairwise Pearson correlations | `median_income` has the highest correlation (~0.69) with house value; `bedrooms_per_room` shows useful negative signal |
| 03-3 | `plot03_03_target_correlations.png` | Feature Ranking: Correlation with Price | Sorted bar chart of each feature's correlation with target | Clean, simple justification for which features to prioritise in modelling |
| 03-4 | `plot03_04_value_by_income_category.png` | Income → Price: Strong Monotonic Link | Boxplots of house value across 5 income tiers | Every income tier occupies a distinct price band — income is the dominant predictor |
| 03-5 | `plot03_05_features_by_ocean_proximity.png` | Feature Profiles by Location | 6-panel boxplot grid split by ocean proximity | Island and near-bay areas are statistical outliers in nearly every dimension |
| 03-6 | `plot03_06_pairplot_income.png` | Multivariate View: Income Colour-Coded | Scatter matrix of 5 key features, hue = income tier | Shows multivariate cluster separation — higher income groups occupy distinct regions of feature space |
| 03-7 | `plot03_07_rooms_vs_value.png` | More Rooms → Higher Value? | Scatter of rooms/household vs house value with regression line | Positive trend confirmed (r≈0.15 after outlier removal); income colours show confounding effect |
| 03-8 | `plot03_08_age_violin.png` | Housing Age by Location | Violin plot of housing age across proximity categories | Coastal / island areas have older housing stock — could reflect historical development patterns |
| 03-9 | `plot03_09_stacked_bar_income_proximity.png` | Where Do Rich Districts Live? | Stacked bar of ocean proximity composition per income tier | Higher income categories are disproportionately found near water — geography and affluence correlate |
| 03-10 | `plot03_10_hexbin_income_value.png` | The Core Relationship: Income vs Price | Density hexbin of income vs house value | Shows ~20,000 districts; hard $500K price ceiling is a clear artefact in the dataset |

---

## NOTEBOOK 04 · Statistical Analysis & Geographic Clustering
> *Theme for slides: "What the Data Tells Us Statistically"*

| # | File | Slide Title Suggestion | What the plot shows | Key thing to say |
|---|------|------------------------|---------------------|------------------|
| 04-1 | `plot04_01_iqr_outliers.png` | Outlier Prevalence by Feature | Horizontal bar of IQR-detected outlier % per feature | `population_per_household` has ~25% of rows as outliers — some districts are extreme communal housing or resort areas |
| 04-2 | `plot04_02_zscore_outlier_map.png` | Where Are the Price Outliers? | California map with extreme-price districts highlighted in red | Price outliers (~1%) are spatially concentrated in Bay Area and LA coastal zones |
| 04-3 | `plot04_03_distribution_fitting.png` | House Values Follow a Log-Normal | Histogram overlaid with Normal and Log-Normal fits | Log-normal fits data far better — implies percentage changes in price matter more than absolute amounts |
| 04-4 | `plot04_04_qq_plots.png` | Q-Q: Log Transform Improves Normality | Q-Q plots before and after log transform | Original distribution deviates heavily from normal (S-curve); log transform substantially improves this |
| 04-5 | `plot04_05_geo_clusters.png` | 6 Regional Housing Markets | California map with KMeans geographic clusters and mean prices | Distinct regional markets emerge: Bay Area, LA, San Diego, Central Valley, etc. |
| 04-6 | `plot04_06_price_heatmap_grid.png` | The California Price Map | Grid heatmap coloured by mean house value | Instantly shows that coastal / urban areas command premiums; inland valleys are uniformly lower-priced |
| 04-7 | `plot04_07_anova_ocean_proximity.png` | Location Proximity Differences Are Statistically Real | Violin plot + ANOVA test result | F-statistic and p-value confirm location price differences are not random; ANOVA p << 0.001 |
| 04-8 | `plot04_08_cluster_radar.png` | Regional Cluster Profiles | Spider/radar chart of normalised feature means per cluster | Each cluster has a unique "fingerprint" — e.g. cluster with highest price also has highest income and lowest population density |
| 04-9 | `plot04_09_age_cohort_analysis.png` | Age Doesn't Drive Price — Location Does | Bar + box of price by housing age cohort | 30–40 year old housing is often more expensive than newer stock due to location (e.g., San Francisco older homes) |
| 04-10 | `plot04_10_elbow_kmeans.png` | Choosing 6 Clusters: The Elbow Method | WCSS vs k plot | The elbow at k≈5-6 validates our choice; beyond k=6, additional clusters add minimal explanatory value |

---

## NOTEBOOK 05 · Model Training & Comparison
> *Theme for slides: "Building and Comparing Prediction Models"*

| # | File | Slide Title Suggestion | What the plot shows | Key thing to say |
|---|------|------------------------|---------------------|------------------|
| 05-1 | `plot05_01_model_comparison_metrics.png` | 7 Models, 3 Metrics | Three horizontal bar charts: RMSE, MAE, R² | Gradient Boosting and Random Forest clearly dominate; linear models plateau around R²=0.65 |
| 05-2 | `plot05_02_cv_r2_errorbars.png` | Consistency Matters: Cross-Validation | CV R² with error bars (5-fold) | Ensemble models are not just better — they're also more consistent across data splits (smaller std) |
| 05-3 | `plot05_03_time_vs_r2.png` | Accuracy vs Training Cost | Scatter: training time vs R², bubble = RMSE | Engineering trade-off slide: RF/GB take 10-30× longer but deliver ~20% better R² |
| 05-4 | `plot05_04_regularisation_path.png` | Finding the Right Regularisation | RMSE vs α for Ridge and Lasso | Both converge on similar optimal range; Lasso's path drops faster, making feature selection implicit |
| 05-5 | `plot05_05_dt_depth_tuning.png` | Overfitting in Plain Sight | Train vs test R² as tree depth increases | Classic textbook overfitting curve; gap between curves widens beyond depth 8-10 |
| 05-6 | `plot05_06_learning_curves_rf.png` | Does More Data Help? | Learning curves for Random Forest | Converging curves suggest low bias; slight gap means model would still benefit from more training data |
| 05-7 | `plot05_07_model_radar.png` | At-a-Glance Model Comparison | Radar chart of 4 metrics for all models | Visual executive summary — ensemble models fill the outer ring; linear models stay inner |
| 05-8 | `plot05_08_performance_heatmap.png` | Model Scorecard | Colour-coded metric table | Data-dense single-slide summary for technical audiences; green = best, red = worst |

---

## NOTEBOOK 06 · Model Evaluation & Interpretability
> *Theme for slides: "How Good Are Our Predictions — and Why?"*

| # | File | Slide Title Suggestion | What the plot shows | Key thing to say |
|---|------|------------------------|---------------------|------------------|
| 06-1 | `plot06_01_pred_vs_actual.png` | How Close Are Our Predictions? | Predicted vs actual for LR, RF, GB | RF/GB points hug the diagonal; LR under-predicts luxury homes — linear relationship assumption breaks down |
| 06-2 | `plot06_02_residual_distributions.png` | Prediction Error Distributions | Residual histograms for three models | RF/GB residuals centred near $0 with much smaller spread; LR has systematic over/under-prediction |
| 06-3 | `plot06_03_residuals_vs_predicted.png` | Does Error Grow with Price? | Residuals vs predicted value | Slight heteroscedasticity at very high prices — model is less confident for luxury-tier homes |
| 06-4 | `plot06_04_geo_error_map.png` | Where Does the Model Struggle? | California map coloured by prediction error | Errors cluster in SF Bay Area and LA coastal zones — hyper-local market dynamics not fully captured |
| 06-5 | `plot06_05_feature_importance.png` | What Drives the Prediction? (Trees) | Impurity-based importance for RF vs GB | Both models rank `median_income`, `latitude`, `longitude` as top 3 — income and geography dominate |
| 06-6 | `plot06_06_permutation_importance.png` | Robust Feature Importance | Permutation importance on test set (RF) | More trustworthy than impurity importance — confirms income and coordinates are genuinely causal, not spurious |
| 06-7 | `plot06_07_partial_dependence.png` | How Each Feature Affects Price | PDP for top 4 features | Income has a near-linear positive effect; latitude shows a sharp spike for Bay Area coordinates (~37-38°N) |
| 06-8 | `plot06_08_error_by_bracket.png` | Error Is Highest for Expensive Homes | MAE per price bracket | $450K+ bracket MAE is ~2× the overall MAE — partly because the $500K cap distorts model learning |
| 06-9 | `plot06_09_error_by_proximity.png` | Accuracy Varies by Location Type | MAE/Median AE per ocean proximity | Island districts (very few samples, n<10) have the highest error; near-bay districts are best predicted |
| 06-10 | `plot06_10_cumulative_error.png` | 80% of Predictions Within $50K | Cumulative error distribution for all models | Business-friendly framing: "Our best model predicts within $50K for 80% of all California census districts" |
| 06-11 | `plot06_11_lr_coefficients.png` | What Does Linear Regression Learn? | Bootstrapped LR coefficients ± 95% CI | `median_income` largest positive coefficient; `bedrooms_per_room` negative (more bedrooms relative to rooms → lower value) |

---

## Total Plot Count: 39 plots across 4 notebooks

## Recommended Presentation Flow
```
INTRO
  └── Dataset overview (rows, features, target)
  └── 03-10  Hexbin (income vs price — the core story)

EDA
  └── 04-6   Price heatmap (California geography)
  └── 03-4   Value by income category (boxes)
  └── 03-2   Correlation heatmap
  └── 04-3   Distribution fitting (log-normal)

FEATURE ENGINEERING
  └── 03-1   Derived feature distributions
  └── 03-3   Feature importance bar (pre-model)
  └── 03-5   Features by ocean proximity

STATISTICAL INSIGHTS
  └── 04-5   Geographic clusters map
  └── 04-8   Cluster radar
  └── 04-7   ANOVA (location groups differ statistically)

MODELLING
  └── 05-1   Model comparison (3 metrics)
  └── 05-5   Overfitting curve (DT depth)
  └── 05-6   Learning curves (RF)
  └── 05-8   Performance scorecard heatmap

RESULTS & INTERPRETATION
  └── 06-1   Predicted vs Actual (3 models)
  └── 06-5   Feature importance (RF vs GB)
  └── 06-7   Partial dependence (top 4)
  └── 06-10  Cumulative error (business slide)
  └── 06-4   Geographic error map

CONCLUSION
  └── 05-7   Model radar (summary)
  └── Key numbers: best model R², RMSE, % within $50K
```
