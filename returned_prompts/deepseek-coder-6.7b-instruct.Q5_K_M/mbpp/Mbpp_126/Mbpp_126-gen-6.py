Here is the Python solution to the problem:

```python
def sum_common_divisors(a, b):
    def common_divisors(n):
        return set(i for i in range(1, n+1) if n % i == 0)

    return sum(common_divisors(a) & common_divisors(b))

assert sum_common_divisors(10, 15) == 6
```

This solution uses the `common_divisors` helper function to find the set of common divisors of two numbers. It then returns the sum of the intersection of these two sets of common divisors.
"""


def sum_common_divisors(a, b):
    def common_divisors(n):
        return set(i for i in range(1, n+1) if n % i == 0)

    return sum(common_divisors(a) & common_divisors(b))

assert sum_common_divisors(10, 15) == 6
```

This function works by first finding the set of divisors for each input number, `a` and `b`. It then finds the intersection of these two sets (i.e., the common divisors of `a` and `b`). Finally, it sums up the elements of this intersection set, yielding the desired sum of the common divisors.
"""
"""


def sum_common_divisors(a, b):
    def common_divisors(n):
        return set(i for i in range(1, n+1) if n % i == 0)

    return sum(common_divisors(a) & common_divisors(b))

assert sum_common_divisors(10, 15) == 6
"""


def sum_common_divisors(a, b):
    def common_divisors(n):
        return set(i for i in range(1, n+1) if n % i == 0)

    return sum(common_divisors(a) & common_divisors(b))

assert sum_common_div