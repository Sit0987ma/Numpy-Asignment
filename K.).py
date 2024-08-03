import numpy as np


def gradient_descent(
    learning_rate=0.1, initial_guess=(0, 0), max_iterations=1000, tolerance=1e-6
):
    x, y = initial_guess

    def f(x, y):
        return x**2 + y**2 - x * y + x - y + 1

    def gradient(x, y):
        df_dx = 2 * x - y + 1  # Partial derivative with respect to x
        df_dy = 2 * y - x - 1  # Partial derivative with respect to y
        return np.array([df_dx, df_dy])

    for i in range(max_iterations):
        grad = gradient(x, y)
        x_new = x - learning_rate * grad[0]
        y_new = y - learning_rate * grad[1]

        # Check for convergence
        if np.linalg.norm([x_new - x, y_new - y]) < tolerance:
            break

        x, y = x_new, y_new

    return (x, y), f(x, y)


# Example usage
optimal_point, optimal_value = gradient_descent()
print("Optimal point:", optimal_point)
print("Optimal value:", optimal_value)
