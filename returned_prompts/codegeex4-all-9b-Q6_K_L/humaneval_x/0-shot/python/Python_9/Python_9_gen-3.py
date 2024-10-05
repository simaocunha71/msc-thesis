from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    rolling_max_list = [numbers[0]]

    for i in range(1, len(numbers)):
        rolling_max_list.append(max(rolling_max_list[i-1], numbers[i]))

    return rolling_max_list

if __name__ == "__main__":
    import doctest
    doctest.testmod()

