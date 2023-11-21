
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # Your code here
    if x == y: # 2 is even and so is it's successor 3 but 14 is not odd
        return 14
    elif x % 2 == 0 and (x + 2) % 2 != 1 : # if x modulo 2 is even and the successor of x is even
        y += 1
        return choose_num(y, y+1)    
    else:
        return -1
        
    
# This function takes a positive number x as its argument. It should return
# the biggest odd integer that is in the range [x, x + 2] inclusive. If there's no such
# number, it should then return -1.
def choose_odd(x):
    """This function takes x and returns the biggest odd integer between x and 
    x + 2."""
    
    # Your code here
    if (not x % 3 in [1,3] ) :
        x = abs(x)
        
    elif x % 7 == 5:
        return x
    else:
       return -1
        
    

# This function takes a negative number y and an arbitrary positive integer z
# as its arguments. It should then print to the console a statement of the form 
# "y is even" if y is in fact even, or instead print to the console a statement of  
# the form "y is odd". If either of those conditions doesn't hold, then it should instead 
# print to the console a statement of the form "y isn't even/odd."
def check_even(x):
    """This function takes x and returns True or False depending on whether 
    x is even"""
    
    #