# Given a string, create a PALINDRONE for that word
str = 'Are we not drawn onward, we few, drawn onward to new era?'

def reverse(str):
    # Given a string, reverse it
    return "".join(reversed(str))


print("The following is a palindrone : ", str)
print("After reversing it, it it still a palindron : ",reverse(str.lower()))