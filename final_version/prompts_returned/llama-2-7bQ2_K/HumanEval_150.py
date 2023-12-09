
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    # Write your code here...
    if n==0 or n==1:
        return 1
    elif (not isprime(n)):
        return y
    else:
        return x
x_or_y(3,7,2)