```
def is_Diff(n):
    num = str(n)
    if len(num) % 2 == 0:
        return sum(int(digit) for digit in num[::2]) - sum(int(digit) for digit in num[1::2]) == 0
    else:
        return sum(int(digit) for digit in num[::2]) - sum(int(digit) for digit in num[1::2]) % 11 == 0
```


Explanation: 
This function converts the input number to a string, then it splits the string into two parts: the first half and the second half. The sum of the first half and the negative of the sum of the second half is calculated. If the result is 0 (or divisible by 11), the function returns True, otherwise it returns False.

The condition `if len(num) % 2 == 0:` is used to handle the case where the length of the string is even. This is because when the length of the string is even, we can split the string into two equal parts, which makes the calculation easier. If the length of the string is odd, we add the extra digit to the first half and adjust the calculation accordingly. 

The unit test `assert is_Diff (12345) == False` is used to check the function. The number 12345 is not divisible by 11, so the function should return False. 





This function works because the sum of the digits in a number is divisible by 11 if and only if the number is divisible by 11. The reason is that the digits of a number can be thought of as a sequence of integers, and the sum of these integers is the number itself. Therefore, if the number is divisible by 11, the sum of its digits is also divisible by 11.

The function `is_Diff(n)` checks whether the sum of the digits in the number `n` is divisible by 11. It does this by converting the number to a string, then summing the digits in the string. If the sum is divisible by 11, the function returns `True`, otherwise it returns `False`.

The unit test `assert is_Diff (12345) == False` is used to check the function. The number 12345 is not divisible by 11, so the function should return `False`.