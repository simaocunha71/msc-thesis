Here is the Python solution for the problem:

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_val = float('-inf')
    result = []
    for num in numbers:
        max_val = max(max_val, num)
        result.append(max_val)
    return result
```

In this solution, we initialize `max_val` as negative infinity and `result` as an empty list. Then, for each number in `numbers`, we update `max_val` as the maximum of the current `max_val` and the number. After that, we append `max_val` to `result`. Finally, we return `result`.

This function works by iterating through the input list once, and thus has a time complexity of O(n), where n is the length of the input list.

You can run this function with the example given in the problem statement as follows:

```python
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

This will print the correct output.

Note: The function uses Python's built-in `max` function to find the maximum value between `max_val` and the current number. This function works by iterating through the list only once, which results in a time complexity of O(1).

In summary, this function generates a list of rolling maximum elements by iterating through the input list once, which results in a time complexity of O(n), where n is the length of the input list.

The space complexity of the function is also O(n), where n is the length of the input list, because it stores the result in a new list.

This function is efficient and easy to understand.
