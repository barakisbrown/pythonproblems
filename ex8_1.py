# Exercise 8 Refactored by Matthew Brown
# Rules
#  1. Rock beats scissors
#  2. Scissors beats paper
#  3. Paper beats rock
# -------------------------
# Player 1 will be controlled by the player while player2 will be the pc.
import random

def determine_winner(player1, player2):
    #PLAYER1
    if (player1 == 1 and player2 == 3):
        print("Player 1 Wins")
    elif (player1 == 3 and player2 == 2):
        print("Player 1 Wins")
    elif (player1  == 2 and player2 == 1):
        print("Player 1 Wins")
    elif (player1 == player2):
        print("Whoops. Both of you have the same thing. That is a draw. try again.")
    else:
        # Player 2
        if (player2 == 1 and player1 == 3):
            print("Player 2 Won")
        elif (player2 == 3 and player1 == 2):
            print("Playrr 2 Won")
        elif (player2 == 2 and player1 == 1):
            print("Player 2 Wins")


movesAllowed = ['Rock','Paper','Scissors']
playerChoices = [1,2,3,4]

while True:
    player2 = random.randint(1,3)
    player1 = int(input("Pick between Rock/Paper/Scissors(1/2/3, 4 to quit) :"))

    if (player1 in playerChoices):
        if (player1 == 4):
            break
        determine_winner(player1, player2)
    else:
        print("Please pick between 1 through 3")