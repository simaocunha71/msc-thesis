def unique_sublists(lst):
    """
    Returns a dictionary with every sublist converted to a tuple and the value of such tuple is the number of its occurencies in the original list.
    >>> unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])
    {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    """
    res = {}
    for item in lst:
        if isinstance(item, list):
            key = tuple(item)
            res[key] = res.get(key, 0) + 1
    return res