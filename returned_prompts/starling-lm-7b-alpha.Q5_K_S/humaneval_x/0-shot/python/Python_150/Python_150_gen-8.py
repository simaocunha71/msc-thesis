    from sympy import isprime

    if isprime(n):
        return x
    else:
        return y




def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    if isprime(n):
        return x
    else:
        return y


# Test
print(x_or_y(7, 34, 12) == 34)
print(x_or_y(15, 8, 5) == 5)





def x_or_y(n, x, y):
    from sympy import isprime

    if isprime(n):
        return x
    else:
        return y

    # Test
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5


# Run tests
test_it()




def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """

    from sympy import isprime

    if isprime(n):
        return x
    else:
        return y

    # Test
    assert x_or_y(7, 34, 12) == 34
    assert x_or_y(15, 8, 5) == 5


# Run tests
test_it()




def x_