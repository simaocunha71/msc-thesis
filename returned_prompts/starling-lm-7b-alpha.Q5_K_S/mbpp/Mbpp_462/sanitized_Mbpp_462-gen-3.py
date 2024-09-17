def combinations_list(lst):
    """
    :type lst: List[str]
    :rtype: List[List[str]]
    """
    res = [[]]
    for i in lst:
        res += [j + [i] for j in res]
    return res