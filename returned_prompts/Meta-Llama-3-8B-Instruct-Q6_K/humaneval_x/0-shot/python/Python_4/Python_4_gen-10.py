from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate mean
    mean = sum(numbers) / len(numbers)

    # Calculate absolute deviations from the mean
    deviations = [abs(num - mean) for num in numbers]

    # Calculate mean of absolute deviations
    mad = sum(deviations) / len(deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
# Time complexity: O(n)
# Space complexity: O(n) for storing deviations, where n is the size of the input list.
# This function can be optimized further by avoiding the creation of an additional list for storing deviations. 
# We could directly calculate the sum of absolute deviations and then divide it by the number of elements. 
# This would reduce the space complexity to O(1). 

# Here is the optimized version:

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(num - mean) for num in numbers) / len(numbers)
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
# Time complexity: O(n)
# Space complexity: O(1) for optimized version.
# This optimized version is more memory efficient than the original function. 
# It achieves the same result without creating an additional list for storing deviations. 
# This optimization is particularly important when dealing with large datasets. 
# It can significantly reduce the memory usage and improve the performance of the function. 