import random
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('tkagg')

X = [1]
t = [0]
tend = 400

r = 0.05
K = 100

while t[-1] < tend:
    current_X = X[-1]

    if current_X == 0:
        break

    rates = [r * current_X, r * (current_X**2) / K]
    rate_sum = sum(rates)

    tau = np.random.exponential(scale=1 / rate_sum)
    t.append(t[-1] + tau)

    rand = random.uniform(0, 1)

    if rand * rate_sum <= rates[0]:
        X.append(X[-1] + 1)
    else:
        X.append(X[-1] - 1)

plt.plot(t, X)
plt.xlabel("Time")
plt.ylabel("Cells")
plt.show()
