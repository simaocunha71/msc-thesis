Here's how you might define the function:

```python
def x_or_y(n, x, y):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    return x if is_prime(n) else y
```

This function first defines a helper function `is_prime` to check if a number is prime. It then returns `x` if `n` is prime, and `y` otherwise.

You can test this function with the examples you provided:

```python
print(x_or_y(7, 34, 12))  # should output 34
print(x_or_y(15, 8, 5))   # should output 5
```