    rolling_max = []
    current_max = numbers[0]

    for number in numbers:
        current_max = max(current_max, number)
        rolling_max.append(current_max)

    return rolling_max


def rolling_min(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling minimum element found until given moment
    in the sequence.
    >>> rolling_min([1, 2, 3, 2, 3, 4, 2])
    [1, 1, 1, 2, 2, 3, 3]
    """
    rolling_min = []
    current_min = numbers[0]

    for number in numbers:
        current_min = min(current_min, number)
        rolling_min.append(current_min)

    return rolling_min


def rolling_sum(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling sum of all elements up to the current moment
    in the sequence.
    >>> rolling_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    """
    rolling_sum = []
    current_sum = 0

    for number in numbers:
        current_sum += number
        rolling_sum.append(current_sum)

    return rolling_sum


def rolling_product(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling product of all elements up to the current
    moment in the sequence.
    >>> rolling_product([1, 2, 3, 4])
    [1, 2, 6, 24]
    """
    rolling_product = []
    current_product = 1

    for number in numbers:
        current_product *= number
        rolling_product.append(current_product)

    return rolling_product


def rolling_any(numbers: List[int], condition: callable) -> List[int