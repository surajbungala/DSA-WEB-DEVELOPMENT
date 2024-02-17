# Welcome to the bill split calculator

print("Welcome to the tip calculator")

# user input total bill

bill= float(input("What was the total bill ? $ "))

# tip percent included in total amount

tip = int(input("What percentage tip would you like to give ? 10, 12, or 15 ? "))
tip_percent = tip / 100

# counting of people for spliting

people_count = int(input("How many people to split the bill ? "))

# each person should pay

tip_percent_amount = bill * tip_percent

total_amount = bill + tip_percent_amount

bill_per_person = total_amount / people_count

Final_Amount = round(bill_per_person, 2)

print(f"Each person should pay $ {Final_Amount}")