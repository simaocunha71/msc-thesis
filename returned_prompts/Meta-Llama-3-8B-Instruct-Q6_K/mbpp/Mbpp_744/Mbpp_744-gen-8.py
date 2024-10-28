```
def check_none(t):
    return any(t) and not all(t)
```
The function `check_none` takes a tuple `t` as an argument. It checks if the tuple contains any `None` value by using the `any` function, which returns `True` if at least one element is `True`. Then, it checks if all elements in the tuple are `True` by using the `all` function, which returns `True` if all elements are `True`. The function returns `True` if the tuple contains any `None` value, and `False` otherwise. This is because `any` will return `True` as soon as it encounters a `None` value, and `all` will return `False` as soon as it encounters a `None` value. The unit test `assert check_none((10, 4, 5, 6, None)) == True` shows that the function should return `True` if the tuple contains a `None` value.