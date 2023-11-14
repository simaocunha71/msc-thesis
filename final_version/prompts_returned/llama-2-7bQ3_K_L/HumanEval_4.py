from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    total_sum = sum(numbers)
    total_num = len(numbers)

    devs = [abs(x - total_sum / total_num) for x in numbers]

    return math.sqrt(sum([x ** 2 for x in devs]) / len(devs))
