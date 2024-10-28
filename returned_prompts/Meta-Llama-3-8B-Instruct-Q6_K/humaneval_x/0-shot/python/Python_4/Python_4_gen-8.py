from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

    mean = statistics.mean(numbers)
    deviations = [abs(num - mean) for num in numbers]
    mad = statistics.mean(deviations)
    return mad

# Example usage:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
print(mean_absolute_deviation([5.0, 10.0, 15.0, 20.0]))  # Output: 5.0

# Check for different types of numbers (integers, floats):
print(mean_absolute_deviation([1, 2, 3, 4]))  # Output: 1.0
print(mean_absolute_deviation([5.5, 10.5, 15.5, 20.5]))  # Output: 5.5

# Test with a single number:
print(mean_absolute_deviation([5]))  # Output: 0.0
print(mean_absolute_deviation([5.5]))  # Output: 0.0

# Test with an empty list:
print(mean_absolute_deviation([]))  # Output: ValueError: cannot calculate mean of an empty list
# This is expected, since the mean of an empty list is undefined. The function
# should raise an error in this case. You can add error handling to deal with
# this situation if needed.