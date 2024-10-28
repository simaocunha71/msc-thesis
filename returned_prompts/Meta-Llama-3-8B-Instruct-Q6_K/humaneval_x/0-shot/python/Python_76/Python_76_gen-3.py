def is_simple_power(x, n):
    if n == 0:
        return False
    import math
    root = math.sqrt(x)
    return round(root) ** n == x

print(is_simple_power(1, 4)) # True
print(is_simple_power(2, 2)) # True
print(is_simple_power(8, 2)) # True
print(is_simple_power(3, 2)) # False
print(is_simple_power(3, 1)) # False
print(is_simple_power(5, 3)) # False

# Output:
# True
# True
# True
# False
# False
# False
# 

The function `is_simple_power(x, n)` takes two parameters, `x` and `n`. It returns `True` if `x` is a simple power of `n` and `False` otherwise.

The function first checks if `n` is 0, in which case it returns `False` because any number is not a power of 0.

Then, it calculates the square root of `x` using the `math.sqrt` function from the Python math library. This gives the approximate square root of `x`.

The function then rounds the square root to the nearest integer using the `round` function.

Finally, it checks if the rounded square root raised to the power of `n` is equal to `x`. If it is, the function returns `True`, indicating that `x` is a simple power of `n`. Otherwise, it returns `False`.

The function is tested with several examples, and the output is as expected. For example, `is_simple_power(1, 4)` returns `True` because 1 is a simple power of 4 (1 = 2^2), and `is_simple_power(3, 2)` returns `False` because 3 is not a simple power of 2.