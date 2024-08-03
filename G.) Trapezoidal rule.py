import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(f, a, b, n):
    """
    Calculate the integral of f from a to b using the trapezoidal rule.
    
    Parameters:
    f : function - The function to integrate.
    a : float - The lower limit of integration.
    b : float - The upper limit of integration.
    n : int - The number of trapezoids.
    
    Returns:
    float - The approximate value of the integral.
    """
    h = (b - a) / n  # Width of each trapezoid
    integral = 0.5 * (f(a) + f(b))  # Start with the first and last terms

    for i in range(1, n):
        integral += f(a + i * h)  # Add the middle terms

    integral *= h  # Multiply by the width of the trapezoids
    return integral

# Example function to integrate
def f(x):
    return x**2  # Example: f(x) = x^2

# Integration limits
a = 0  # Lower limit
b = 1  # Upper limit
n = 10  # Number of trapezoids

# Calculate the integral
result = trapezoidal_rule(f, a, b, n)
print(f"Approximate value of the integral from {a} to {b} is: {result}")

# Visualization
x = np.linspace(a, b, 100)
y = f(x)

plt.plot(x, y, 'b', label='f(x) = x^2')
plt.fill_between(x, y, color='lightblue', alpha=0.5, label='Area under curve')

# Draw trapezoids
for i in range(n):
    x0 = a + i * (b - a) / n
    x1 = a + (i + 1) * (b - a) / n
    plt.fill_between([x0, x0, x1, x1], [0, f(x0), f(x1), 0], color='orange', alpha=0.5)

plt.title('Trapezoidal Rule Integration')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()
