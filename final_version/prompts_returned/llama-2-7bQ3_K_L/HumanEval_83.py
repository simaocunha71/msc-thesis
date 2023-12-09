
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    n = int(n)
    if not (1 < n<10**9):
        raise ValueError('n must be in range(1,10^9).')

    # Create a dict for counting the number of n-digit positive integers that
    # start or end with 1.
    dct = {}

    # Find the count of numbers that start with 1 and end with a nonzero digit
    if (n > 0):
        for i in range(2, int((n+1)/10)):
            dct[(i, n-int(i))] += 1
    
    # Find the count of numbers that start with a nonzero digit and end with 1
    if (n < 9):
        for i in range(2, int((n+1)/10)):
            dct[(n-int(i), i)] += 1
    
    return sum([dct[k] for k in dct])
