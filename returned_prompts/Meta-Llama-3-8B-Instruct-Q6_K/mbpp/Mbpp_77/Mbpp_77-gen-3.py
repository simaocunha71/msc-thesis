```
def is_Diff(n):
    return sum(int(digit) for digit in str(n)) % 11 == 0
```



This function converts the number into a string, then iterates over each character in the string (which represents a digit in the number), converts it back into an integer, and sums all these digits. It then checks if the sum is divisible by 11. 

The unit test `assert is_Diff (12345) == False` is used to check if the function correctly identifies numbers that are not divisible by 11. 

Note that this function considers the number as a whole, not its digits. For example, 12345 is not divisible by 11, but its digits are. This is because the problem statement doesn't specify whether the digits should be considered individually or the number as a whole. 

If the problem statement meant to consider the digits individually, the function would need to be modified to calculate the alternating sum of the digits, i.e., the sum of the digits at even indices minus the sum of the digits at odd indices. 

Here is the modified function for that:

```
def is_Diff(n):
    n = str(n)
    even_sum = sum(int(digit) for i, digit in enumerate(n) if i % 2 == 0)
    odd_sum = sum(int(digit) for i, digit in enumerate(n) if i % 2 != 0)
    return even_sum - odd_sum % 11 == 0
```



This function calculates the sum of the digits at even indices and the sum of the digits at odd indices, then checks if the difference between these two sums is divisible by 11.  This is the standard way to check if a number is divisible by 11, considering the digits individually.  The unit test `assert is_Diff (12345) == False` still passes with this modified function.  However, the function now correctly identifies numbers that are not divisible by 11 considering the digits individually.  For example, the number 12345 is not divisible by 11 considering its digits individually, and the function correctly identifies this.  It would incorrectly identify 1111111111111111111 as not divisible by 11, because it's not divisible by 11 as a whole, but it is divisible by 11 considering its digits individually.  If the problem statement meant to consider the digits individually, this function should be used.  If the problem statement meant to consider