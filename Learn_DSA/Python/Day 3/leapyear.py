year = int(input("Which year you want to check ? "))

if year % 4 == 0: #if year divisble by 4 then this year is leap year
    if year % 100 == 0:   #if year divisble by 100 then this year is not leap year
        if year % 400 == 0: #if year divisble by 400 then this year is leap year
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")