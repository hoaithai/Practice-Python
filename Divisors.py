#Create a program that asks the user for a number and then prints out a list of all the divisors of that number

number = int(input("Enter a number: "))
divisors = []
for i in range(1, number):
    if number % i == 0:
        divisors.append(i)

print(divisors)