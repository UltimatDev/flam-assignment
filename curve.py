import numpy as np

def curve(t, theta, M, X):
    theta = np.radians(theta)
    
    x = (
        t*np.cos(theta) - np.exp(M*np.abs(t))*np.sin(0.3*t)*np.sin(theta) + X
    )
    
    y = (
        42
        + t*np.sin(theta)
        + np.exp(M*np.abs(t))*np.sin(0.3*t)*np.cos(theta)
    )

    return x,y