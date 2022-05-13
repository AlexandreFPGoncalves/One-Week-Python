# f strings will read and evaluate and code between {} 
# the result will be turned into a string and inserted into the overall string

age_in_days = input("How old are you? (in days (years*365))")
print(f"You are {float(age_in_days) / 365} old!")