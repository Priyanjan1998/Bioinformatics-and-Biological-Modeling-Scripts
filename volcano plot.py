import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
n_genes = 1000
log2FC = np.random.normal(loc=0, scale=1.5, size=n_genes)
pvalues = np.random.uniform(0, 1, size=n_genes) * (1 / (np.abs(log2FC) + 0.1))
pvalues = np.clip(pvalues, 1e-10, 1)


df = pd.DataFrame({"log2FC": log2FC, "pvalue": pvalues})


FC_threshold = 1.0
P_threshold = 0.05

df["minus_log10_p"] = -np.log10(df["pvalue"])

conditions = [
    (df["log2FC"] >= FC_threshold) & (
        df["minus_log10_p"] >= -np.log10(P_threshold)),
    (df["log2FC"] <= -FC_threshold) & (df["minus_log10_p"] >= -np.log10(P_threshold)),
]
df["Expression"] = np.select(conditions, ["Up", "Down"], default="NS")

plt.figure(figsize=(8, 6))
sns.scatterplot(
    data=df,
    x="log2FC",
    y="minus_log10_p",
    hue="Expression",
    palette={"Up": "#ff4d4d", "Down": "#1e90ff", "NS": "#d3d3d3"},
    alpha=0.8,
    edgecolor=None,
    s=20,
)

plt.axvline(x=FC_threshold, color="black", linestyle="--", linewidth=1)
plt.axvline(x=-FC_threshold, color="black", linestyle="--", linewidth=1)
plt.axhline(y=-np.log10(P_threshold), color="black",
            linestyle="--", linewidth=1)

plt.xlabel("log2 Fold Change")
plt.ylabel("-log10(P-value)")
plt.tight_layout()
plt.show()
