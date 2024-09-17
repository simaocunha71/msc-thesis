```
def find_tuples(tuples, k):
    return [t for t in tuples if all(i % k == 0 for i in t)]
```


This function uses a list comprehension to iterate over the list of tuples. For each tuple, it uses the built-in `all` function to check if all elements in the tuple are divisible by `k`. If they are, the tuple is added to the result list. The `all` function returns `True` if all elements in the iterable (in this case, the tuple) are true; otherwise, it returns `False`. The `all` function stops iterating as soon as it finds a false value, so it is more efficient than using a loop.

For example, `find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6)` returns `[(6, 24, 12)]`, because only the tuple `(6, 24, 12)` has all elements divisible by `6`. The other tuples have at least one element that is not divisible by `6`. The `assert` statement in the problem ensures that this function works correctly.