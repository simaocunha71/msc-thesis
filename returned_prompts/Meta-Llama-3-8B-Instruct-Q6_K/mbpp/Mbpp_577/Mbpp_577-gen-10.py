```
def last_Digit_Factorial(n):
    last_digit = 1
    for i in range(1, n+1):
        last_digit = (last_digit * i) % 10
    return last_digit
```
The problem is asking to find the last digit of the factorial of a given number. 

The unit test `assert last_Digit_Factorial(4) == 4` suggests that the function should return the last digit of the factorial of 4, which is 4.

The solution uses a loop to calculate the factorial of the given number, and the last digit of the factorial is calculated using the modulus operator `% 10`. This is because the last digit of the factorial of a number is the same as the last digit of the product of all the numbers from 1 to that number, which can be calculated using the modulus operator.

For example, the factorial of 4 is 24, and the last digit of 24 is 4. The function `last_Digit_Factorial(4)` will return 4, which is the expected output. 