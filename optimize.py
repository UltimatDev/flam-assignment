from scipy.optimize import minimize
from loss import objective

def optimize_curve(data):
    initial_guess = [20, -0.01, 30]

    bounds = [
        (0, 50),       # theta
        (-0.05, 0.05), # M
        (0, 100)       # X
    ]

    result = minimize(
        objective,
        initial_guess,
        args=(data,),
        method="L-BFGS-B",
        bounds=bounds,
    )

    return result