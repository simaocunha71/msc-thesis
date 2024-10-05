from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    return [numbers[0]] + [delimeter] + intersperse(numbers[1:], delimeter)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

The function `intersperse` takes two arguments: a list of integers `numbers` and an integer `delimeter`. It inserts the `delimeter` between every two consecutive elements of the list `numbers`. If the list is empty, it returns an empty list. Otherwise, it returns a new list that starts with the first element of `numbers`, followed by the `delimeter`, and followed by the result of recursively calling `intersperse` on the remainder of the list.

The `doctest.testmod()` function is used to test the `intersperse` function with the provided examples.