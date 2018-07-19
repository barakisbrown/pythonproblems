def inputNumber(message):
    """
    Asks the user for a enter a number based on the message being asked
    :param message: What message is asked of the user.
    :returns: the number the user entered
    """
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Oops. Not an valid input. Must be a number > 1")
            continue
        else:
            return userInput

def fibonacci(numSeq):
    """
    returns a fabonacci sequeunce. A fib sequence ex: [1,1,2,3,5,8,...]
    Please note that a seq of 1 is [1]
    :param numSeq: The number of finonacci sequence
    :returns: List of fib sequences
    """
    if (numSeq == 1):
        return [1]
    else:
        l = [1]
        a,b = 1,1
        for i in range(numSeq - 1):
            a,b = b,a+b
            l.append(a)
        return l

seq = inputNumber("How many fabonacci seq u want done :> ")
print(fibonacci(seq))
