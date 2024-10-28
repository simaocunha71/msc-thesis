def sort_sublists(lists):
    """
    Sort each sublist of strings in a given list of lists.

    >>> sort_sublists((["green", "orange"], ["black", "white"], ["white", "black", "orange"]))
    [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    """
    return [sorted(sublist) for sublist in lists]