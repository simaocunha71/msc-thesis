from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)  # calculate the mean
    deviations = [abs(num - mean) for num in numbers]  # calculate the deviations
    return sum(deviations) / len(deviations)  # return the mean of the deviations
# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
# Explanation:
# The mean of the input numbers is (1+2+3+4)/4 = 10/4 = 2.5
# The absolute deviations from the mean are:
# |1-2.5| = 1.5, |2-2.5| = 0.5, |3-2.5| = 0.5, |4-2.5| = 1.5
# The mean of these absolute deviations is (1.5+0.5+0.5+1.5)/4 = 1.0
# The function returns the mean absolute deviation, which is 1.0 in this case.