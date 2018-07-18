#EXERCISE 12

# Two Different Answers
# 
def firstLast(orignal): 
    """
    1. use append like I did which would work with adding multiple values
    # 2. [orignal[0], orignal[-1]]
    
    :param orignal: List
    :returns: list containing first and last element of list provided
    """   
    return [orignal[0], orignal[-1]]
    

a = [5,10,15,20,25]

print(firstLast(a))