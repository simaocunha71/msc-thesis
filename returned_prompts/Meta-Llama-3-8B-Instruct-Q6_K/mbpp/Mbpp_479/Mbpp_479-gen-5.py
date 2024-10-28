```
def first_Digit(n):
    return int(str(n)[0])
```

The function `first_Digit` takes an integer `n` as input, converts it to a string, and then returns the first character of the string, which is the first digit of the number. The `int` function is used to convert the character back to an integer. For example, `first_Digit(123)` returns `1`. 

The unit test `assert first_Digit(123) == 1` ensures that the function works correctly.  If the function does not work correctly, the unit test will fail. 

This solution assumes that the input number is a positive integer and the first digit is the leftmost digit. If the input can be a negative number or a non-integer, the function will need to be modified accordingly. 

Note: The problem statement does not specify whether to consider negative numbers. For simplicity, let's assume that the input number is always positive. If the input can be negative, the function needs to handle it. For example, we can add a check to handle negative numbers and return the first digit of the absolute value of the number. 

Here is the modified function:
```
def first_Digit(n):
    n = abs(n)
    return int(str(n)[0])
```
This function first converts the absolute value of the number to a string and then returns the first character of the string, which is the first digit of the number.  This way, the function works correctly for both positive and negative numbers.  For example, `first_Digit(-123)` returns `1`.  The function still assumes that the input is an integer. If the input can be a non-integer, the function needs to be modified accordingly.  For example, we can add a check to handle non-integer inputs and return an error message or a special value.  Here is the modified function:
```
def first_Digit(n):
    if not isinstance(n, int):
        return "Error: Input is not an integer"
    n = abs(n)
    return int(str(n)[0])
```  This function checks if the input is an integer using the `isinstance` function. If the input is not an integer, it returns an error message. If the input is an integer, it converts the absolute value of the number to a string and then returns the first character of the string, which is the first digit of the number.  For example, `first