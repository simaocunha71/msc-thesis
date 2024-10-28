def is_undulating(n):
    """
    Check if the given number is undulating.
    >>> is_undulating(1212121)
    True
    """
    str_n = str(n)
    if len(str_n) < 3:
        return False
    for i in range(1, len(str_n) - 1):
        if str_n[i] == str_n[i-1] and str_n[i] == str_n[i+1]:
            return False
    return True