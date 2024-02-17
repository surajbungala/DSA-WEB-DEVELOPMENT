# user input height and weight

height = float(input("Enter your height in m : "))
weight = int(input("Enter your weight in kg : "))

# bmi = weight / height * height 

bmi = weight / height ** 2

# print bmi calculation

print("User bmi calculation : " , bmi)