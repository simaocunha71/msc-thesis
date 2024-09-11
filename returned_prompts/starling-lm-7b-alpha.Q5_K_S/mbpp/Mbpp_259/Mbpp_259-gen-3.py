from itertools import chain, starmap
from operator import max_


def maximize_elements(t1, t2):
    return tuple(max_((max(a, b), i) for i, (a, b) in enumerate(zip(t1, t2)))[0] for _ in chain.from_iterable(starmap(zip, zip(t1, t2))))


# Alternatively, a more readable version:
def maximize_elements(t1, t2):
    """
    >>> maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3)))
    ((6, 7), (4, 9), (2, 9), (7, 10))
    """
    combined = zip(t1, t2)
    max_elements = []
    for pair_index, pair in enumerate(combined):
        max_elements.append(max(pair))
    return tuple(max_elements)


# Alternatively, a more efficient version:
def maximize_elements(t1, t2):
    """
    >>> maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3)))
    ((6, 7), (4, 9), (2, 9), (7, 10))
    """
    max_elements = []
    for i, (a, b) in enumerate(zip(t1, t2)):
        max_elements.append(max(a, b))
    return tuple(max_elements)


# Alternatively, a more efficient version using built-in functions:
def maximize_elements(t1, t2):
    """
    >>> maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1),