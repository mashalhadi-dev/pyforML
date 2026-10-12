import numpy as np

# Aik NumPy array banate hain
numbers = np.array([10, 20, 30, 40, 50])

# 1. Indexing: Specific element nikalna
print("Pehla element (Index 0):", numbers[0])
print("Teesra element (Index 2):", numbers[2])
print("Aakhri element (-1):", numbers[-1])

# 2. Slicing: Aik hissa nikalna (Pehlay 3 elements)
print("Pehlay 3 elements:", numbers[0:3])

# 3. Step slicing: Aik chorkar aik lena
print("Alternate elements:", numbers[::2])