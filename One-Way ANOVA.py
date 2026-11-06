import numpy as np
import pandas as pd
import scipy.stats as stats


np.random.seed(42)


control = np.random.normal(loc=10.2, scale=1.5, size=30)
treated_drugA = np.random.normal(loc=10.5, scale=1.2, size=30)
treated_drugB = np.random.normal(loc=14.1, scale=1.6, size=30)


f_stat, p_val = stats.f_oneway(control, treated_drugA, treated_drugB)

# 3. PRINT RESULTS
print(f"F-Statistic: {f_stat:.4f}")
print(f"P-value:     {p_val:.4e}")

if p_val < 0.05:
    print("\nResult: Statistically significant! At least one group differs.")
else:
    print("\nResult: Not significant. No statistical difference between groups.")

