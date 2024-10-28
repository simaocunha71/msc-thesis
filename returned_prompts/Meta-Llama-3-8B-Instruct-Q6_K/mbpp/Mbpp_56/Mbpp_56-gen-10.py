```
def check(n):
    rev = int(str(n)[::-1])
    return n == 2*rev - 1
```
This function works by first reversing the input number `n` and then checking if `n` is equal to twice its reverse minus 1. If the condition is met, the function returns `True`; otherwise, it returns `False`. The unit test `assert check(70) == False` ensures that the function correctly identifies numbers that are not one less than twice their reverse. For example, when `n=70`, the reverse is `07`, and `70` is not equal to `2*07-1`, so the function returns `False`. 