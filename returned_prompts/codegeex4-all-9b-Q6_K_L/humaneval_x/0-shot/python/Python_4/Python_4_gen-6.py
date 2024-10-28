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
    n = len(numbers)
    if n == 0:
        raise ValueError("The input list is empty")
    mean = sum(numbers) / n
    return sum(abs(x - mean) for x in numbers) / n

print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]))