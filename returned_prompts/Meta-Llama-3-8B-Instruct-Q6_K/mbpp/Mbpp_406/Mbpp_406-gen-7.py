```
def find_Parity(n):
    if n % 2 == 0:
        return False
    else:
        return True
```


Explanation:
The parity of a number is defined as whether the number is even or odd. In this problem, we need to find whether the parity of the given number is odd. 

A number is even if it is divisible by 2, and odd if it is not divisible by 2. Therefore, we can use the modulus operator `%` to check if the number is divisible by 2. If the remainder is 0, the number is even, and if the remainder is 1, the number is odd.

The unit test `assert find_Parity(12) == False` suggests that the function should return `False` for even numbers and `True` for odd numbers. 

So, the function `find_Parity` takes an integer `n` as input and returns `False` if `n` is even and `True` if `n` is odd. 

For example, `find_Parity(12)` returns `False` because 12 is even, and `find_Parity(13)` returns `True` because 13 is odd. 