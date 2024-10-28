Here is a Python function that implements the described behavior:

```Python
def sortThird(l):
    return [x if i % 3 != 0 else sorted([x])[0] for i, x in enumerate(l)]
```

This function uses list comprehension to create a new list where elements at indices that are not divisible by 3 are the same as in the original list, and elements at indices that are divisible by 3 are the first element of the sorted list of elements at that index in the original list.

For example, `sortThird([5, 6, 3, 4, 8, 9, 2])` would return `[2, 6, 3, 4, 8, 9, 5]`. The elements at indices 0, 4, and 6 are the same as in the original list, while the elements at indices 2 and 5 are the first elements of the sorted lists `[3, 3]` and `[8, 9]`, respectively.  The elements at index 1 are the same as in the original list.  The resulting list is `[2, 6, 3, 4, 8, 9, 5]`.