The problem is asking to write a function that finds the maximum value in a given heterogeneous list. The list can contain any type of elements, including strings, integers, floats, etc.

However, the problem does not specify what type of values should be considered for the maximum. For example, should we consider only integers and floats, or should we consider all values including strings?

Thanks to the provided unit test, `assert max_val(['Python', 3, 2, 4, 5, 'version'])==5`, we can assume that the maximum value is the highest integer in the list. This means we should ignore non-integer values in the list.

Here is a Python solution for the problem:

```python
def max_val(lst):
    max_val = float('-inf')
    for val in lst:
        if isinstance(val, int):
            max_val = max(max_val, val)
    return max_val
```

This function iterates over the list, checks if each value is an integer, and updates the maximum value if it is. The function returns the maximum value found in the list. If the list is empty, the function returns negative infinity.