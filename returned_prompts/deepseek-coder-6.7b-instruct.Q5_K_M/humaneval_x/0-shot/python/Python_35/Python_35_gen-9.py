
    return max(l)


def min_element(l: list):
    """Return minimum element in the list.
    >>> min_element([1, 2, 3])
    1
    >>> min_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    -10
    """

    return min(l)


def sum_elements(l: list):
    """Return the sum of all elements in the list.
    >>> sum_elements([1, 2, 3])
    6
    >>> sum_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    116
    """

    return sum(l)


def average_elements(l: list):
    """Return the average of all elements in the list.
    >>> average_elements([1, 2, 3])
    2.0
    >>> average_elements([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    23.4
    """

    return sum(l) / len(l)


def count_elements(l: list, x):
    """Return the number of elements in the list that equals to x.
    >>> count_elements([1, 2, 3, 1, 1, 2, 2, 2, 3, 3, 3], 1)
    2
    >>> count_elements([1, 2, 3, 1, 1, 2, 2, 2, 3, 3, 3], 2)
    3
    >>> count_elements([1, 2, 3, 1, 1, 2, 2, 2, 3, 3, 3], 3)
    3
    """

    return l.count(x)


def reverse_list(l: list):
    """Return the list in