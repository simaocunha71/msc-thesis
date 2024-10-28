```python
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(max(result[-1], numbers[i]))

    return result
```

The `rolling_max` function takes a list of integers as input and returns a new list where each element is the maximum value found from the start of the list up to that point. This is done by iterating through the input list and using the `max` function to compare the current element with the maximum value found so far. The result is then appended to the `result` list, which is returned at the end.