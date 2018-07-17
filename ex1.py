name = input("What is your name? ")
age = input("What is your age? ")
copies = input("How many copies would you like? ")
year100 = (100 - int(age)) + 2017
display = "{} will be 100 in the year {}".format(name, year100)
print(display)

for cp in range(1, int(copies)):
    print(display + '\n')
