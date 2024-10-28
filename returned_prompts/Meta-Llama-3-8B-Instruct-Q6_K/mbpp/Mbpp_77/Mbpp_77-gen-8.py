```
def is_Diff(n):
    return sum(int(digit) for digit in str(n)) % 11 == 0
```


The function `is_Diff(n)` takes an integer `n` as input, converts it to a string, iterates over each character (digit) in the string, converts each character back to an integer, sums up the digits, and checks if the sum is divisible by 11. If it is, the function returns `True`; otherwise, it returns `False`.

The unit test `assert is_Diff(12345) == False` ensures that the function works correctly by checking that the sum of the digits of the number 12345 is not divisible by 11. The function should return `False` for this input.

This solution uses the built-in `sum` function, `int` function, and `str` function in Python. The `str` function is used to convert the integer to a string, the `int` function is used to convert each character back to an integer, and the `sum` function is used to sum up the digits. The `%` operator is used to check if the sum is divisible by 11.