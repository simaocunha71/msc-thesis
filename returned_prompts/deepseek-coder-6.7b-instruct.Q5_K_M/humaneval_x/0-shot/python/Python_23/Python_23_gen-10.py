

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    count = 0
    for _ in string:
        count += 1
    return count


if __name__ == "__main__":
    import doctest
    doctest.testmod()


