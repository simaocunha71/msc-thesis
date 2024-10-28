from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    differences = [abs(n - mean) for n in numbers]
    mad = sum(differences) / len(differences)
    return mad


print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))

"""
In this code, we first calculate the mean of the input numbers. Then, we create a list of the absolute differences between each number and the mean. Finally, we calculate the mean of these differences, which is the Mean Absolute Deviation.
"""

