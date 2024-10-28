```
def is_Diff(n):
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum % 11 != 0
```
Explanation: 
The function is_Diff checks if the sum of the digits of the given number is divisible by 11. If the sum is not divisible by 11, the function returns True, indicating that the number is not divisible by 11. If the sum is divisible by 11, the function returns False, indicating that the number is divisible by 11.

The unit test `assert is_Diff (12345) == False` ensures that the function correctly identifies the number 12345 as not divisible by 11. This is because the sum of the digits of 12345 is 15, which is not divisible by 11. 
This function works by first converting the number into a string and then iterating over each character in the string, converting it back to an integer, and summing up these digits. The result is then checked to see if it is divisible by 11. 
If the sum of the digits is not divisible by 11, the function returns True, indicating that the number is not divisible by 11. If the sum is divisible by 11, the function returns False, indicating that the number is divisible by 11. 
This function can be used to check if a number is divisible by 11, but it is not the most efficient method for large numbers. A more efficient method would be to use the built-in modulo operator, which can be used to check if a number is divisible by 11 in O(1) time. 
Here is an example of how to use the built-in modulo operator to check if a number is divisible by 11:
```
def is_Diff(n):
    return n % 11 != 0
```
This function is much simpler and more efficient than the original function, but it does not work for negative numbers. If you need to check if negative numbers are divisible by 11, you can modify the function to handle negative numbers:
```
def is_Diff(n):
    return abs(n) % 11 != 0
```
This function uses the built-in abs function to get the absolute value of the number, and then checks if the result is divisible by 11. This function works for both positive and negative numbers. 
In summary, the original function is not the most efficient method for checking if a number is divisible by 11