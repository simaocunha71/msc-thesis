    from math import fabs
    from statistics import mean

    # calculate the mean
    mean_num = mean(numbers)

    # calculate the mean absolute difference
    mad = sum([fabs(x - mean_num) for x in numbers]) / len(numbers)

    return mad


if __name__ == "__main__":
    print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))





def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    from math import fabs
    from statistics import mean

    # calculate the mean
    mean_num = mean(numbers)

    # calculate the mean absolute difference
    mad = sum([fabs(x - mean_num) for x in numbers]) / len(numbers)

    return mad


if __name__ == "__main__":
    print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))






def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    from math import fabs
    from statistics import mean

    # calculate the mean
    mean_num = mean(numbers