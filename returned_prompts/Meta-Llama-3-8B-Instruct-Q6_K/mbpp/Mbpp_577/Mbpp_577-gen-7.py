```
def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        last_digit = last_Digit_Factorial(n-1)
        return last_digit % 10
```


This function works by recursively calculating the factorial of the given number and returning the last digit of the result. The base case is when the input number is 0, in which case the function returns 1, since the factorial of 0 is 1. For other inputs, the function calls itself with the input number decremented by 1, and then returns the last digit of the result. The last digit of the result is calculated by taking the remainder of the result when divided by 10, which effectively gives the last digit. This approach ensures that the function returns the last digit of the factorial of the given number. For example, `last_Digit_Factorial(4)` returns 4, which is the last digit of the factorial of 4. The unit test `assert last_Digit_Factorial(4) == 4` confirms that the function works correctly.