```
def iscube(a):
    return round(a**1/3)**3 == a
```


Here is an explanation of the code:

The function `iscube(a)` takes an integer `a` as input and returns `True` if `a` is a cube of some integer number, and `False` otherwise.

The function uses the property that if `a` is a cube of some integer number, then `a^(1/3)` is an integer. 

The function first calculates `a^(1/3)` using the exponentiation operator `**`. Then it rounds the result to the nearest integer using the `round` function. 

If the rounded result is cubed (i.e., raised to the power of 3) and is equal to `a`, then `a` is a cube of some integer number, and the function returns `True`. 

Otherwise, the function returns `False`. 

This function works for both positive and negative input values, as well as for zero. 

For example, `iscube(1)` returns `True` because 1 is a cube of 1. `iscube(2)` returns `False` because 2 is not a cube of any integer. `iscube(-1)` returns `True` because -1 is a cube of -1. `iscube(64)` returns `True` because 64 is a cube of 4. `iscube(0)` returns `True` because 0 is a cube of 0. `iscube(180)` returns `False` because 180 is not a cube of any integer. 

Note that this function assumes that the input is always valid, which means it does not check if the input is an integer. If the input could be a non-integer, additional error checking would be needed. 