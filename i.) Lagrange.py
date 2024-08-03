def lagrange_interpolation(x, y):
    def L(k, x_val):
        result = 1
        for i in range(len(x)):
            if i != k:
                result *= (x_val - x[i]) / (x[k] - x[i])
        return result
    
    def P(x_val):
        total = 0
        for k in range(len(x)):
            total += y[k] * L(k, x_val)
        return total
    
    return P

# Example usage:
data_points = [(1, 1), (2, 4), (3, 9), (4, 16)]
x_vals = [point[0] for point in data_points]
y_vals = [point[1] for point in data_points]

lagrange_poly = lagrange_interpolation(x_vals, y_vals)
print(lagrange_poly(2.5))  # Evaluate at x = 2.5
