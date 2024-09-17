```
def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```


The function `prime_num(n)` takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise.

The function first checks if `n` is less than or equal to 1, in which case it is not a prime number and the function returns `False`.

Then, it iterates over the range from 2 to the square root of `n` (inclusive) using the `range` function. For each number `i` in this range, it checks if `n` is divisible by `i` using the modulo operator `%`. If `n` is divisible by `i`, then it is not a prime number and the function returns `False`.

If `n` is not divisible by any of the numbers in the range, then it is a prime number and the function returns `True`.

The unit test `assert prime_num(13) == True` ensures that the function correctly identifies 13 as a prime number.