    if len(numbers) == 0:
        return []

    result = [numbers[0]]
    for i in range(len(numbers) - 1):
        result.append(delimeter)
        result.append(numbers[i + 1])
    result.append(numbers[-1])
    return result


# intersperse([], 4)
# intersperse([1, 2, 3], 4)
# intersperse([1, 2, 3, 4], 4)
# intersperse([1, 2, 3, 4, 5, 6], 4)
# intersperse([1, 2, 3, 4, 5, 6, 7], 4)
# intersperse([1, 2], 3)


# intersperse([1, 2], 1)


def test(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    >>> intersperse([1, 2, 3], 1)
    [1, 1, 2, 1, 3]
    >>> intersperse([1, 2, 3, 4], 1)
    [1, 1, 2, 1, 3, 1, 4]
    >>> intersperse([1, 2, 3, 4, 5, 6], 1)
    [1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6]
    """
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i != len(numbers) - 1:
            result.append(