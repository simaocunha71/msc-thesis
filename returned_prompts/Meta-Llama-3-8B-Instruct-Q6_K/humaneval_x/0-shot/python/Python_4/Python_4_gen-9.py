from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    deviation = [abs(num - mean) for num in numbers]
    return sum(deviation) / len(deviation)
# for example:
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
# Explanation:
# 1. Calculate the mean of the input list.
# 2. Calculate the absolute difference between each element and the mean.
# 3. Calculate the mean of these differences to get the Mean Absolute Deviation.  # noqa: E501
# 4. The mean Absolute Deviation for the list [1.0, 2.0, 3.0, 4.0] is 1.0.  # noqa: E501
# 5. This is because the mean of the list is 2.5, and the absolute differences  # noqa: E501
#    between each element and the mean are 1.5, 0.5, 0.5, 1.5, which sum to 4.0,  # noqa: E501
#    and the average of these differences is 1.0.