def newton_divided_difference(x, y):
  """
  This function implements Newton's divided difference method for polynomial interpolation.

  Args:
      x: List of x-coordinates of the data points.
      y: List of y-coordinates of the data points.

  Returns:
      A function representing the Newton polynomial.
  """
  n = len(x)
  coeffs = [0] * n
  coeffs[0] = y[0]

  # Calculate divided differences
  for j in range(1, n):
    for i in range(n - 1, j - 1, -1):
      y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j])
    coeffs[j] = y[j]

  # Define the polynomial function
  def P(x_val):
    result = coeffs[0]
    for i in range(1, n):
      term = coeffs[i]
      for j in range(i):
        term *= (x_val - x[j])
      result += term
    return result

  return P

# Example usage:
data_points = [(1, 1), (2, 4), (3, 9), (4, 16)]
x_vals = [point[0] for point in data_points]
y_vals = [point[1] for point in data_points]

newton_poly = newton_divided_difference(x_vals, y_vals)
print(newton_poly(2.5))  # Evaluate at x = 2.5
