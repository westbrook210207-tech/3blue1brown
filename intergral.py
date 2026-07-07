import numpy as np
x1, x2 = 1, 5
x = np.linspace(x1, x2, 1000)
y = x**3
area = np.trapezoid(y, x)
print(area)