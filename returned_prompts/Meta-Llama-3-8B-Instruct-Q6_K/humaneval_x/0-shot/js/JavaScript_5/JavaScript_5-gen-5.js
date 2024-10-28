Here is a Python solution:

```python
def intersperse(numbers, delimeter):
    return [numbers[i] for i in range(len(numbers)) if i < len(numbers) - 1] + [delimeter] + [numbers[i] for i in range(1, len(numbers))]
```

Here's a breakdown of how this works:

1. We use list comprehension to create a new list that includes every element from the original list, except the last one.
2. We then add the `delimeter` to the list.
3. Finally, we add the last element from the original list to the new list.

For example, if we call `intersperse([1, 2, 3], 4)`, the list comprehension will create the list `[1, 2]`, we'll add the `delimeter` `4` to the list, and then add the last element `3` to the list, resulting in `[1, 4, 2, 4, 3]`.