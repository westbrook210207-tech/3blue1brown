import numpy as np
x1, x2 = 1, 5
x = np.linspace(x1, x2, 1000)
y = x**3
area = np.trapezoid(y, x) # integral of y with respect to x using the trapezoidal rule
print(area)

x3, x4 = 1,1.000001
x = np.linspace(x3, x4, 2)
y = x**3
derivative = np.gradient(y, x) # derivative of y at x using the gradient function
print(derivative) 