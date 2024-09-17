def all_unique(lst):
    """
    >>> all_unique([1,2,3])
    True
    >>> all_unique([1,1,2,3])
    False
    >>> all_unique([1,2,3,3])
    False
    """
    return len(lst) == len(set(lst))