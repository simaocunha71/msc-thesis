def sort_sublists(l):
    """
    >>> sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))
    [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    >>> sort_sublists((["white", "black"], ["green", "orange"], ["white", "black", "orange"]))
    [['black', 'green', 'orange'], ['white', 'white', 'black', 'orange']]
    """
    if not l:
        return []
    if type(l[0]) == str:
        return [sorted(l)]
    else:
        for i in range(len(l)):
            l[i] = sort_sublists(l[i])
        return sorted(l)