```
def find_Parity(n):
    if n % 2 == 0:
        return False
    else:
        return True
```
The function `find_Parity` takes an integer `n` as input and returns a boolean value indicating whether the parity of `n` is odd or not. 

The parity of a number is determined by the remainder when the number is divided by 2. If the remainder is 0, the parity is even; otherwise, the parity is odd. 

The function uses the modulus operator `%` to find the remainder of `n` divided by 2. If the remainder is 0, the function returns `False` indicating even parity. Otherwise, it returns `True` indicating odd parity. 

The unit test `assert find_Parity(12) == False` ensures that the function correctly identifies the parity of 12 as even. 

This function can be used to find the parity of any integer. For example, `find_Parity(5)` will return `True` indicating that the parity of 5 is odd, while `find_Parity(10)` will return `False` indicating that the parity of 10 is even. 