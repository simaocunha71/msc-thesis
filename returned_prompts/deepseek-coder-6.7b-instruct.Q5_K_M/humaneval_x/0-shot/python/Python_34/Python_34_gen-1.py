

def unique(l: list):
    return sorted(set(l))


print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))



def unique_v2(l: list):
    """Return sorted unique elements in a list
    >>> unique_v2([5, 3, 5, 2, 3, 3, 9, 0, 123])
    0, 2, 3, 5, 9, 123
    """
    return sorted(set(l))


print(unique_v2([5, 3, 5, 2, 3, 3, 9, 0, 123]))



def unique_v3(l: list):
    """Return sorted unique elements in a list
    >>> unique_v3([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return list(set(l))


print(unique_v3([5, 3, 5, 2, 3, 3, 9, 0, 123]))



def unique_v4(l: list):
    """Return sorted unique elements in a list
    >>> unique_v4([5, 3, 5, 2, 3, 3, 9, 0, 123])
    0, 2, 3, 5, 9, 123
    """
    return ", ".join(str(i) for i in sorted(set(l)))


print(unique_v4([5, 3, 5, 2, 3, 3, 9, 0, 123]))



def unique_v5(l: list):
    """Return sorted unique elements in a list
    >>> unique_v5([5, 3, 5, 2, 3, 3, 9, 0, 