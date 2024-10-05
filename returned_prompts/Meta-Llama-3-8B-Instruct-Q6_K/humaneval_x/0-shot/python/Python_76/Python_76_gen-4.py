```
def is_simple_power(x, n):
    if n <= 0:
        return False
    if x <= 0:
        return False
    if x == 1:
        return True
    if x == n:
        return True
    if x % n == 0:
        if x // n == n**int(math.log(x, n)):
            return True
        else:
            return False
    else:
        return False
```



The function `is_simple_power(x, n)` checks whether a number `x` is a simple power of `n`. It first checks if `n` or `x` is less than or equal to 0, in which case it returns `False`. Then it checks if `x` is 1 or `n`, in which case it returns `True`. 

If `x` is not 1 or `n`, it checks if `x` is divisible by `n`. If it is, it calculates `x // n` and checks if it is equal to `n` raised to the power of the integer part of the logarithm of `x` to the base `n`. If it is, it returns `True`; otherwise, it returns `False`. If `x` is not divisible by `n`, it returns `False`. 

The function uses the `math.log` function to calculate the logarithm of `x` to the base `n`, and the `int` function to calculate the integer part of the logarithm. 

Note that the `math.log` function returns the natural logarithm, so we need to specify the base as `n` to get the logarithm to the base `n`. 

This function works for positive integers `x` and `n`, and returns `False` for negative `x` or `n`. If you want to extend the function to work with negative `x` or `n`, you would need to add additional checks. 





```
import math
```





```
def is_simple_power(x, n):
    if n <= 0:
        return False
    if x <= 0:
        return False
    if x == 1:
        return True
    if x == n:
        return True
    if x % n == 0:
        if x // n == n**int(math.log(x, n)):
            return True
        else:
            return False
    else:
        return False
```





```
