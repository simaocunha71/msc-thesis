import sys
def tuple_size(t):
    """
    Returns the size in bytes of the given tuple.
    >>> tuple_size(("A", 1, "B", 2, "C", 3) )
    38
    """
    return sys.getsizeof(t)