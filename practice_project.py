# Step 1: Raw data define karna
# raw_lines = ["  ali, 25, lahore", "sara, 30, karachi"]

# for line in raw_lines:
#     print("Asli line:", line)

# raw_lines = ["  ali, 25, lahore", "sara, 30, karachi"]

# for line in raw_lines:
#     # Comma par line ko tod kar tukre (parts) banana
#     parts = line.split(',')
#     print("Tutay huay tukre:", parts)


raw_lines = ["  ali, 25, lahore", "sara, 30, karachi"]
for line in raw_lines:
    # Comma par line ko tod kar tukre (parts) banana
    parts = line.split(',')
    print("Tutay huay tukre:", parts)
cleaned_records = [
   {"name": parts[0].strip().title(),
    "age": int(parts[1].strip()),
    "city": parts[2].strip().capitalize()
   }
   for line in raw_lines
   if (parts := line.split(','))and len(parts) ==3

]
print('saaf record:', cleaned_records)