```
def find_Parity(n):
    return n % 2 != 0
```


This function checks whether the given number `n` is odd or not. It returns `True` if the number is odd and `False` if the number is even. The unit test `assert find_Parity(12) == False` confirms that the function works as expected. The number 12 is even, so the function returns `False`. 

The parity of a number is defined as the remainder when the number is divided by 2. If the remainder is 0, the number is even. If the remainder is 1, the number is odd. This is implemented in the function using the modulo operator `%`. The expression `n % 2 != 0` is `True` if `n` is odd and `False` if `n` is even.  This expression is used as the return value of the function. 





The time complexity of this function is O(1) because it only involves a constant number of operations and does not depend on the size of the input. The space complexity is also O(1) because it only uses a constant amount of space to store the function's local variables.