from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [0] * len(numbers)
    for i in range(len(numbers)):
        result[i] = max(result[i-1], numbers[i])
    return result


def rolling_max_2(numbers):
    return [max(numbers[i:]) for i in range(len(numbers))]
