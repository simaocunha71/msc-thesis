```
def divisor(n):
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d
```

Here's a Python function that takes an integer `n` and returns the number of divisors of `n`. It uses a loop to iterate through all integers from 1 to `n`, checking if each one is a divisor of `n`. If it is, it increments the counter variable `d`. Finally, it returns the value of `d`.

The function `divisor` can be tested using the provided `assert` statement. When `divisor(15)` is called, it should return `4` because the divisors of `15` are `1`, `3`, `5`, and `15`, so there are `4` divisors in total.

You can test the function with other integers as well to verify its correctness. For example, if you call `divisor(24)`, it should return `8` because the divisors of `24` are `1`, `2`, `3`, `4`, `6`, `8`, `12`, and `24`, so there are `8` divisors in total.

Overall, the function correctly calculates the number of divisors of a given integer using a simple loop and counter variable.

```python
def divisor(n):
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d
```

Here's a Python function that takes an integer `n` and returns the number of divisors of `n`. It uses a loop to iterate through all integers from 1 to `n`, checking if each one is a divisor of `n`. If it is, it increments the counter variable `d`. Finally, it returns the value of `d`.

The function `divisor` can be tested using the provided `assert` statement. When `divisor(15)` is called, it should return `4` because the divisors of `15` are `1`, `3`, `5`,