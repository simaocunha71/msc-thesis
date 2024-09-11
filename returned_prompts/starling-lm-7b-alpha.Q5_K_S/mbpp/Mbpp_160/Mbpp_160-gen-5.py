```
def find_solution(a, b, n):
    if n % gcd(a, b) != 0:
        return None
    else:
        x, y = 0, 0
        while b:
            q = a // b
            r = a % b
            a, b = b, r
            x, y = y, x - q * y
        return (n / a, x)
```

Here's an example of how to use this function:

```python
def gcd(a, b):
    while b:
        q = a // b
        r = a % b
        a, b = b, r
        return a
```

Explanation:
The function `find_solution` takes in three integers `a`, `b`, and `n`. It first checks if `n` is divisible by the greatest common divisor (GCD) of `a` and `b`. If it is not divisible, then there is no solution and the function returns `None`.

If `n` is divisible by the GCD, the function initializes two variables `x` and `y` to 0. It then uses a while loop to iteratively update the values of `a` and `b` using the Euclidean algorithm until `b` becomes 0. During each iteration, the function also updates the values of `x` and `y` to ensure that the equation `ax + by = n` holds true.

Finally, the function returns a tuple containing the values of `x` and `y` that satisfy the equation `ax + by = n`.

The `gcd` function is a helper function that calculates the GCD of two integers using the Euclidean algorithm. It is used in the `find_solution` function to check if `n` is divisible by the GCD of `a` and `b`.

Overall, this function finds the integers `x` and `y` that satisfy the equation `ax + by = n` and returns them as a tuple, or `None` if no solution exists.

To use this function, you can simply call it with the appropriate arguments, as shown in the example above.

```python