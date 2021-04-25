import matplotlib.pyplot as plt
import numpy as np


def derivative_func(func, x, eps):
    return (func(x + eps)-func(x))/eps


def derivative_func1(func, x, eps):
    return (func(x)-func(x - eps))/eps


def derivative_func2(func, x, eps):
    return (func(x + eps)-func(x - eps))/(2*eps)


def func(x):
    return np.cos(x ** 3)


eps = 1e-7
x = np.linspace(-1, 1, 100)
y = func(x)
#derivative_func(func, arg, eps) for arg in np.linspace(0, 5, 1000)
plt.plot(x, y, "r")
plt.show()