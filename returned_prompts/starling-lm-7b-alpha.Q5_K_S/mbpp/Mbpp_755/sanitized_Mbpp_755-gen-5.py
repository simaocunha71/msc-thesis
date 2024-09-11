def second_smallest(lst):
    """
    Return the second smallest number in a list.

    Parameters
    ----------
    lst : list
        A list of numbers.

    Returns
    -------
    smallest : int
        The second smallest number in the list.
    """
    lst.sort()
    return lst[1]