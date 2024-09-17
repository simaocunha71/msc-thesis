def frequency(lst, k):
    """
    Count the number of occurrences of a number in a given list.
    >>> frequency([1,2,3], 4)
    0
    """
    return sum(1 for i in lst if i==k)