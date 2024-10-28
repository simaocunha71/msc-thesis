from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    return [(x - min_num) / (max_num - min_num) for x in numbers]

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = rescale_to_unit(numbers)
print(result)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```
In this code, the function `rescale_to_unit` takes a list of numbers as input. It first calculates the minimum and maximum values in the list. Then, for each number in the list, it calculates the proportion of the number's distance from the minimum value to the maximum value. This proportion is used to rescale the number to the range [0, 1].

The `min` and `max` functions are used to find the minimum and maximum values in the list. The list comprehension is used to apply the rescaling to each number in the list. The result is a new list where each number has been rescaled to the range [0, 1]. This is a common technique used in data preprocessing, for example, in machine learning, where it is often necessary to normalize the data to have the same range. This is particularly important when using certain algorithms that are sensitive to the range of the input data.