
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    
    n = int(n)
    s = s.rstrip()
    s = s[:-1]
    b = 0
    p = 0
    if (len(s) == 1):
        return 1
    for i in range(len(s)-2,-1,-1):    
        if (s[i] == 'a'):
            p +=1
            
        
        elif (s[i] == 'o'):
            b +=1
            
        
        else:
            return 0
    return n-b+p