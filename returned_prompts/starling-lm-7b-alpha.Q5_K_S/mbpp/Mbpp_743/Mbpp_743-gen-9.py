def rotate_right(lst, k):
    return lst[k:] + lst[:k]


# Test
print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))  # [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

























"""
To rotate a given list by specified number of items to the right direction, we can use list slicing to select the range of indices from the original list.
For example, to rotate the list by k, we can use the following logic:

lst[k:] selects the range from index k to the end of the list;
lst[:k] selects the range from the start of the list to index k.
By concatenating the two ranges, we can rotate the list by k to the right.
"""

```python
def rotate_right(lst, k):
    return lst[k:] + lst[:k]
```

The `rotate_right` function takes two parameters: `lst`, which is the original list, and `k`, which is the number of positions to rotate the list to the right.

In the function body, we use list slicing to select the range of indices from index `k` to the end of the list (`lst[k:]`), and the range from the start of the list to index `k` (`lst[:k]`). By concatenating the two ranges using the `+` operator, we obtain a new list that has been rotated to the right by `k` positions.

For example, if we call `rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)`, the function will return `[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]`, which is the original list rotated to the right by 3 positions