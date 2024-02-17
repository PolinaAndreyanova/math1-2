import math


def f(x):
    f_x = 3 * math.cos(2 * x) - x + 0.25
    return float(format(f_x, '.10f'))


def simple_iteration_method(x):
    next_x = x - 0.1 * (3 * math.cos(2 * x) - x + 0.25)
    return float(format(next_x, '.10f'))


def newtons_method(x):
    next_x = x - ((3 * math.cos(2 * x) - x + 0.25) / (-6 * math.sin(2 * x) - 1))
    return float(format(next_x, '.10f'))


def modified_newton_method(x):
    next_x = x - ((3 * math.cos(2 * x) - x + 0.25) / (-6 * math.sin(2 * (-0.9)) - 1))
    return float(format(next_x, '.10f'))
