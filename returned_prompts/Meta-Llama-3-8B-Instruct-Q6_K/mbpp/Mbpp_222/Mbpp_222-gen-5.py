```
def check_type(tup):
    return all(type(x) == type(tup[0]) for x in tup)
```


The function `check_type` takes a tuple `tup` as input and returns a boolean value indicating whether all elements in the tuple have the same data type or not.

The function uses the built-in `all` function in combination with a generator expression to check if all elements in the tuple have the same type. The `all` function returns `True` if all elements in the iterable are true, and `False` otherwise.

The generator expression `type(x) == type(tup[0]) for x in tup` checks the type of each element `x` in the tuple and compares it with the type of the first element `tup[0]`. If all types match, the function returns `True`; otherwise, it returns `False`.

The unit test `assert check_type((5, 6, 7, 3, 5, 6) ) == True` confirms that the function works correctly for a tuple of integers.