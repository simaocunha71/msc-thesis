def min_of_three(a, b, c):
    """
    Finds the minimum of three numbers

    Parameters
    ----------
    a : int
        The first number
    b : int
        The second number
    c : int
        The third number

    Returns
    -------
    int
        The minimum of the three numbers
    """
    return min(a,b,c)

# Test the function
assert min_of_three(10,20,0)==0

# Test the function with some more complex inputs
assert min_of_three(10,20,5)==5
assert min_of_three(10,5,20)==5
assert min_of_three(10,100,5)==5

# Test the function with some negative numbers
assert min_of_three(10,-20,5)==-20
assert min_of_three(-10,20,-5)==-10
assert min_of_three(-10,-5,20)==-10

# Test the function with some zeroes
assert min_of_three(0,20,10)==0
assert min_of_three(0,0,10)==0
assert min_of_three(0,10,0)==0

# Test the function with some very large numbers
assert min_of_three(10**10,20,5)==5
assert min_of_three(10**10,5,20)==5
assert min_of_three(10**10,100,5)==5

# Test the function with some very small numbers
assert min_of_three(1e-10,20,5)==1e-10
assert min_of_three(1e-10,5,20)==1e-10
assert min_of_three(1e-10,100,5)==1e-10

# Test the function with some complex inputs
assert min_of_three(10**10,20**10,5)==5