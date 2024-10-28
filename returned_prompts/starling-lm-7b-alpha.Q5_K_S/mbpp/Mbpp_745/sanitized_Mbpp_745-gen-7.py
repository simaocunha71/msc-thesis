def divisible_by_digits(startnum, endnum):
    """
    >>> divisible_by_digits(1,22)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    """
    # your code goes here
    result = []
    for i in range(startnum, endnum + 1):
        if all(i % j == 0 for j in str(i)):
            result.append(i)
    return result