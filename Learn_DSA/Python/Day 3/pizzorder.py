# welcome note 
print("Welcome to the Pizza Deliveries !")

# inputs
size = input("What size you want ? S, M or L ? ")

add_pepperoni = input("Do you want add pepperoni ? Y or N ? ")
extra_cheese = input("Do you want extra cheese ? Y or N ? ")


if size == "S":
    bill = 15
    print("Small Pizza Price : $15")

elif size == "M":
    bill = 20
    print("Medium Pizza Price : $20")
    
else:
    bill = 25
    print("Large Pizza Price : $15")

# Add pepperoni code

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Add extra cheese code
       
if extra_cheese == "Y":
    bill += 1
    
print(f"Your Final bill is $ {bill}")   