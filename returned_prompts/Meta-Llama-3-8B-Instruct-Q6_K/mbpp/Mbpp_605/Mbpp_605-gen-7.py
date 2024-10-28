```
def prime_num(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```


In this solution, the function `prime_num` checks if a given integer `n` is a prime number. It does this by iterating from 2 to `n-1` and checking if `n` is divisible by any of these numbers. If `n` is divisible by any of these numbers, it is not a prime number and the function returns `False`. If `n` is not divisible by any of these numbers, it is a prime number and the function returns `True`. The function also checks if `n` is less than or equal to 1, in which case it is not a prime number and the function returns `False`. This is because prime numbers are greater than 1. The unit test `assert prime_num(13)==True` ensures that the function is working correctly.