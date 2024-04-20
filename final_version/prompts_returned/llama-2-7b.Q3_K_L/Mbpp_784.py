"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""

def mul_even_odd(lst):
    # Your code here
    print("Here")
    if len(lst) == 0:
        return 1
        
    # Get the first two elements of list
    x = lst[0]
    y = lst[1]
    
    # Checks if both elements are zero. If yes, product is 1
    if (x == 0 and y == 0):
        return 1
    
    elif(x % 2 != 0 and x > 0 or y % 2 != 0 and y > 0):
        
        # Checks if both even elements are non-zero. If yes, product is 1
        if (x%2 == 0 and y%2 == 0):
            return 1
            
        else:
            x_product = MulEven(x)
            y_product = MulOdd(y)
            # Checks if even elements of list are odd or even. If yes, product is 1
            elif (x%2 == 0 and y%2 != 0 or x%2!= 0 and y %2 == 0):
                return mul_even_odd(x_product)
            else:
                return 1
    else:
        if (x > 0 and y%2 != 0):
            # Checks if even elements of list are odd or even. If yes, product is x*y+1.
            return x * MulOdd(y) + 1
        else:
            # Checks if even elements of list are odd or even. If yes, product is x*y+1.
            return x * MulEven(y) + 1
    
    return mul_even_odd()