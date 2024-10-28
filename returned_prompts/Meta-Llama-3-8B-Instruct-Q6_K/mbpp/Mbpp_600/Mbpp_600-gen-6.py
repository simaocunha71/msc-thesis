```
def is_Even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

This function takes an integer `n` as input and returns `True` if the number is even, and `False` otherwise. The condition `n % 2 == 0` checks if the remainder of the division of `n` by 2 is 0, which is true for even numbers. 

The unit test `assert is_Even(1) == False` ensures that the function returns `False` for odd numbers.  If the number is even, the function will return `True`. 

For example, `is_Even(4)` will return `True` and `is_Even(3)` will return `False`. 

Remember to add the necessary unit tests to ensure the function behaves as expected.  This function can be further improved by handling non-integer inputs or edge cases as per the problem requirements. 