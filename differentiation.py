import numpy as np
def f(x):
 return x**3 + 2*x**2 + x + 1

x = np.linspace(0, 10, 100)
y = f(x)
dy_dx = np.gradient(y, x)
print(f"The numerical derivative is: {dy_dx}")