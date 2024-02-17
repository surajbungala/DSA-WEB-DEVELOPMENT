# user input height for ride
print("Welcome to the rollercoaster ")
user_height = int(input("Please enter your height for ride : "))
bill = 0
# condition statement

if(user_height > 120):
    print("You can ride the rollercoaster")
    # how much money rollercoaster ride 
    age = int(input("What is your age : "))
    if age <= 12:
        bill = 12
        print("Child tickets are $12")
    elif age <= 18:
        bill = 20
        print("Youth tickets are $20")
    else:
        bill = 30
        print("Adult tickets are $30")   
        
    # this code is for photos 
    
    photos_cost = input("Do you want take photos ? Y or N : ")
    if photos_cost == "Y":
        bill += 3
        
    print(f"Your final bill is : ${bill}")
else:
    print("Sorry, You have to grow taller before you can ride")