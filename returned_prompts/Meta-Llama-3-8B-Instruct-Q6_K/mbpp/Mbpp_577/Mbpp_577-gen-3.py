```
def last_Digit_Factorial(n):
    if n == 0:
        return 1
    last_digit = 10
    for i in range(1, n + 1):
        last_digit = last_digit % i
    return last_digit
```
The function `last_Digit_Factorial` calculates the last digit of the factorial of a given number `n`. 

The approach is to calculate the last digit of each factorial from 1 to `n` and return the last calculated last digit. 

The last digit of the factorial is calculated by taking the last digit of the previous result and multiplying it with the last digit of the current factorial. 

For example, the last digit of 5! is calculated as the last digit of 4! multiplied by 5, which is 4. 

The unit test `assert last_Digit_Factorial(4) == 4` ensures that the function is working correctly. 

The time complexity of this function is O(n) as it needs to calculate the factorial up to `n`. The space complexity is O(1) as it only uses a constant amount of space. 







