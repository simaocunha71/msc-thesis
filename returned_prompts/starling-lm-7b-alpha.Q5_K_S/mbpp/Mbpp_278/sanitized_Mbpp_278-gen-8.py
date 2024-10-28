def count_first_elements(t):
    """
    Find the number of elements that occurs before the tuple element in the given tuple.
    >>> count_first_elements((1, 5, 7, (4, 6), 10) )
    3
    """
    count = 0
    for i in t:
        if isinstance(i, tuple):
            count += 1
    return count