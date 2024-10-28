

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


print(strlen('abc'))
print(strlen(''))

# or

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


print(strlen('abc'))
print(strlen(''))

# or

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    count = 0
    while string[count:]:
        count += 1
    return count


print(strlen('abc'))
print(strlen(''))

# or

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return sum(1 for _ in string)


print(strlen('abc'))
print(strlen(''))

# or

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    try:
        return 1 + strlen(string[1:])
    except IndexError:
        return 0


print(strlen('abc'))
print(strlen(''))

# or

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if not string:
        return 0
    else:
        return 1 + strlen(string[1:])


print(strlen('abc'))
print