```
def is_decimal(s):
    try:
        float(s)
        return len(s.split('.')[1]) <= 2
    except ValueError:
        return False
```
This function uses a try-except block to attempt to convert the input string to a float. If the conversion is successful, it then checks if the length of the fractional part of the string (i.e., the part after the decimal point) is 2 or less. If both conditions are met, the function returns True, indicating that the input string is a decimal number with a precision of 2. If the conversion to float fails (i.e., the input string is not a valid decimal number), the function returns False.

The unit test `assert is_decimal('123.11')==True` ensures that the function correctly identifies decimal numbers with a precision of 2. For example, the input string '123.11' should return True because it has a precision of 2 (i.e., the fractional part is '11' and has a length of 2). On the other hand, the input string '123.111' should return False because it has a precision greater than 2. The function correctly handles these cases.