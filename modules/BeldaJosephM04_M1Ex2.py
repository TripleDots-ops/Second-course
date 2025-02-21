"""

Author:  Joseph Belda
Date written: 2/10/25
Assignment:   Assignment Part II
Short Desc:   This program will go through the list of items and sort the top three highest ones
and print them out


"""

# Sample data
shop_items = {'Apple': 0.50, 'Banana': 0.20, 'Mango': 0.99, 'Coconut': 2.99, 'Pineapple': 3.99}

# Sort the dictionary by price in descending order and get the top three items
top_three_items = sorted(shop_items.items(), key=lambda item: item[1], reverse=True)[:3]

# Output the top three items with their prices
for item in top_three_items:
    print(f"{item[0]} {item[1]}")
