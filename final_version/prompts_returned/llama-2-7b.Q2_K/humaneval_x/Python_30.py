

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return filter(lambda x: x > 0, l)

def get_nonzero(l):
    """Return only non-zero values in the list.
    >>> print(get_nonzero([1, 0, -4]))
    1
    >>> print(get_nonzero([2, -3, -10, 3])).split()[:6]
    [2, -3, -10, 3, -25, 187.5]
    """
    return filter(lambda x: x != 0, l)

def get_unique(l):
    """Return only unique values in the list.
    >>> print(get_unique([1, 0, -4]))
    1
    >>> print(get_unique([2, -3, -10, 3])).split()[:6]
    [2, -3, -10, 3, -25, 187.5]
    """
    u = set(l)
    return filter(lambda x: x not in u, l)

def get_sorted(l):
    if type(l[0]) is int:
        pass
    else:
        l.sort()
    print(get_sorted([1, 2]))
