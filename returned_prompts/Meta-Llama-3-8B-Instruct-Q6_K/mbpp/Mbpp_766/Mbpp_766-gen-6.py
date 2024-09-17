You can use list comprehension to generate pairs of consecutive items in a given list. Here is a Python function that does this:

```python
def pair_wise(lst):
    return [(i, j) for i, j in zip(lst, lst[1:])]
```

This function uses the built-in `zip` function to pair each item in the list with the next item in the list. The `zip` function stops when the shorter list is exhausted, so if the list is of odd length, the last item will be paired with `None`.

For example, if you call `pair_wise([1,1,2,3,3,4,4,5])`, it will return `[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]`. This matches the expected output in the problem statement.