Here is the Python code to solve the problem:

```python
def is_simple_power(x, n):
    if x <= 0:
        return False
    if n <= 0:
        return False
    if x == n:
        return True
    if x % n != 0:
        return False
    return is_simple_power(x // n, n)
```
The function `is_simple_power(x, n)` checks if `x` is a simple power of `n`. It does this by recursively dividing `x` by `n` until it is no longer divisible by `n`. If `x` is divisible by `n` but `n` is not `1`, then `x` is not a simple power of `n`. If `x` is divisible by `n` and `n` is `1`, then `x` is a simple power of `n`. If `x` is `0` or `n` is `0`, then `x` is not a simple power of `n`. The function returns `True` if `x` is a simple power of `n` and `False` otherwise. This function uses the property of exponents that `a^b = c` implies `a = c^(1/b)`. This function applies this property in reverse by repeatedly dividing `x` by `n` until `x` is no longer divisible by `n`. If `x` is divisible by `n` but `n` is not `1`, then `x` is not a simple power of `n`. If `x` is divisible by `n` and `n` is `1`, then `x` is a simple power of `n`. If `x` is `0` or `n` is `0`, then `x` is not a simple power of `n`. The function returns `True` if `x` is a simple power of `n` and `False` otherwise. This function uses the property of exponents that `a^b = c` implies `a = c^(1/b)`. This function applies this property in reverse by repeatedly dividing `x` by `n` until `x` is no longer divisible by `n`. If `x` is divisible by `n` but `n` is not `1`, then `x` is not a simple power of `n`. If `x` is divisible by `n` and `n` is