"""
Write a function to remove tuples from the given tuple.
assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)
"""
from typing import Callable

def remove_nested(tuple_, filter_function: Callable[[int], bool] = lambda x: True) -> tuple:
    """Remove elements from a nested tuple.

    Args:
        tuple_ (tuple): The tuple to be removed the nested elements from.

        filter_function (Callable): A function that takes an integer and returns
            True if it is supposed to remain in the tuple, False otherwise.

    Returns:
        2-tuple: The result of removing the tuple's elements from the original tuple.

    Examples:
        >>> remove_nested((1, 5, (4, 6), 10))
        (1, 5, 10)

        >>> remove_nested((1, 5, (4, 6), 10), lambda i: 3 < i)
        (1, 5, 10)
    """
    n = len(tuple_) - 1

    if not isinstance(tuple_, tuple):
        tuple_ = list(tuple_)
    
    if filter_function is None or filter_function(*tuple_).__nonzero__() == False:
        return tuple_(filter((lambda x: filter_function(*x)[0] != 4), range(n)))
    else:
        return tuple_(filter((lambda i: (i, filter_function(tuple_[i], *args=tuple_, index=i))), range(n)))
