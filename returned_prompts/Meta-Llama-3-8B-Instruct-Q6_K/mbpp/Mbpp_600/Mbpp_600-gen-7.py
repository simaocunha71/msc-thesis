```
def is_Even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```
The function `is_Even(n)` checks whether the given number `n` is even or not. It uses the modulus operator `%` to find the remainder of the division of `n` by 2. If the remainder is 0, then `n` is even, otherwise it is odd. The function returns `True` if `n` is even and `False` if `n` is odd. This solution passes the given unit test `assert is_Even(1) == False`.