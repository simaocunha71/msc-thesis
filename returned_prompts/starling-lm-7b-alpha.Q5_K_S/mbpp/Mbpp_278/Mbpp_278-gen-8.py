def count_first_elements(t):
    """
    Find the number of elements that occurs before the tuple element in the given tuple.
    >>> count_first_elements((1, 5, 7, (4, 6), 10) )
    3
    """
    count = 0
    for i in t:
        if isinstance(i, tuple):
            count += 1
    return count

# Many thanks to @cricket_007 for the help


"""
The above solution will fail for nested tuples like below.

assert count_first_elements(((1, 2, 3), (4, 5, 6), (7, 8, 9))) == 3
"""


def count_first_elements_2(t):
    """
    Find the number of elements that occurs before the tuple element in the given tuple.
    >>> count_first_elements_2((1, 5, 7, (4, 6), 10) )
    3
    >>> count_first_elements_2(((1, 2, 3), (4, 5, 6), (7, 8, 9))) == 3
    True
    """
    return sum(map(lambda x: x == tuple, t))


# Many thanks to @cricket_007 for the help


def count_first_elements_3(t):
    """
    Find the number of elements that occurs before the tuple element in the given tuple.
    >>> count_first_elements_3((1, 5, 7, (4, 6), 10) )
    3
    >>> count_first_elements_3(((1, 2, 3), (4, 5, 6), (7, 8, 9))) == 3
    True
    """
    return sum(map(lambda x: isinstance(x, tuple), t))


# Many thanks to @cricket_007 for the help


def count_first_elements_4(t):
    """
    Find the number of elements that occurs before the tuple element in the given tuple.
    >>> count_first_elements_4((1