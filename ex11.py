def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Oops. Not an valid input. Must be a number > 1")
            continue
        else:
            return userInput

def isPrime(number):
    pass

prime = inputNumber("Enter a number ")    