Here's a function that takes an array of integers and returns the ratio of zeroes to non-zeroes in the array.

```python
from typing import List
from math import isclose

def zero_count(nums: List[int]) -> float:
    zero_count = 0
    non_zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            non_zero_count += 1
    return zero_count / non_zero_count if non_zero_count != 0 else 0
```

In this function, we initialize two counters: `zero_count` and `non_zero_count`. We iterate through the input array, and for each element, if it's equal to zero, we increment `zero_count`. Otherwise, we increment `non_zero_count`. Finally, we return the ratio of `zero_count` to `non_zero_count`.

To test the function, we can use the `assert` statement to check if the result of `zero_count` is approximately equal to the expected value of 0.181818 within a relative tolerance of 0.001.

```python
assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
```

This assertion verifies that the function correctly computes the ratio of zeroes to non-zeroes in the given array.

```python
zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])  # Returns: 0.18181818181818182
```

Here's an example usage of the `zero_count` function, where it calculates the ratio of zeroes to non-zeroes in the provided array and returns the result.
```python
zero_count([