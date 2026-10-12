# 🍽️ Analogy: Aik aik plate dhona vs Dishwasher Machine
# Standard Python Loops (Aik aik plate dhona):
# Agar aapke paas 10 plates hain, aur aap aik-aik plate utha kar nal ke niche dho rahe ho, toh bohot time lagega. Python ka for loop bhi yahi karta hai—har number ko aik-aik karke uthata hai aur process karta hai.

# NumPy Vectorization (Dishwasher Machine):
# NumPy kya karta hai ke saari 10 plates ko aik sath machine mein dalta hai aur aik hi button dabata hai—saari plates aik hi second mein saaf ho jati hain! Isko Vectorization kehte hain jisme koi loop nahi chalana parta, balkay computer ka hardware direct poori array par aik sath calculation kar deta hai.
import numpy as np

# Students ke pehle ke marks ki array
marks = np.array([50, 60, 70, 80])

# Har student ko 10 grace marks dene hain (Bina kisi loop ke!)
updated_marks = marks + 10

print("Purane Marks:", marks)
print("Grace Marks ke baad Updated Marks:", updated_marks)

# Aik aur misal: Prices par 20% discount lagana
prices = np.array([100, 200, 500])
discounted_prices = prices * 0.80  # 20% minus karne ke baad bacha hua price
print("Discounted Prices:", discounted_prices)