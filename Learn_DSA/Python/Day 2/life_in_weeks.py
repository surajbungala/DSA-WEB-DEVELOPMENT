# user input current age

current_age = int(input("Enter your current age : "))

# left days weeks months if user live until 90 years

remaining_age = 90 - current_age

# how many days left

days = remaining_age * 365

# how many weeks left

weeks = remaining_age * 52

# how many months left

months = remaining_age * 12

# f"String" print

print(f"You have {days} days, {weeks} weeks and {months} months left")



 