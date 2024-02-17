number = int(input("Which number is even or odd ?\n"))
if number % 2 != 0:
    print("Number %f is odd" %number)
    print("Number {} is odd".format(number))
else:
    print("Number %f is even" %number)