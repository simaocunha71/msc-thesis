def check_distinct(t):
    '''
    >>> check_distinct((1, 4, 5, 6, 1, 4)) == False
    True
    >>> check_distinct((1, 2, 3, 4, 5)) == True
    True
    '''
    return len(t) == len(set(t))