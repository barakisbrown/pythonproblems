# Determine Prime Number
# There is a more elegant way of doing it but this version is simply by getting it divisors
# because if it has more than 1 divisor than it is not prime since prime has to have only 1
# which itself(I am ignoring 1 since it is a divisor in itself)
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
    if (number == 1):
        return True
    else:
        a = []
        for x in range(2, number + 1):
            if (number % x == 0):
                a.append(x)
        # If the length is greater than 0 then it is not prime
        return len(a) == 1

prime = inputNumber("Enter a number to see if it prime or not: ")
if (isPrime(prime)):
    print("The number " + str(prime) + " is a prime number")
else:
    print("The number " + str(prime) + " is not a prime number")    