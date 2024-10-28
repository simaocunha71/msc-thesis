def empty_list(n):
    """
    >>> empty_list(5)
    [{}, {}, {}, {}, {}]
    """
    return [{} for _ in range(n)]