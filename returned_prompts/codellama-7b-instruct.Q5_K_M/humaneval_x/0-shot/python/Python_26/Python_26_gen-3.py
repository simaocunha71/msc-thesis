from collections import OrderedDict


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = OrderedDict()
    for num in numbers:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1

    return [num for num, _ in seen.items() if seen[num] == 1]
