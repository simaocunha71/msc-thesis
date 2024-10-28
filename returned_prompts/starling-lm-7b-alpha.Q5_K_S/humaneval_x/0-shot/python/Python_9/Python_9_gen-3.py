    max_num = [numbers[0]]
    for i in range(1, len(numbers)):
        max_num.append(max(numbers[i], max_num[i - 1]))
    return max_num


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 2, 2]
    """
    min_num = [numbers[0]]
    for i in range(1, len(numbers)):
        min_num.append(min(numbers[i], min_num[i - 1]))
    return min_num


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum until given moment in the sequence.
    >>> rolling_sum([1, 2, 3, 2, 3, 4, 2])
    [1, 3, 6, 8, 11, 13, 15]
    """
    sum_num = [numbers[0]]
    for i in range(1, len(numbers)):
        sum_num.append(sum_num[i - 1] + numbers[i])
    return sum_num


def rolling_count(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling count of the current element until given
    moment in the sequence.
    >>> rolling_count([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 2, 2, 2, 2]
    """
    count_num = [1 for _ in numbers]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
