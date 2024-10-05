    mean = sum(numbers) / len(numbers)
    return sum(abs(num - mean) for num in numbers) / len(numbers)


def mean_absolute_deviation_list(numbers: List[List[float]]) -> List[float]:
    """ For a given list of input numbers, calculate the Mean Absolute
    Deviation for each sub-list (i.e. return a list of MAD for each
    sub-list):
    >>> mean_absolute_deviation_list([[1.0, 2.0, 3.0, 4.0]])
    [1.0]
    """
    return [mean_absolute_deviation(numbers) for numbers in numbers]


def mean_absolute_deviation_tuple(numbers: List[List[float]]) -> List[float]:
    """ For a given list of input numbers, calculate the Mean Absolute
    Deviation for each sub-tuple (i.e. return a list of MAD for each
    sub-tuple):
    >>> mean_absolute_deviation_tuple([(1.0, 2.0, 3.0, 4.0)])
    [1.0]
    """
    return [mean_absolute_deviation(numbers) for numbers in numbers]


if __name__ == '__main__':
    print(mean_absolute_deviation_list([[1.0, 2.0, 3.0, 4.0]]))
    print(mean_absolute_deviation_tuple([(1.0, 2.0, 3.0, 4.0)]))

































































































































