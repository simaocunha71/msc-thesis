    result = []
    for element in numbers:
        if element not in result:
            result.append(element)
    return result


# Testing
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([]))  # []
print(remove_duplicates([1]))  # [1]
print(remove_duplicates([1, 1, 1]))  # [1]


def remove_duplicates_v2(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates_v2([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    unique_numbers = set(numbers)
    result = []
    for number in unique_numbers:
        result.append(number)
    return result


# Testing
print(remove_duplicates_v2([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates_v2([1, 1, 2, 2, 3, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates_v2([]))  # []
print(remove_duplicates_v2([1]))  # [1]
print(remove_duplicates_v2([1, 1, 1]))  # [1]


def remove_duplicates_v3(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once