# FLAM Assignment

# Parametric Curve Parameter Estimation

## Objective

The objective of this assignment is to estimate the unknown parameters **θ (theta)**, **M**, and **X** of the given parametric curve using the provided dataset. The estimated parameters should generate a curve that best matches the observed data by minimizing the **L1 distance** between the predicted and observed points.

Rather than directly applying an optimization algorithm, the work was approached in stages—first understanding the dataset and the behaviour of the mathematical model, then defining an appropriate objective function, and finally estimating the parameters numerically.

---

## Mathematical Model

The given parametric equations are

[
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
]

[
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
]

where

* **θ** controls the orientation of the trajectory.
* **M** controls the exponential component, affecting the amplitude of the oscillations.
* **X** shifts the entire curve horizontally.

The parameter **t** is sampled uniformly in the range

[
6 \le t \le 60
]


# Methodology

Instead of treating this purely as an optimization problem, I first tried to understand both the dataset and the influence of each parameter. This made it easier to define suitable parameter ranges and verify that the mathematical model had been implemented correctly before running the optimizer.

## 1. Understanding the Dataset

The first step was to inspect the dataset using Pandas.

The following functions were used:

* `head()`
* `info()`
* `describe()`

### Observations

* The dataset contains **1500 observations**.
* Both columns are numerical.
* No missing values were present.
* The dataset required no preprocessing before analysis.

---

## 2. Visualizing the Data

A scatter plot was generated to understand the overall structure of the observations.

### Observations

* The points form a smooth continuous trajectory.
* No obvious outliers are present.
* The curve exhibits a periodic oscillatory pattern.
* The overall shape resembles the mathematical model provided in the assignment.

This visualization also served as a reference for comparing later optimization results.

---

## 3. Implementing the Parametric Curve

The mathematical equations were implemented as a reusable Python function.

```python
curve(t, theta, M, X)
```

Since the optimization operates using degrees for θ, the implementation converts θ into radians before evaluating the trigonometric functions.

At this stage the objective was simply to ensure that the implementation reproduced the mathematical equations correctly.

---

## 4. Initial Curve Generation

Before attempting optimization, I generated the curve using manually selected parameter values.

Initial parameters:

* θ = 20°
* M = -0.01
* X = 30

These values were not expected to fit the data accurately. Their purpose was only to verify that the equations behaved as expected and produced a reasonable trajectory.

---

## 5. Exploring Individual Parameters

To build intuition about the model, each parameter was varied independently while keeping the remaining parameters fixed.

### Effect of θ

* Rotates the trajectory.
* Changes the overall orientation.
* Has little influence on the curve's shape.

### Effect of X

* Produces a horizontal translation.
* Does not change the geometry of the curve.

### Effect of M

* Controls the exponential component.
* Changes the magnitude of the oscillations.
* Has the largest influence on the overall appearance of the trajectory.

Performing this exploration made it easier to understand how the optimizer would later adjust each parameter.

---

## 6. Comparing the Initial Fit

The manually generated curve was plotted alongside the observed dataset.

Although the general trend was similar, noticeable differences remained in both orientation and oscillation magnitude. This confirmed that manual parameter selection would not be sufficient and motivated the use of numerical optimization.

---

## 7. Defining the Objective Function

The assignment specifies minimizing the **L1 distance** between the generated curve and the observed dataset.

Accordingly, an objective function was implemented that computes the average absolute error between the predicted and observed coordinates.

Using L1 loss makes the optimization less sensitive to large individual deviations while still producing an overall good fit across the dataset.

---

## 8. Parameter Optimization

The unknown parameters were estimated using **SciPy's L-BFGS-B optimizer**.

Parameter bounds:

| Parameter | Search Range |
| --------- | -----------: |
| θ         |     0° – 50° |
| M         | -0.05 – 0.05 |
| X         |      0 – 100 |

The optimizer repeatedly evaluated the objective function and updated the parameter values until no further meaningful reduction in L1 loss was achieved.

---

## 9. Estimated Parameters

The optimization converged successfully and produced the following estimates.

| Parameter | Estimated Value |
| --------- | --------------: |
| θ         |          28.12° |
| M         |         0.02113 |
| X         |           56.89 |

### Final L1 Loss

```text
12.6216
```

---

## 10. Final Result

The optimized curve was plotted together with the observed dataset.

Compared to the initial manually selected parameters, the optimized curve aligns much more closely with the observed trajectory. The optimization successfully captures both the orientation of the curve and the oscillatory behaviour introduced by the exponential component.

---

# Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* SciPy
* Jupyter Notebook

---

# Repository Overview

| File                | Purpose                                                                                |
| ------------------- | -------------------------------------------------------------------------------------- |
| `exploration.ipynb` | Complete exploratory analysis, parameter exploration, optimization, and visualizations |
| `curve.py`          | Parametric curve implementation                                                        |
| `loss.py`           | L1 loss and optimization objective                                                     |
| `optimize.py`       | Optimization routine using SciPy                                                       |
| `xy_data.csv`       | Provided dataset                                                                       |
| `figures/`          | Generated plots                                                                        |

---

# Possible Improvements

While the current solution produces a good fit, several extensions could be explored in future work:

* Multi-start optimization using different initial guesses.
* Global optimization methods such as Differential Evolution.
* Adaptive parameter search before local optimization.
* Comparison of L1 and L2 objective functions.
* Sensitivity analysis to better understand parameter influence.

---

# Conclusion

This assignment was approached by first understanding the behaviour of the dataset and the mathematical model before attempting optimization. Exploring the influence of each parameter helped verify the implementation and provided intuition about the search space.

The final parameter estimates were obtained by minimizing the L1 objective function using SciPy's L-BFGS-B optimizer. The optimized model closely reproduces the observed trajectory while remaining within the specified parameter bounds, demonstrating an effective combination of exploratory analysis and numerical optimization.
