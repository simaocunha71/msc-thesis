def replace_spaces(string):
    """
    Returns the given string with all spaces replaced by '%20'
    >>> replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'
    True
    """
    return string.replace(' ', '%20')