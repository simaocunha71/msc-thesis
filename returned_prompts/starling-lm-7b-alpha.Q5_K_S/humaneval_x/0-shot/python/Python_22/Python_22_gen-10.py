def filter_integers(values: List[Any]) -> List[int]:
    integers = [x for x in values if isinstance(x, int)]
    return integers


# Some tests
assert filter_integers(['a', 3.14, 5]) == [5]
assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]


# Some more tests with exceptions
try:
    filter_integers([1, 2, 3, 'abc', [], []])
except TypeError as e:
    print(e)


try:
    filter_integers([])
except TypeError as e:
    print(e)


try:
    filter_integers([1, 2, 3, 4, 5, 'a'])
except TypeError as e:
    print(e)


try:
    filter_integers([1, 2, 3, None, 5])
except TypeError as e:
    print(e)


try:
    filter_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
except TypeError as e:
    print(e)


try:
    filter_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 'a'])
except TypeError as e:
    print(e)


# Some tests with exceptions

from typing import List, Any, Union


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    integers = [x for x in values if isinstance(x, (int, Union[int, float]))]
   