import numpy as np


quantities_sold = np.array([120, 45, 300, 85])
unit_prices = np.array([15.5, 50.0, 5.0, 120.0])


print ("Quantities Sold:", quantities_sold)
print ("Unit Prices:", unit_prices)


product_revenue = quantities_sold * unit_prices
print("Product-wise Revenue:", product_revenue)


total_store_revenue = np.sum(product_revenue)
print(f"Total Store Revenue: ${total_store_revenue:.2f}")

shipping_fee = 2.0
net_prices = unit_prices + shipping_fee
print("Net Prices (including shipping):", net_prices)


city_multipliers = np.array([
    [1.0, 1.1],
    [1.2, 1.0],
    [0.9, 1.1],
    [1.1, 1.2]
])

regional_sales = quantities_sold @ city_multipliers
print("regional sales breakdown (Lahore vs Karachi):", regional_sales)
print("\n-- Project Executed Successfully --")