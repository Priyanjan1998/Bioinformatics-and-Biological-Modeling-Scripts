# Bioinformatics and Biological Modeling Scripts

This repository is a collection of standalone Python examples for exploring biological systems with numerical models, stochastic simulations, and basic statistical analysis. The scripts use synthetic or hard-coded inputs, run independently, and either display a plot or print a statistical result. There is no shared application entry point or command-line configuration.

## What is included

| Script | Description | Result |
| --- | --- | --- |
| `Activation Hill Function.py` | ODE model of an activating Hill-function gene interaction | Plot of two gene abundances over time |
| `Gene model repression.py` | ODE model of gene expression with Hill-function repression | Plot of two gene abundances over time |
| `first code on Bioinformatics.py` | Deterministic mRNA and protein production/degradation model | Plot of mRNA and protein abundance |
| `Oscillatory Gene Network.py` | Three-gene deterministic regulatory network with activating and repressing Hill functions | Three-panel abundance plot |
| `Gillespie Algorithm.py` | Stochastic single-species production and degradation simulation | Plot of molecule count over time |
| `More Gillespie.py` | Stochastic birth-death population model with density-dependent loss | Plot of population size over time |
| `Stocastic Oscillator.py` | Stochastic three-gene regulatory network simulation | Three-panel gene-count plot |
| `Logistic Growth Model.py` | Deterministic logistic population growth model | Plot of population size over time |
| `Predator-Prey Model.py` | Lotka-Volterra-style predator-prey ODE model | Separate plots of fish and bear populations |
| `One-Way ANOVA.py` | One-way ANOVA on three generated sample groups | F-statistic, p-value, and a significance message |
| `t-test.py` | One-way ANOVA on three small, hard-coded sample groups | F-statistic and p-value |
| `volcano plot.py` | Volcano plot generated from simulated fold changes and p-values | Scatter plot classifying points as up, down, or not significant |

The statistical scripts use example data, not measurements from a real experiment. In particular, despite its filename, `t-test.py` runs a one-way ANOVA (`scipy.stats.f_oneway`), not a t-test.

## Requirements

- Python 3
- Packages listed in [`requirements.txt`](requirements.txt): NumPy, SciPy, Matplotlib, pandas, and seaborn
- A graphical plotting environment for scripts that display figures. Several plotting scripts explicitly select Matplotlib's Tk backend, so a working Tk installation is also needed to open their plot windows.

## Setup

From the project directory, create and activate a virtual environment, then install the dependencies.

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell prevents virtual-environment activation, either adjust the execution policy for your user according to your organization's guidance, or run the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Usage

Run any script from the project directory with the environment activated. Quote filenames that contain spaces:

```powershell
python "Logistic Growth Model.py"
python "Oscillatory Gene Network.py"
python "volcano plot.py"
```

On macOS or Linux, the same commands work with `python` (or use `python3` if that is how Python is installed).

The modeling and plotting examples open interactive Matplotlib windows; close the plot window to finish the script. The ANOVA examples print their output directly in the terminal:

```powershell
python "One-Way ANOVA.py"
python "t-test.py"
```

Most parameters, initial conditions, and time ranges are defined near the top of each file and can be edited directly. The scripts currently do not accept command-line arguments, load external datasets, or save figures automatically.

## Contributing

Contributions that improve the examples while keeping them approachable are welcome:

1. Open an issue describing a bug, proposed improvement, or new example before making a substantial change.
2. Make a focused change in a separate branch and keep each script independently runnable.
3. Keep dependencies declared in `requirements.txt`; include clear units, assumptions, and parameter descriptions where useful.
4. Run the changed script after installing the requirements. For plotting scripts, verify that the figure opens; for statistical scripts, verify that the printed output is sensible.
5. Submit a pull request describing the change and how it was checked. Include sample output or a figure when it helps explain the change.

There is no automated test suite or formatting configuration in the repository at present.

## License

No license file is currently included. Please contact the project maintainer for permission and terms before redistributing or reusing this code.
