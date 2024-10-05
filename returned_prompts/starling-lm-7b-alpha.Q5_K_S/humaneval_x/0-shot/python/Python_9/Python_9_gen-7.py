    result = [max(numbers[:i + 1]) for i in range(len(numbers))]
    return result


def rolling_max_window(numbers: List[int], window: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence, with a given window of size.
    >>> rolling_max_window([1, 2, 3, 2, 3, 4, 2], 3)
    [1, 2, 3, 3, 4, 4, 4]
    """
    result = [max(numbers[i: i + window]) for i in range(len(numbers))]
    return result


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """

    result = [min(numbers[:i + 1]) for i in range(len(numbers))]
    return result


def rolling_min_window(numbers: List[int], window: int) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence, with a given window of size.
    >>> rolling_min_window([1, 2, 3, 2, 3, 4, 2], 3)
    [1, 1, 1, 2, 2, 2, 2]
    """

    result = [min(numbers[i: i + window]) for i in range(len(numbers))]
    return result


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of numbers until given moment in
    the sequence.
   