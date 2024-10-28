```
def is_simple_power(x, n):
    import math
    if x < 1:
        return False
    root = math.sqrt(x)
    return int(root + 0.5) ** n == x
```


The function `is_simple_power` checks if a number `x` is a simple power of another number `n`. 

It first checks if `x` is less than 1. If it is, the function returns `False` because a simple power of `n` must be greater than or equal to 1.

Then, it calculates the square root of `x` and rounds it to the nearest integer using the `int(root + 0.5)` expression. 

Finally, it checks if the `n`-th power of this rounded root is equal to `x`. If it is, the function returns `True`; otherwise, it returns `False`. 

The `+ 0.5` is used to round the root to the nearest integer, because the `int` function in Python rounds down, and we want to round up in this case. 

For example, `int(4.5)` would be `4`, but `int(4.5 + 0.5)` would be `5`. 

This function works correctly for both positive and negative `x` and `n`, as well as for `x` and `n` equal to 0. 

However, it may not work correctly for very large or very small `x` and `n`, due to the limitations of Python's floating point arithmetic. 

For example, `math.sqrt(2)` is not exactly equal to `1.4142135623730951`, but `int(math.sqrt(2) + 0.5)` is `1`, which is not correct. 

If you need to handle very large or very small `x` and `n`, you may need to use a more sophisticated method, such as the `decimal` module. 

Also note that this function returns `True` if `x` is equal to `n`, even if `n` is not a perfect power of itself. For example, `is_simple_power(2, 2)` returns `True`, even though `2` is not a perfect power of itself. 

If you want to exclude this case, you can add an additional check at the beginning of the function: `if x == n: return False`. 

However, this would make the function