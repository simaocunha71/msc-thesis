```
def iscube(a):
    root = round(a ** (1. / 3.))
    return root ** 3 == a
```


The function `iscube(a)` takes an integer `a` as input and returns `True` if `a` is a cube of some integer number, and `False` otherwise.

It works by first calculating the cube root of `a` using the exponentiation operator `**` with a fractional exponent `1./3.`, and then rounding the result to the nearest integer using the `round()` function.

It then checks if the cube of this integer is equal to `a` using another exponentiation operator `**` with the exponent `3`. If this condition is true, it means that `a` is a cube of some integer number, so the function returns `True`. Otherwise, it returns `False`.