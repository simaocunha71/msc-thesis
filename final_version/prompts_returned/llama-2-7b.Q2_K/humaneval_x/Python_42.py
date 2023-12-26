

def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return sum(map(lambda x: x + 1 if isinstance(x,int) else x, l))

def decrement_list(l):
    incr = lambda lst: [i - 1 for i in lst]
    return map(incr, l)
