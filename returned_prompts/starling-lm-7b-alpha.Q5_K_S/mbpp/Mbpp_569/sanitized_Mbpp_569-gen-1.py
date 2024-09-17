def sort_sublists(lst):
    """
    >>> sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])
    [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    """
    for i in range(len(lst)):
        lst[i].sort()
    return lst