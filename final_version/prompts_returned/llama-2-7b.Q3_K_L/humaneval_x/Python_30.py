

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return list(filter(lambda x: x > 0, l))

def get_negative_numbers(l: list):
    "Return only negative numbers in the list."
    
    return list(filter(lambda x: x < 0, l))

if __name__ == '__main__':
    pass