# Exercise 8 by Matthew Brown
# Rules
#  1. Rock beats scissors
#  2. Scissors beats paper
#  3. Paper beats rock
# -------------------------
# Player 1 will be controlled by the player while player2 will be the pc.
import random

movesAllowed = ['Rock','Paper','Scissors']
playerChoices = [1,2,3]

while True:
    player1 = int(input("Pick between Rock/Paper/Scissors(1/2/3) :"))
    if (player1 in playerChoices):
        # Determine Player2 Move
        player2 = random.randint(1,3)
        # Determine who wins
        if (player1 == 1 and player2 == 3):
            print("Player 1 Won!!")
            break
        elif (player1 == 3 and player2 == 2):
            print("Player 1 Won!!")
            break
        elif (player1 == 2 and player2 == 1):
            print("Player 1 Won!!")
            break
        elif (player2 == 3 and player1 == 2):
            print("Player 2 Won!!")
            break
        elif (player2 == 1 and player1 == 3):
            print("Player 2 Won!!")
            break
        elif (player2 == 2 and player1 == 1):
            print("Player 2 Won!!")
            break            
        else:
            print("Your tied .. try again")
            continue
    else:
        print("Your choice has to be between 1 and 3")
