from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint  (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(n - mean) for n in numbers) / len(numbers)
    return mad


print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))

This function first calculates the mean of the input numbers. Then it calculates the absolute difference between each number and the mean, sums up these differences, and divides by the number of elements to get the Mean Absolute Deviation. The result is returned.

The function is tested with a list [1.0, 2.0, 3.0, 4.0] and the expected result is 1.0.

The function uses python's built-in `abs` function to calculate the absolute value of the difference between each number and the mean. The `sum` function is used to sum up these differences and the `len` function is used to calculate the number of elements in the input list.

The function also uses python's built-in `sum` and `len` functions to calculate the mean of the input numbers.

The function is a good example of how to use python's built-in functions to calculate the mean absolute deviation of a list of numbers.
