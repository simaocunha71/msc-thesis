
Here's a Python function that adds the even elements at odd indices of a non-empty list of integers:

```python
def add(lst):
    res = 0
    for i in range(0, len(lst), 2):
        res += lst[i]
    return res
```

To use this function, you can call it with a list of integers as an argument. For example, if you call `add([4, 2, 6, 7])`, the function will return `2`, which is the sum of the even elements at odd indices (i.e., `4` and `6`).

Here's a breakdown of how the function works:

- The `range(0, len(lst), 2)` expression generates a sequence of indices that start at `0`, end at `len(