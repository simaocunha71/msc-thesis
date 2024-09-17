```
def find_Parity(n):
    if n % 2 != 0:
        return True
    else:
        return False
```


The function `find_Parity(n)` takes an integer `n` as an argument. It checks whether the remainder of `n` divided by 2 is not equal to 0. If the remainder is not 0, then the parity of `n` is odd, and the function returns `True`. If the remainder is 0, then the parity of `n` is even, and the function returns `False`. The unit test `assert find_Parity(12) == False` ensures that the function correctly identifies even numbers. For example, the parity of 12 is even, so the function should return `False`. 





