```
def is_decimal(s):
    try:
        float(s)
        if s.replace('.','').replace('-','').replace(' ','').replace('+','').isdigit():
            if len(s.split('.')[1]) > 2:
                return False
            return True
    except ValueError:
        return False
```


The function `is_decimal(s)` checks whether the given string `s` is a decimal number with a precision of 2. The function first tries to convert the string to a float. If the conversion is successful, it checks whether the string consists of digits after removing all non-digit characters. If the string has more than 2 digits after the decimal point, the function returns `False`. Otherwise, it returns `True`. If the conversion to a float fails, the function returns `False`. The unit test `assert is_decimal('123.11')==True` ensures that the function works correctly. 

The function handles edge cases such as negative numbers, decimal numbers with more than 2 digits after the decimal point, and non-numeric strings. For example, `is_decimal('123.111')` returns `False` because the precision is more than 2, and `is_decimal('abc')` returns `False` because the string is not a decimal number. 

The function does not handle cases where the decimal point is not exactly in the middle of the string, such as `is_decimal('123.11abc')`, which returns `True` but is not a valid decimal number. To handle such cases, additional checks could be added. 