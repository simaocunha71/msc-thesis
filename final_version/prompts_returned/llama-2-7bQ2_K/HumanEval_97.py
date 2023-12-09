
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    
    a = int(a)
    b = int(b)
    
    if len(str(a)) > 1 and len(str(b)) > 1:   # if both numbers length is more than one then else condition will be executed
        print('else')
        
        return a*b

    elif (len(str(b))) < 2 and (len(str(a))) < 2:   # if the second number is a string that's length is less than two, then the else part of this condition will be executed
        print('else')
        
        return a*b

    elif not str(a).isdigit() and (len(str(b)) >= 2):   # if the first number is a string that's length is less than two, then the else part of this condition will be executed
        print('else')
        
        return a*b        
    else:
        print('else')
        
        return a*b        
     
 