def and_tuples(t1, t2):
    """
    Extracts the elementwise and tuples from the given two tuples.
    >>> and_tuples((10, 4, 6, 9), (5, 2, 3, 3))
    (0, 0, 2, 1)
    """
    return tuple(min(i,j) for i,j in zip(t1,t2))