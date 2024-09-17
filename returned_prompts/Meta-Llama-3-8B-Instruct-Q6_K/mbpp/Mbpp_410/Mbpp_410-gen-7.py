The problem is asking for a function that finds the minimum value in a given list. The list can contain different types of values like strings, integers, etc. 

However, the problem statement does not specify how to handle strings. But, based on the unit test `assert min_val(['Python', 3, 2, 4, 5, 'version'])==2`, it seems that the function should return the smallest numeric value in the list. If the list contains no numeric values, the function should return a default value, such as None.

Here's a Python function that solves the problem:

```
def min_val(lst):
    numeric_vals = [x for x in lst if isinstance(x, (int, float))]
    return min(numeric_vals) if numeric_vals else None
```

This function first filters out the non-numeric values from the list using a list comprehension. Then, it returns the minimum value from the filtered list. If the filtered list is empty (i.e., the original list contained no numeric values), the function returns None. 

For example, if you call `min_val(['Python', 3, 2, 4, 5, 'version'])`, the function will return `2`, which is the smallest numeric value in the list. If you call `min_val(['Python', 'version'])`, the function will return `None` because the list contains no numeric values. 