    from math import log, floor

    # Check if x is an integer
    if not x == int(x):
        return False

    # Calculate the log base n of x
    log_n = log(x) / log(n)

    # Check if log_n is an integer and x = n^log_n
    return log_n.is_integer() and pow(n, floor(log_n)) == x







```
```

```

```
```
```

In the `is_simple_power` function, we first check if the input `x` is an integer by comparing `x` with the result of `int(x)`. If `x` is not an integer, we return `False` immediately, as a number cannot be a simple power of another number if it's not an integer.

Next, we calculate the logarithm of `x` to the base `n` using the `log` function from the `math` module. We then divide the logarithm by the logarithm of `n` to get the log base `n` of `x`. We store this value in the variable `log_n`.

We then check if `log_n` is an integer by using the `is_integer` method. If it is an integer, we proceed to check if `x` can be expressed as `n` raised to the power of `log_n`. We do this by using the `pow` function, which raises `n` to the power of `floor(log_n)`. If the result of this calculation is equal to `x`, we return `True`, indicating that `x` is a simple power of `n`. Otherwise, we return `False`.

This algorithm ensures that `x` is a simple power of `n` by checking if the logarithm of `x` to the base `n` is an integer and if `x` can be expressed as `n` raised to that power.
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
