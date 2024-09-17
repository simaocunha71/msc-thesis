def add_string(l, s):
    """
    Apply a given format string to all elements in a list.

    Parameters
    ----------
    l : list
        The list of elements.
    s : str
        The format string.

    Returns
    -------
    list
        The list of formatted strings.
    """
    return [s.format(i) for i in l]