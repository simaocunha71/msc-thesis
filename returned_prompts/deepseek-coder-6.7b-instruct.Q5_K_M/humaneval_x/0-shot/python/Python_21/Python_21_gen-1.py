```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    return [(i - min_num) / (max_num - min_num) for i in numbers]

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```
In this Python code, we first find the minimum and maximum values from the input list. Then, for each element in the list, we subtract the minimum value from it and divide the result by the difference between the maximum and minimum values. This rescales the numbers in the list to the range 0-1.

We then return the list of transformed numbers.

When we run this code with the input `[1.0, 2.0, 3.0, 4.0, 5.0]`, it outputs the list `[0.0, 0.25, 0.5, 0.75, 1.0]`.

This is because the minimum value in the list is `1.0` and the maximum value is `5.0`. So, to rescale the numbers in the list to the range 0-1, we subtract `1.0` from each number and divide the result by `4.0` (the difference between `5.0` and `1.0`). This gives us the numbers `[0.0, 0.25, 0.5, 0.75, 1.0]`.

This is the expected output, so the function is working correctly.

Note: This function assumes that the input list has at least two elements, as per the question. If the list could have one element, you would need to add a check for that.









































































