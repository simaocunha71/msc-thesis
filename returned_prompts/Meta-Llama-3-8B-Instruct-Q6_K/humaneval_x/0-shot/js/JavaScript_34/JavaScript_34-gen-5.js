```python
def unique(l):
    return sorted(list(set(l)))
```


Explanation:
The problem is asking for a function that takes a list as input and returns a new list containing the unique elements from the input list in sorted order.

The solution uses the built-in Python functions `set` and `sorted`. The `set` function is used to remove duplicates from the list, and the `sorted` function is used to sort the resulting set.

Here's a breakdown of the solution:

1. `set(l)`: This converts the input list `l` to a set, which automatically removes any duplicate elements.
2. `list(set(l))`: This converts the set back to a list, so that we can use it as input to the `sorted` function.
3. `sorted(list(set(l)))`: This sorts the list of unique elements in ascending order and returns the result.

For example, if we call the `unique` function with the input list `[5, 3, 5, 2, 3, 3, 9, 0, 123]`, the function will return the list `[0, 2, 3, 5, 9, 123]`, which are the unique elements from the input list in sorted order.