```
def is_Even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```


Explanation:
The function `is_Even(n)` checks whether a given number `n` is even or not. It uses the modulus operator `%` to find the remainder of the division of `n` by 2. If the remainder is 0, then the number is even, otherwise it's odd. The function returns a boolean value indicating whether the number is even or not. The unit test `assert is_Even(1) == False` ensures that the function correctly identifies odd numbers as False. 





