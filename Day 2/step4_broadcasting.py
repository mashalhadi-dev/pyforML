import numpy as np

# 1. 3 students ke 3 subjects ke marks (3 rows, 3 columns ka matrix)
marks = np.array([
    [50, 60, 70],
    [80, 90, 85],
    [65, 75, 55]
])

# 2. Har subject ka bonus marks (3 numbers ki choti array)
bonus = np.array([5, 10, 15])

# 3. Broadcasting ka jaadu: Choti array khud-ba-khud har row par apply ho jaye gi!
updated_marks = marks + bonus

print("Original Marks:\n", marks)
print("\nBonus Marks add hone ke baad (Broadcasting ke zariye):\n", updated_marks)


# 🎁 Analogy: Ek Barray Box mein Chotay Tohfay Fit Karna
# Imagine karo:

# Tumhare paas aik bara box (2D Table / Matrix) hai jisme 3 rows aur 3 columns hain (misal ke tor par 3 students aur unke 3 subjects ke marks).

# Aur aik chota packet (1D Array) hai jisme 3 numbers hain (har subject ka bonus).

# Asal zindagi mein agar tum alag alag size ki cheezon ko jorne lago ge toh error aa jayega. Lekin NumPy ka Broadcasting jaadu kya karta hai? Woh us chote packet ko khud-ba-khud "stretch" (khinch kar bara) kar deta hai taake woh baray box ke sath fit ho jaye aur calculations ho sakein!

# Isi automatic khinchne aur fit hone ke amal ko Broadcasting kehte hain.