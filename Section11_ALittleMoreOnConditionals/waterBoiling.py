unit = input("What unit are you using? ").lower()
temp = int(input("What temperature is the water? "))
#f - 212, c - 100, k - 373

if unit == "f":
    if temp > 212:
        print("The Water is Boiling!")
    else: 
        print("The Water is NOT Boiling!")
elif unit == "c":
    if temp > 100:
        print("The Water is Boiling!")
    else: 
        print("The Water is NOT Boiling!")
elif unit == "k": 
    if temp > 373:
        print("The Water is Boiling!")
    else: 
        print("The Water is NOT Boiling!")