from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    return [v for v in values if isinstance(v, int)]

# Example usage:
print(filter_integers(['a', 3.14, 5]))  # Output: [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```


In this solution, we use a list comprehension to filter the input list `values`. The comprehension iterates over each value `v` in the list and checks if it is an instance of `int` using the `isinstance` function. If it is, the value is included in the output list. Otherwise, it is skipped.

The `filter_integers` function takes a list of any Python values as input and returns a new list containing only the integers from the original list.

The example usage demonstrates the function's behavior with two different input lists. In the first case, the function returns a list containing only the integer `5`. In the second case, it returns a list containing the integers `1`, `2`, and `3`. The non-integer values in the input lists (`'a'`, `3.14`, `'abc'`, `{}`, and `[]`) are ignored.