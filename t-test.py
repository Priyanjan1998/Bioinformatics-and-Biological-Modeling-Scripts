import scipy.stats as stats

group1 = [10.2, 9.8, 11.5, 10.1]
group2 = [10.5, 11.2, 10.8, 11.1]
group3 = [14.1, 13.8, 14.5, 13.9]

f_stat, p_val = stats.f_oneway(group1, group2, group3)

print(f"F-Statistic: {f_stat}")
print(f"P-value: {p_val}")
