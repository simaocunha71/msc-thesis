```
def is_Even(n):
    return n % 2 == 0
```


Explanation:
The provided unit test `assert is_Even(1) == False` suggests that the function should return `False` for odd numbers. The function `is_Even(n)` takes an integer `n` as input and returns `True` if `n` is even, and `False` otherwise.

The function works by using the modulus operator `%` which returns the remainder of the division of `n` by `2`. If the remainder is `0`, then `n` is even, and the function returns `True`. Otherwise, the function returns `False`.

For example, `is_Even(4)` returns `True` because `4 % 2 == 0`, and `is_Even(3)` returns `False` because `3 % 2 != 0`. 

This function is a simple and efficient way to check whether a given number is even or not. 