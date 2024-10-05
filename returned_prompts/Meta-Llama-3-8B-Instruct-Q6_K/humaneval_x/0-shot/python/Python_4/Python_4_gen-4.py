from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ Calculate Mean Absolute Deviation around the mean of the dataset.
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of input numbers.

    Returns:
        float: Mean Absolute Deviation.
    """
    
    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)

    # Initialize sum of absolute deviations
    sum_deviations = 0

    # Calculate sum of absolute deviations
    for num in numbers:
        sum_deviations += abs(num - mean)

    # Calculate Mean Absolute Deviation
    mad = sum_deviations / len(numbers)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```
The `mean_absolute_deviation` function calculates the Mean Absolute Deviation (MAD) of a given list of numbers. It does this by first calculating the mean of the dataset, then calculating the sum of the absolute deviations from the mean, and finally dividing that sum by the length of the dataset.

The function takes a list of float numbers as input, calculates the mean, and then iterates over the list to calculate the sum of absolute deviations. The MAD is then calculated by dividing the sum of absolute deviations by the length of the list.

The example usage at the end demonstrates how to use the function with a list of numbers. In this case, the output is 1.0, which is the Mean Absolute Deviation of the dataset [1.0, 2.0, 3.0, 4.0].