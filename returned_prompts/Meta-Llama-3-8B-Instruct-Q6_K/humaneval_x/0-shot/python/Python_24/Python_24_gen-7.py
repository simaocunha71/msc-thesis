```
def largest_divisor(n: int) -> int:
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i
    return 1
```

Explanation:
This function iterates from `n-1` down to `1`, checking if each number is a divisor of `n`. The first number that is a divisor is the largest divisor, so we return that number. If no divisor is found (i.e., `n` is a prime number), the function returns `1`, which is a divisor of every number.

The unit test `>>> largest_divisor(15)` returns `5`, which is the largest number that divides `15` evenly, smaller than `15`. This test helps to verify that the function is working correctly.