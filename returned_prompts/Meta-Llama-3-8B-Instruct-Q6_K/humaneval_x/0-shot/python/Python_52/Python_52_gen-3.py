```
def below_threshold(l: list, t: int):
    return all(i < t for i in l)
```


In this code, the function `below_threshold` takes a list `l` and an integer `t` as input. It returns `True` if all elements in the list `l` are less than `t`, and `False` otherwise.

The `all()` function is a built-in Python function that returns `True` if all elements of the iterable (in this case, a generator expression) are `True`. The generator expression `(i < t for i in l)` yields `True` for each element `i` in the list `l` if `i` is less than `t`, and `False` otherwise.

For example, if we call `below_threshold([1, 2, 4, 10], 100)`, the function will return `True` because all elements in the list are less than 100. On the other hand, if we call `below_threshold([1, 20, 4, 10], 5)`, the function will return `False` because 20 is not less than 5.