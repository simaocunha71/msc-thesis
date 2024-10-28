```
def last_Digit(n):
    return n % 10
```
The function `last_Digit` takes an integer `n` as input and returns the last digit of `n`. This is achieved by using the modulus operator `%`, which returns the remainder of the division of `n` by 10. The last digit of `n` is the remainder, which is `n % 10`. For example, if `n` is 123, `n % 10` returns 3, which is the last digit of 123. This function passes the given unit test `assert last_Digit(123) == 3`. 