def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [v for v in values if isinstance(v, int)]


def filter_even_numbers(values: List[int]) -> List[int]:
    """ Filter given list of integers only for even numbers
    >>> filter_even_numbers([1, 2, 3, 4, 5, 6])
    [2, 4, 6]
    >>> filter_even_numbers([10, 11, 12, 13, 14, 15])
    [10, 12, 14]
    """
    return [v for v in values if v % 2 == 0]


def filter_odd_numbers(values: List[int]) -> List[int]:
    """ Filter given list of integers only for odd numbers
    >>> filter_odd_numbers([1, 2, 3, 4, 5, 6])
    [1, 3, 5]
    >>> filter_odd_numbers([10, 11, 12, 13, 14, 15])
    [11, 13, 15]
    """
    return [v for v in values if v % 2 != 0]


def filter_positive_numbers(values: List[int]) -> List[int]:
    """ Filter given list of integers only for positive numbers
    >>> filter_positive_numbers([1, -2, 3, -4, 5, -6])
    [1, 3, 5]
    >>> filter_positive_numbers([10, -11, 12, -13, 14, -15])
    [10, 12, 14]