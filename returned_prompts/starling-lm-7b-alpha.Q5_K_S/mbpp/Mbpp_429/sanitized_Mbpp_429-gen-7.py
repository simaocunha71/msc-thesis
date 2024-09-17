def and_tuples(t1, t2):
    """
    >>> and_tuples((10, 4, 6, 9), (5, 2, 3, 3))
    (0, 0, 2, 1)
    """
    # initialize result
    result = ()

    # get length of tuples
    n = len(t1)

    # traverse tuples and find elementwise
    for i in range(n):
        result += (t1[i] & t2[i],)

    # return result
    return result