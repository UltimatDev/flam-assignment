# FLAM Assignment

# Parametric Curve Parameter Estimation

## Objective

The goal of this assignment is to estimate the unknown parameters **θ (theta)**, **M**, and **X** of a given parametric curve using the provided dataset. The estimated parameters should generate a curve that closely matches the observed data by minimizing the **L1 distance** between the observed and predicted points.

---

## Mathematical Model

The given parametric equations are

\[
x(t)=t\cos(\theta)-e^{M|t|}\sin(0.3t)\sin(\theta)+X
\]

\[
y(t)=42+t\sin(\theta)+e^{M|t|}\sin(0.3t)\cos(\theta)
\]

where

- **θ** controls the orientation of the trajectory.
- **M** controls the exponential component, affecting the oscillatory behaviour.
- **X** translates the curve horizontally.

The parameter \(t\) is sampled uniformly in the range

\[
6 \le t \le 60
\]

---

## Project Structure

```text
flam-assignment/
│
├── exploration.ipynb      # Complete notebook containing analysis and observations
├── curve.py               # Parametric curve implementation
├── loss.py                # L1 loss function and objective function
├── optimize.py            # SciPy optimization routine
├── xy_data.csv            # Provided dataset
├── figures/               # Generated plots
├── requirements.txt
└── README.md
```

---

## Workflow

The project was completed in the following stages.

### 1. Dataset Inspection

The dataset was first inspected using Pandas.

Functions used:

- `head()`
- `info()`
- `describe()`

Observations:

- Dataset contains 1500 observations.
- Two numerical variables (`x` and `y`).
- No missing values.
- Data is suitable for curve fitting.

---

### 2. Data Visualization

The dataset was visualized using a scatter plot.

Observations:

- The points form a smooth continuous trajectory.
- No noticeable outliers are present.
- The curve exhibits oscillatory behaviour.
- The overall shape appears consistent with the provided mathematical model.

---

### 3. Mathematical Model

The given equations were implemented in Python as a reusable function.

```python
curve(t, theta, M, X)
```

The implementation converts θ from degrees to radians before evaluating the trigonometric functions.

---

### 4. Initial Curve Generation

To verify the implementation, an initial curve was generated using manually selected parameters.

Initial values:

- θ = 20°
- M = -0.01
- X = 30

These values were chosen only to confirm that the equations had been implemented correctly.

---

### 5. Parameter Exploration

Each parameter was varied independently while keeping the remaining parameters fixed.

#### Effect of θ

- Rotates the trajectory.
- Changes the orientation of the curve.
- Does not significantly change the overall shape.

#### Effect of X

- Shifts the entire curve horizontally.
- Does not affect the shape of the trajectory.

#### Effect of M

- Controls the exponential term.
- Changes the magnitude of oscillations.
- Influences the overall shape of the curve.

This exploration helped develop intuition about the role of each parameter before optimization.

---

### 6. Initial Comparison

The manually generated curve was compared with the observed dataset.

Although the overall trend was similar, several differences remained between the predicted and observed trajectories. This indicated that manually selecting parameter values was insufficient and motivated the need for numerical optimization.

---

### 7. Loss Function

The assignment evaluates the solution using the **L1 distance** between the observed dataset and the predicted curve.

An objective function was therefore defined to compute the average absolute difference between the observed and predicted coordinates.

This objective function is minimized during optimization.

---

### 8. Numerical Optimization

The unknown parameters were estimated using **SciPy's L-BFGS-B optimizer**.

The optimization was performed under the following parameter bounds:

| Parameter | Range |
|-----------|-------|
| θ | 0° – 50° |
| M | -0.05 – 0.05 |
| X | 0 – 100 |

The optimizer iteratively updated the parameters until the L1 loss could no longer be reduced significantly.

---

### 9. Estimated Parameters

The optimization converged successfully and produced the following parameter estimates.

| Parameter | Estimated Value |
|-----------|----------------:|
| θ | 28.12° |
| M | 0.02113 |
| X | 56.89 |

Final L1 Loss

```
12.6216
```

---

### 10. Final Comparison

The optimized curve was plotted together with the observed dataset.

The optimized model closely follows the overall trajectory of the observed data and captures both the orientation and oscillatory behaviour of the curve. Compared to the initial manually selected parameters, the optimized parameters provide a much better fit.

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- SciPy
- Jupyter Notebook

---

## Repository Overview

| File | Description |
|------|-------------|
| `exploration.ipynb` | Complete analysis, visualizations, optimization, and observations |
| `curve.py` | Implementation of the parametric equations |
| `loss.py` | L1 loss and objective function |
| `optimize.py` | Parameter optimization using SciPy |
| `xy_data.csv` | Dataset provided for the assignment |
| `figures/` | Generated plots and visualizations |

---

## Conclusion

This project demonstrates how exploratory analysis and numerical optimization can be combined to estimate unknown parameters of a mathematical model. By first understanding the influence of each parameter individually and then minimizing an L1 objective function, the model was able to closely reproduce the observed trajectory. The final optimized parameters provide the best fit within the specified parameter constraints and significantly improve upon the initial manually selected values.