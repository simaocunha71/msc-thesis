from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Check that the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All values in the list must be different")

    # Apply the linear transform
    scaled_numbers = [(n - min_val) / (max_val - min_val) for n in numbers]

    return scaled_numbers


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```


The provided code is a Python function named `rescale_to_unit` that takes a list of floats as input and returns a new list with the same numbers, but rescaled to be between 0 and 1. The rescaling is done by subtracting the minimum value in the list from each number, then dividing by the range of the list (i.e., the difference between the maximum and minimum values).

The function first checks that the input list has at least two elements, and raises a `ValueError` if not. It also checks that all values in the list are different, and raises a `ValueError` if not.

The example usage at the end of the code shows how to use the function with a list of numbers. The output is a new list with the same numbers, but rescaled to be between 0 and 1.