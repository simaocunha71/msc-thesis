
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    if n % 2 == 0 or n < 2:  # base case
        return y
        
    elif (n+1)/2 == int(n/2):
        x_or_y(int((n-1)/2), x, y)
    
    else:
        x_or_y(int((n-1)/2), x, y)
    return y  # base case
