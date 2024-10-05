from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    deviations = [abs(n - mean) for n in numbers]
    mad = sum(deviations) / len(deviations)
    return mad

print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))

"""
The function works by first calculating the mean of the numbers. Then, it creates a list of absolute differences between each number and the mean. The function finally calculates the mean of these absolute differences, which is the Mean Absolute Deviation.
"""

"""
The time complexity of the function is O(n), where n is the length of the input list. This is because the function iterates through the list of numbers twice: once to calculate the mean, and once to calculate the absolute deviations from the mean. The space complexity is also O(n), due to the creation of the list of absolute deviations.
"""

"""
The function is tested with the input [1.0, 2.0, 3.0, 4.0] and returns 1.0, which is the expected result.
"""

"""
The function is a good example of how to calculate statistics from a dataset. It's important to note that the Mean Absolute Deviation is a measure of variability in a dataset, with a lower value indicating less variability.
"""

"""
The function also demonstrates how to handle errors that might occur if the input list is empty. If the input list is empty, the function will raise a ZeroDivisionError when calculating the mean. To handle this, you could modify the function to return a special value (like None) if the input list is empty.
"""

"""
Finally, the function demonstrates how to use list comprehension, a concise way to create lists based on existing lists. This makes the function more readable and efficient.
"""
"""
The function is tested with the input [1.0, 2.0, 3.0, 4.0] and returns 1.0, which is the expected result.
"""

"""
The function demonstrates how to calculate statistics from