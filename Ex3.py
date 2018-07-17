a = [1, 1, 2, 3, 5, 8, 13, 21, 35, 55, 89]
x = []

for values in a:
    if (values < 5):
        x.append(values)
        print(values)

print(x)
