def average_tuple(t):
    """
    >>> average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))
    [30.5, 34.25, 27.0, 23.25]
    """
    result = []
    for tup in t:
        result.append(sum(tup)/len(tup))
    return result