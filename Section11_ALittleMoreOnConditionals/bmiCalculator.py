height = float(input("enter your height in meters: ")) 
weight = int(input("enter your weight in kg: "))

bmi = (weight / (height**2))

if bmi >= 39.9:
    print(f"Your BMI of {bmi} makes you Morbidly Obese")
elif bmi >= 35.0:
    print(f"Your BMI of {bmi} makes you Severely Obese")
elif bmi >= 30.0:
    print(f"Your BMI of {bmi} makes you Moderately Obese")
elif bmi >= 25:
    print(f"Your BMI of {bmi} makes you Overweight")
elif bmi >= 18.5:
    print(f"Your BMI of {bmi} makes you Normal")
elif bmi >= 16:
    print(f"Your BMI of {bmi} makes you Underweight")
else:
    print(f"Your BMI of {bmi} makes you Severely Underweight")
