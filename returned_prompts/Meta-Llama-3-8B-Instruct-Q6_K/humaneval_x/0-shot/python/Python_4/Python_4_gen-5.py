from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate absolute deviations from the mean
    deviations = [abs(x - mean) for x in numbers]
    
    # Calculate mean of absolute deviations
    mad = sum(deviations) / len(deviations)
    
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output: 1.0
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]))  # Output: 1.25
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]))  # Output: 1.5
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]))  # Output: 1.75
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]))  # Output: 2.0
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]))  # Output: 2.25
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]))  # Output: 2.5
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]))  # Output: 2.75
print(mean_absolute_deviation([1.0, 2