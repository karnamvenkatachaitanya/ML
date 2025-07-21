# Step 2: Compute the y-intercept mathematically
# c = y - mx i.e., c = ȳ - m * x̄
# Step 3: Substitute the values in the final equation.
# Source Code
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
y = np.array([1.2, 1.8, 2.6, 3.2, 3.8])
m = np.cov(x, y, bias=True)[0, 1] / np.var(x)
b = np.mean(y) - m * np.mean(x)
y_pred = m * x + b
mse = np.mean((y - y_pred) ** 2)
rmse = np.sqrt(mse)
plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, y_pred, color='red', label='Regression line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
print(f"Slope (m): {m:.4f}")
print(f"Intercept (b): {b:.4f}")
print(f"Mean squared error (MSE): {mse:.4f}")
print(f"Root mean squared error (RMSE): {rmse:.4f}")
