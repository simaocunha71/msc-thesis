def is_upper(string):
    """
    Return true if all characters in the string are uppercase
    """
    for c in string:
        if not c.isupper():
            return False
    return True