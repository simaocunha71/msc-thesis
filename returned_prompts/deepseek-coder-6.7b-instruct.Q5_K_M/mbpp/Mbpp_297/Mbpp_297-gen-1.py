Here is a Python solution using recursion:

```python
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))
```

This function works by iterating through each item in the input list. If the item is a list itself, the function calls itself (recursion) on this sublist and appends the result to the flat_list. If the item is not a list, it is simply appended to the flat_list. The function repeats this process until all items have been processed and the flat_list has been returned.

The output of this script will be:

```
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
```

which is the flattened version of the input list.
"""

# ---------------------
"""
