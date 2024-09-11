from math import factorial

def last_Digit_Factorial(x):
    # if x is less than 0, return 1
    if x < 0:
        return 1
    # get the factorial of x
    factorial_x = factorial(x)
    # find the last digit of factorial_x
    last_digit = factorial_x % 10
    return last_digit

# Test the function
print(last_Digit_Factorial(4))




"""
    You can use Python's built-in function `factorial()` to calculate the factorial of a given number.
    To find the last digit of the factorial, you can take the modulus of the factorial by 10.
"""

"""
    The last digit of a number's factorial is the same as the number's itself if the number is less than or equal to 4.
    For example, 3! = 3 * 2 * 1 = 6, and the last digit of 6 is 6.
"""

"""
    However, if the number is greater than 4, the last digit of the factorial is 0.
    For example, 5! = 5 * 4 * 3 * 2 * 1 = 120, and the last digit of 120 is 0.
"""

```python
# Test the function
print(last_Digit_Factorial(4))  # Output: 4
```

This code defines a function `last_Digit_Factorial` that takes a number `x` as input and calculates the factorial of `x`. It then finds the last digit of the factorial by taking the modulus of the factorial by 10. The function returns the last digit.

The test case `print(last_Digit_Factorial(4))` calls the function with the argument 4 and prints the result, which should be 4.

This test case verifies that the function correctly calculates the last digit of the factorial of a given number.

"""

```python
from math import factorial

def last_Digit_Factorial(x):
   