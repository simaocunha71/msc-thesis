def extract_values(s):
    """
    Extract values between quotation marks from a string.

    Parameters
    ----------
    s : str
        The string to extract values from.

    Returns
    -------
    list
        A list of values between quotation marks.

    Examples
    --------
    >>> extract_values('"Python", "PHP", "Java"')
    ['Python', 'PHP', 'Java']
    """
    values = []
    start = False
    end = False
    for c in s:
        if c == '"':
            start = not start
        elif start:
            values.append(c)
        elif end:
            if c != '"':
                values.append(c)
            end = False
    return values