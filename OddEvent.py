number = input("Enter a number as you want: ")
number = int(number)
check = int(input("Enter a number to divide: "))

if number % 2 == 0 and number % 4 == 0:
    print(number," is a multiple of 4")
elif number % 2 == 0:
    print (number, " is even number")
else:
    print(number," is odd number")

if number != 0:
    if check % number == 0:
        print(check, " divides evenly into ", number)
    else:
        print(check, "do not divide evenly into ", number)
