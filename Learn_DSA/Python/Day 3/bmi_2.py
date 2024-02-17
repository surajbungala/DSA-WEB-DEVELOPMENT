# welcome text for bmi

print("Welcome to the BMI calculator:")

# user input height and weight

height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

# bmi calculation

bmi = round(weight / height ** 2)

# check condition for bmi

if bmi < 18.5:
    print(f"Your bmi is {bmi}, You are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, You have a normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, You are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, You are obese")
else:
    print(f"Your bmi is {bmi}, You are clinically obese")
