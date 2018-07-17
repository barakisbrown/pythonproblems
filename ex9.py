import random

# Simple program to guess a number between 1 and 9

number = random.randint(1,9)
count = 1

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Oops. Not an valid input. It has between 0 and 9. Try again")
            continue
        else:
            return userInput




while True:    
    guess = inputNumber("Guess a number between 1 and 9, 0 to exit  => ")
    if (guess >= 0 and guess <= 9):
        # Input is correct
        if (guess == 0):
            print("Exiting Program")
            break
        else:
            if (guess < number):
                print("Too Low")
                count += 1
            elif (guess > number):
                print("Too high")
                count += 1
            else:
                str = "Correct. It took you only {} guesses".format(count)
                print(str)
                break