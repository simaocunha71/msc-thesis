Here's one way to solve this problem:

```python
def get_max_sum(n):
    """
    Given the equation f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n),
    find the maximum sum possible by using this equation with the given n.

    Args:
        n: An integer.

    Returns:
        The maximum sum possible by using the given equation.
    """
    def f(n):
        if n % 5 == 0 and n % 4 == 0 and n % 3 == 0 and n % 2 == 0:
            return n / 5 + n / 4 + n / 3 + n / 2
        if n % 5 == 0 and n % 4 == 0 and n % 3 == 0:
            return n / 5 + n / 4 + n / 3
        if n % 5 == 0 and n % 4 == 0:
            return n / 5 + n / 4
        if n % 5 == 0 and n % 3 == 0:
            return n / 5 + n / 3
        if n % 4 == 0 and n % 3 == 0:
            return n / 4 + n / 3
        if n % 5 == 0:
            return n / 5
        if n % 4 == 0:
            return n / 4
        if n % 3 == 0:
            return n / 3
        return n

    return f(n)
```

This function first defines an inner function `f` that computes the value of the equation for a given `n`. It then uses this inner function to compute the maximum sum possible by using the equation with the given `n`.

The `f` function checks for several cases, such as whether `n` is divisible by 5, 4, 3, and 2. It returns the maximum value based on these cases. If `n` is not divisible by any of these numbers, it simply returns `n`.

The `get_max_sum` function