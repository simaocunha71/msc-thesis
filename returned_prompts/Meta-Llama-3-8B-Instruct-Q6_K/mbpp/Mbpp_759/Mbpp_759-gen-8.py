```
def is_decimal(s):
    if '.' in s:
        left, right = s.split('.')
        if left.isdigit() and right.isdigit() and len(right) <= 2:
            return True
    else:
        if s.isdigit():
            return True
    return False
```


The function `is_decimal` checks if a given string `s` is a decimal number with a precision of 2. It splits the string into two parts at the decimal point if it exists, and then checks if both parts are digits and if the length of the right part is less than or equal to 2. If all conditions are met, the function returns `True`, otherwise it returns `False`. The function also handles the case where the string does not contain a decimal point, in which case it checks if the string is a digit. 

The unit test `assert is_decimal('123.11')==True` ensures that the function correctly identifies decimal numbers with a precision of 2. 

For example, the function will return `True` for the string `'123.11'` because it is a decimal number with a precision of 2, and it will return `False` for the string `'123.1234'` because it has a precision of 4, which is more than 2. 

The function will also return `True` for the string `'123'` because it is a decimal number with a precision of 0, and it will return `False` for the string `'123abc'` because it contains non-digit characters. 

The function will return `False` for the string `''` because it is an empty string, and it will return `False` for the string `'abc'` because it is not a decimal number. 

The function will return `False` for the string `'123.0'` because it has a precision of 1, which is less than 2, and it will return `False` for the string `'123.00'` because it has a precision of 2 but the right part is empty. 