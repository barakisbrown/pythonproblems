num = int(input("Give me a number please? :"))

def divisor(num):
    arr = []

    for x in range(2,num + 1):
        if (num % x == 0):
            arr.append(x)
    print(arr)

divisor(num)    