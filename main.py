from print_table import print_row
import f

# method = 'simple_iteration_method'
method = 'newtons_method'
# method = 'modified_newton_method'
n = 0
x = -0.9
e = 0.001
d = 0.01

header = ['n', 'x_n', 'x_n+1', '|x_n+1 - x_n|', '|f(x_n+1)|']
print_row(header)
print("-+-".join('-' * 15 for _ in range(5)))

while True:
    if method == 'simple_iteration_method':
        next_x = f.simple_iteration_method(x)
    elif method == 'newtons_method':
        next_x = f.newtons_method(x)
    else:
        next_x = f.modified_newton_method(x)

    e_param = float(format(abs(next_x - x), '.10f'))
    d_param = abs(f.f(next_x))

    if (e_param <= e) and (d_param <= d):
        break

    print_row([str(n), str(x), str(next_x), str(e_param), str(d_param)])

    n += 1
    x = next_x
