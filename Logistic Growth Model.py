import os

from scipy.integrate import odeint
import numpy as np
import matplotlib

if os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"):
    try:
        matplotlib.use("TkAgg")
    except Exception:
        matplotlib.use("Agg")
else:
    matplotlib.use("Agg")

import matplotlib.pyplot as plt


# System of differential equations
def logistic_growth(variables, t, params):
    x = variables[0]
    r, k = params
    dx_dt = r * x * (1 - x / k)
    return [dx_dt]


def main():
    # Initial conditions
    y0 = [1.0]  # start with 1 cell

    # Time points
    t = np.linspace(0, 500, num=1000)

    # Parameters
    r = 0.05
    k = 100000
    params = [r, k]

    # Integrate ODE
    y = odeint(logistic_growth, y0, t, args=(params,))

    # Plot results
    plt.plot(t, y[:, 0], label="Population")
    plt.xlabel("Time")
    plt.ylabel("Cells")
    plt.title("Logistic Growth Model")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
