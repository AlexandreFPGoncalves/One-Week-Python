print("""
WELCOME TO OUR STORE!
*****************************
""")

purchasing_item = input("What item are you purchasing?")
purchasing_price = input(f"What is the price of {purchasing_item}?")
purchasing_amount = input(f"How many {purchasing_item} are you buying?")

print(f"Added {purchasing_amount} {purchasing_item}(s) to shopping cart")
print(f"Subtotal: {float(purchasing_price) * int(purchasing_amount)}€")