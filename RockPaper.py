#Exercise 8: Rock Paper Scissors
#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out
# a message of congratulations to the winner, and ask if the players want to start a new game)

point_pl1 = 0
point_pl2 = 0

while True:
    number_round = int(input("Enter a number round: "))
    while (number_round >0 ):
        player1 = input("Player1, Enter your choose: ")
        player2 = input("Player2, Enter your choose: ")

        if player1 == "R" and player2 == "S":
            point_pl1 += 1
        elif player1 == "S" and player2 == "P":
            point_pl1 += 1
        elif player1 == "P" and player2 == "R":
            point_pl1 += 1
        elif player2 == "R" and player1 == "S":
            point_pl2 += 1
        elif player2 == "S" and player1 == "P":
            point_pl2 += 1
        elif player2 == "P" and player1 == "R":
            point_pl2 += 1

        number_round -= 1
    print("=============================")
    print("Score of player1: ", point_pl1)
    print("Score of player2: ", point_pl2)
    if point_pl1 > point_pl2:
        print("Congratulation player1, you win")
    elif point_pl1 == point_pl2:
        print("You draw")
    else:
        print("Congratulation player2, you win")

    print("=============================")
    print("Do you want start a new game? ")
    print('Type "Y" if you want continues or "N" if not ')
    choose = input("You choose(Y/N): ")
    if choose == 'Y':
        continue
    else:
        break