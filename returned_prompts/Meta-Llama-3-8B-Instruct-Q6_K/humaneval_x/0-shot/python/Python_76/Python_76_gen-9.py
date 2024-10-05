```
def is_simple_power(x, n):
    if x < 1:
        return False
    root = int(x ** (1/n))
    return root ** n == x
```


This function first checks if x is less than 1, in which case it returns False because a simple power of n must be greater than or equal to 1.

Then it calculates the root of x to the power of 1/n, and converts this root to an integer. This is because a simple power of n must have an integer root.

Finally, it checks if the root raised to the power of n is equal to x. If it is, the function returns True, meaning that x is a simple power of n. If not, it returns False.