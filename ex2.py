number = input("Give me a number so I can see if its even or odd? :")
iseven = int(number) % 2

if (iseven == 0):
    print("The number is even. ")
else:
    print("The number is odd. ")

isfour = int(number) % 4

if (isfour == 0):
    print("The number is divisable by 4. ")
else:
    print("The number is not divisable by 4.")
