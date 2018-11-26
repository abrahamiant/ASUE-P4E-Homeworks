# calculates and returns value of the given function at point x
def f(x):
    return 0.05 * x ** 4 + 0.1 * x ** 3 + 0.5 * x **2 + 10 * x + 5

# calculates and returns value of the first
# derivative of the given function at point x
def f_d1(x):
    return 0.2 * x ** 3 + 0.3 * x ** 2 +  x + 10

# calculates and returns value of the second
# derivative of the given function at point x
def f_d2(x):
    return 0.6 * x ** 2 + 0.6 * x + 1

eps = 0.01
x_min = float(input("initial x_min: "))

i = 1
while abs(f_d1(x_min)) > eps:
    x_min = x_min - f_d1(x_min) / f_d2(x_min)
    print(f"Estimated value of x_min after iteration {i}: {x_min}")
    i += 1

print()
print(f"x_min = {x_min}")
print(f"y_min = {f(x_min)}")
