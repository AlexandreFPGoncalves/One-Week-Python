firstName = input("What is your first name?")
lastName = input("What is your first name?")
nameLength = (len(firstName) + len(lastName))

if nameLength == 12:
    print(f"{firstName} {lastName} is exactly average American name")
elif nameLength < 12:
    print(f"{firstName} {lastName} is shorter than average American name")
else:
    print(f"{firstName} {lastName} is longer than the average American name")