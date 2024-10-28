```
def last_Digit_Factorial(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    last_digit = 10
    for i in range(1, n + 1):
        last_digit = (last_digit * i) % 10
    return last_digit
```
The function `last_Digit_Factorial` calculates the last digit in the factorial of a given number. The factorial of a number is calculated by multiplying the number with the factorial of the number - 1. The last digit of the factorial of a number can be calculated by taking the last digit of the product of the number with the factorial of the number - 1. The function uses this property to calculate the last digit of the factorial of the given number.

The function first checks if the input is a non-negative integer. If the input is not a non-negative integer, it raises a ValueError. If the input is 0, it returns 1 because the factorial of 0 is 1.

Then, the function initializes a variable `last_digit` to 10. This is because the last digit of the factorial of any number is either 0 or 1, and 10 is a number that has a last digit of 0.

The function then calculates the last digit of the factorial of the given number by multiplying the number with the factorial of the number - 1 and taking the last digit of the product. This is done in a loop that runs from 1 to the given number.

Finally, the function returns the last digit of the factorial of the given number.

The unit test `assert last_Digit_Factorial(4) == 4` checks if the function correctly calculates the last digit of the factorial of the number 4. The expected output is 4, which is the last digit of the factorial of 4. The test passes if the function returns 4. If the function returns a different value, the test fails.