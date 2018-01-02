#Exercise 9: Guessing game one
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.

import random

while True:
    print("You can guess a number will apear in the range 1-9")
    n_guess = int(input("Enter a number: "))

    number = random.randint(1,9)
    print ("Number is: ", number)
    count_correct = 0
    if n_guess == number:
        count_correct += 1
        print("Ping pong! Exactly")
    elif n_guess > number:
        print("You guessed too high")
    else:
        print("You guessed too low")

    print("You guess correctly ", count_correct, "tines")
    c_exit = input('Type "exit" if you want to quit')
    if c_exit == "exit":
        break
    else:
        continue
