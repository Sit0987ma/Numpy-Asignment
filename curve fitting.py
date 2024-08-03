import matplotlib.pyplot as plt
import numpy  as np
from scipy.optimize import curve_fit


# Define the model function
def model(x, a, b):
    return a * np.exp(b * x)


# Generate some data
xdata = np.linspace(0, 4, 50)
ydata = model(xdata, 2.5, 1.3) + np.random.normal(size=len(xdata))

# Fit the model to the data
popt, pcov = curve_fit(model, xdata, ydata)
print(popt)

# Plot the data and the fit
plt.scatter(xdata, ydata, label="Data")
plt.plot(xdata, model(xdata, *popt), label="Fit", color="red")
plt.legend()
plt.show()
