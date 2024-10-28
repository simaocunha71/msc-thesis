
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 10
    elif n == 2:
        return 90
    else:
        # the number of 1-digit numbers starting with 1 is 10,
        # the number of 2-digit numbers starting with 1 is 90
        # the number of 3-digit numbers starting with 1 is 810
        # ...
        # the number of n-digit numbers starting with 1 is
        # (n-1)**n - (n-2)**n + (n-3)**n - ... + 10**(n-1)
        return (n-1)**n - (n-2)**n + (n-3)**n - ... + 10**(n-1)

