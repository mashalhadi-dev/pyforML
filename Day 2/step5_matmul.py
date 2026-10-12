import numpy as np

# 1. Inputs (Data features)
inputs = np.array([2.0, 3.0])

# 2. Weights (Neural Network ke wazn / parameters)
weights = np.array([
    [0.5, 0.1],
    [0.2, 0.8]
])

# 3. Matrix Multiplication (AI Layer Calculation)
# Hum yahan '@' symbol use karte hain jo NumPy mein matrix multiplication ke liye hota hai
output = inputs @ weights

print("Inputs:", inputs)
print("Weights Matrix:\n", weights)
print("Neural Network Output (Matrix Multiplication ke baad):", output)