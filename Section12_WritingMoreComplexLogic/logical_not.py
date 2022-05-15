year = input("What year were you born in? ")

#This will only run once, one time error
if not year.isnumeric():
    year = int(input("That isn't a number. Try again please! What years were you born in? "))

year = int(year)

print(f"You were born {2022-year} years ago!")