import math

def f(x):
    return 3 * math.cos(2 * x) - x + 0.25


def simple_iteration_method(x):
    next_x = x - 0.1 * (3 * math.cos(2 * x) - x + 0.25)
    return next_x


def newtons_method(x):
    next_x = x - ((3 * math.cos(2 * x) - x + 0.25) / (-6 * math.sin(2 * x) - 1))
    return next_x


def modified_newton_method(x):
    next_x = x - ((3 * math.cos(2 * x) - x + 0.25) / (-6 * math.sin(2 * (-0.9)) - 1))
    return next_x


print("n\t\tx_n\t\tx_n+1\t\t|x_n+1 - x_n|\t\t|f(x_n+1)|")

n = 0
x = -0.9
e = 0.001
d = 0.01

# next_x = simple_iteration_method(x)
# next_x = newtons_method(x)
next_x = modified_newton_method(x)

print(str(n) + '\t\t' + str(x) + '\t\t' + str(next_x) + '\t\t' + str(abs(next_x - x)) + '\t\t' + str(abs(f(next_x))))

while (abs(next_x - x) > e) or (abs(f(next_x)) > d):
    print(str(n) + '\t\t' + str(x) + '\t\t' + str(next_x) + '\t\t' + str(abs(next_x - x)) + '\t\t' + str(abs(f(next_x))))
    n += 1
    prom_x = x
    x = next_x
    # next_x = simple_iteration_method(x)
    # next_x = newtons_method(x)
    next_x = modified_newton_method(x)

# print(str(n) + '\t\t' + str(x) + '\t\t' + str(next_x) + '\t\t' + str(abs(next_x - x)) + '\t\t' + str(abs(f(next_x))))