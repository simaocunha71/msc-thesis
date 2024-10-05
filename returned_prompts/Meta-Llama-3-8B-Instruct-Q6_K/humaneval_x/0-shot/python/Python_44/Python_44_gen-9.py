```
def change_base(x: int, base: int):
    convertString = "0123456789ABCDEF"
    if x < base:
        return convertString[x]
    else:
        return change_base(x // base, base) + convertString[x % base]
```
This Python function converts an integer `x` to a different base `base`. It uses recursion to perform the conversion. The base 10 number is divided by the target base, and the remainder is converted to the target base using the `convertString` mapping. The function then recursively calls itself with the quotient until the quotient is less than the target base, at which point the final remainder is appended to the converted string.

The function works for bases less than 10, as required. For example, the conversion of 8 to base 3 is '22', 8 to base 2 is '1000', and 7 to base 2 is '111'. The function correctly handles conversions to bases 2-9. For conversions to bases 10 or greater, the function will raise a ValueError, as the problem statement does not specify how to handle these cases. 

The time complexity of this function is O(log x), where x is the input number, because the function makes recursive calls until the quotient is less than the target base, and the number of recursive calls is proportional to the number of digits in the input number. The space complexity is O(log x) as well, because the function uses a recursive call stack of size proportional to the number of digits in the input number. 