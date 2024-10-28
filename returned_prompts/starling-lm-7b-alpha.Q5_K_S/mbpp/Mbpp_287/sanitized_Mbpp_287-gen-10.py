def square_Sum(n):
    """
    Take an integer n and return the sum of squares of first n even natural numbers.
    """
    sum = 0
    for i in range(2, n+1, 2):
        sum += i**2
    return sum