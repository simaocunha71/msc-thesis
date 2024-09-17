```
def first_Digit(n):
    if n < 0:
        n = -n
    return int(str(n)[0])
```
The function first checks if the number is negative, if so, it converts it to positive. Then it converts the number to a string, and returns the first character of the string, which is the first digit of the number. The `int()` function is used to convert the string character back to an integer. For example, `int('1')` returns `1`. 

The unit test `assert first_Digit(123) == 1` ensures that the function returns the correct result. This test passes because `first_Digit(123)` returns `1`, which is the first digit of `123`. 

This function works for both positive and negative numbers, and for numbers with multiple digits. For example, `first_Digit(12345)` returns `1`, and `first_Digit(-12345)` also returns `1`. 

Note that this function returns the first digit of the number as an integer, not as a string. If you want the function to return the first digit as a string, you can remove the `int()` function and return `str(n)[0]` instead. For example, `return str(n)[0]` would return `'1'` for `first_Digit(123)`.  However, the unit test `assert first_Digit(123) == 1` would fail if the function returned `'1'` instead of `1`.  Therefore, it is better to keep the function returning the first digit as an integer.  If you want to return the first digit as a string, you can add another function or method that converts the integer to a string. For example, `def first_Digit_as_String(n): return str(first_Digit(n))`.  This way, you can have both integer and string versions of the function. 

In summary, the function `first_Digit(n)` returns the first digit of a given number as an integer, and works for both positive and negative numbers, and for numbers with multiple digits.  It is a simple and efficient function that can be used in a variety of applications.  For example, you can use it to find the first digit of a number in a list, or to determine if a number is positive or negative.  It is also useful in data processing and analysis applications, such as filtering out numbers that do not start with a certain digit