import numpy as np
from curve import curve

def objective(params, data):
    theta, M, X = params

    t = np.linspace(6, 60, len(data))

    x_pred, y_pred = curve(t, theta, M, X)

    pred = np.column_stack((x_pred, y_pred))
    true = data[["x", "y"]].values

    return np.mean(np.abs(pred - true))