## REQUIREMENTS
**Dataset Quality Score (DQS).** A composite, reproducible, and documented score that measures how “good” a synthetic dataset is:
- *Statistical fidelity* — how well it preserves the distributions, correlations, and properties of the original data
- *Utility* — does a model trained on synthetic data perform comparably to one trained on real data? (TSTR paradigm: Train on Synthetic, Test on Real)
- *Privacy / leakage* — synthetic data does not store or “leak” real records (tests such as membership inference and distance to the nearest neighbor in the original dataset)
- *Diversity and coverage* — does the synthetic data cover the entire space, including rare cases, not just the “average” range?
- *Sensitivity to noise* — how all of the above metrics evolve as a function of the ε budget: the score must be reported alongside the DP level at which the dataset was generated; otherwise, comparisons are meaningless (a DQS of 85 at ε=10 is not comparable to a DQS of 85 at ε=1)
