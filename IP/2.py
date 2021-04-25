import time
import numpy as np


def func(x):
    return x ** 2


def integration(func, a, b, eps):
    total = 0
    for x in np.arange(a, b, eps):
        total += func(x) * eps
    return total

def integration1(func, a, b, eps):
    total = 0
    for x in np.arange(a, b, eps):
        total += func(x + eps) * eps
    return total

def integration_trapezoid(func, a, b, eps):
    total = 0
    for x in np.arange(a, b, eps):
        total += (func(x) + func(x + eps))/2 * eps
    return total


a = -1
b = 2
eps = 0.1
t = time.time()
print(integration_trapezoid(func, a, b, eps))
print(time.time()-t)