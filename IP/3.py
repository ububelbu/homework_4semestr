import numpy as np

g = 9.81
y0 = 0
y0_1 = -30


def func2(x, y, y1):
    return g


eps = 1e-3
t = [0]
y = [y0]
y_1 = [y0_1]
for tau in np.arange(eps, 10, eps):
    pass
