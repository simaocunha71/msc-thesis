```
def find_Parity(n):
    return n % 2 != 0
```


This function works by taking an integer `n` as input and returning `True` if the parity of `n` is odd and `False` if it is even. The `%` operator is the modulus operator which returns the remainder of the division of `n` by 2. If the remainder is not zero, it means the parity of `n` is odd, otherwise, it's even. The unit test `assert find_Parity(12) == False` ensures that the function correctly identifies the parity of 12 as even. 





