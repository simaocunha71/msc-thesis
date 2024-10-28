```python
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two numbers")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize variables to store the closest pair and their difference
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])

    # Iterate through the list to find the closest pair
    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i + 1] - numbers[i])

        if diff < min_diff:
            closest_pair = (numbers[i], numbers[i + 1])
            min_diff = diff

    return closest_pair
```
