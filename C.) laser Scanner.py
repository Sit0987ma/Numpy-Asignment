import numpy as np

# Data points from the table
x_points = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
y_points = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

# Value at which we want to interpolate
x_val = 4.0

# Function to perform linear spline interpolation
def linear_interpolation(x_points, y_points, x_val):
    # Find the interval in which x_val lies
    for i in range(len(x_points) - 1):
        if x_points[i] <= x_val <= x_points[i + 1]:
            x0, x1 = x_points[i], x_points[i + 1]
            y0, y1 = y_points[i], y_points[i + 1]
            break
    # Linear interpolation formula
    y_val = y0 + (y1 - y0) * (x_val - x0) / (x1 - x0)
    return y_val

# Interpolated value of y at x_val
y_val = linear_interpolation(x_points, y_points, x_val)

print(f"The interpolated value of y at x = {x_val} is {y_val}")
