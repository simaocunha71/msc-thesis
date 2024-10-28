```
def below_threshold(l: list, t: int):
    return all(i < t for i in l)
```


This function takes a list `l` and an integer `t` as input. It returns `True` if all numbers in the list are below the threshold, and `False` otherwise.

The `all` function is a built-in Python function that returns `True` if all elements of an iterable (in this case, the generator expression `(i < t for i in l)`) are true. If at least one element is false, `all` returns `False`.

The generator expression `(i < t for i in l)` generates a sequence of boolean values, each of which is `True` if the corresponding element in the list is less than the threshold, and `False` otherwise.

For example, `below_threshold([1, 2, 4, 10], 100)` returns `True` because all the numbers in the list are less than 100. On the other hand, `below_threshold([1, 20, 4, 10], 5)` returns `False` because the number 20 is not less than 5.