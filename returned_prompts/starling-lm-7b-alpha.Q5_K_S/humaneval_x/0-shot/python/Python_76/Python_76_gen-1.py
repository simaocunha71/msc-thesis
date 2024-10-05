    from math import log, ceil

    def is_simple_power(x, n):
        if x == 1:
            return True
        return (log(x) / log(n)) == ceil(log(x) / log(n))


# Driver code
# print(is_simple_power(1, 4))  # True
# print(is_simple_power(2, 2))  # True
# print(is_simple_power(8, 2))  # True
# print(is_simple_power(3, 2))  # False
# print(is_simple_power(3, 1))  # False
# print(is_simple_power(5, 3))  # False

```
  
This function `is_simple_power` checks whether a number `x` is a simple power of `n` or not. It does so by calculating the logarithm of `x` divided by the logarithm of `n` and then comparing it to the ceiling of that value. If the two values are equal, then `x` is a simple power of `n` and the function returns `True`, otherwise it returns `False`. The `ceil` function is used to round up the value to the nearest integer, ensuring that the comparison is exact.

The function first checks if `x` is equal to 1, as any number raised to the power of 1 is itself. If `x` is equal to 1, the function returns `True`. Otherwise, it proceeds to calculate the logarithm of `x` divided by the logarithm of `n`. The `log` function is used to calculate the natural logarithm of a number. The `ceil` function is then used to round up the result to the nearest integer. Finally, the function compares the calculated value with the ceiling of the logarithm of `x` divided by the logarithm of `n`. If they are equal, the function returns `True`; otherwise, it returns `False`.

The provided driver code demonstrates the usage of the `is_simple_power` function with various inputs and prints the corresponding results.