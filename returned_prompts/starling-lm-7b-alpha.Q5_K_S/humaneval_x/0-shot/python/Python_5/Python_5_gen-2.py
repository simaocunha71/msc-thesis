    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[i])
        else:
            result.append(numbers[i])
            result.append(delimeter)
    return result


# Test
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]


# More Test
print(intersperse([1, 2, 3, 4, 5, 6, 7], 4))  # [1, 4, 2, 4, 3, 4, 4, 5, 4, 6, 4, 7]
print(intersperse([1, 2, 3, 4], 4))  # [1, 4, 2, 4, 3, 4]
print(intersperse([1, 2], 4))  # [1, 4, 2, 4]
print(intersperse([], 4))  # []


# 1

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of the input list `numbers`

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[i])
        else:
            result.append(numbers[i])
            result.append(delimeter)
    return result


# Test
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]


# More Test
