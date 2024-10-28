def and_tuples(t1, t2):
    """
    Extract the elementwise and tuples from the given two tuples.
    >>> and_tuples((10, 4, 6, 9), (5, 2, 3, 3)) == (0, 0, 2, 1)
    True
    """
    l1 = len(t1)
    l2 = len(t2)
    if l1 != l2:
        raise ValueError("The two tuples have different length.")
    result = [0] * l1
    for i in range(l1):
        result[i] = t1[i] & t2[i]
    return tuple(result)