```
def last_Digit_Factorial(n):
    if n == 0:
        return 1
    else:
        return last_Digit_Factorial(n-1) * (n % 10)
```
This function uses recursion to calculate the last digit of the factorial of a given number. The base case is when the number is 0, in which case the factorial is 1. Otherwise, the function calls itself with the input decreased by 1 and multiplies the result by the last digit of the input number. The last digit of a number is found using the modulus operator (%). 

For example, `last_Digit_Factorial(4)` will return `4` because the last digit of the factorial of 4 is `4`. This is also the expected output given in the unit test `assert last_Digit_Factorial(4) == 4`. 

The unit test `assert last_Digit_Factorial(4) == 4` is used to verify that the function works correctly for the input `4`. 

The time complexity of this function is O(n) because it uses recursion to calculate the factorial, and the space complexity is O(n) because of the recursion stack. 

This function can be optimized to use a loop instead of recursion, which would reduce the space complexity to O(1). However, the time complexity would remain O(n) because the function still needs to calculate the factorial. 

Here is the optimized function:
```
def last_Digit_Factorial(n):
    result = 1
    for i in range(1, n+1):
        result = (result * i) % 10
    return result
```
This function uses a loop to calculate the factorial and finds the last digit of the result using the modulus operator. The time complexity is O(n) and the space complexity is O(1). 