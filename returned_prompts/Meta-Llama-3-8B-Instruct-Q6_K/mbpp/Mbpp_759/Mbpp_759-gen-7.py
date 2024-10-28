```
def is_decimal(s):
    try:
        float(s)
        return len(s.split('.')[1]) <= 2
    except ValueError:
        return False
```



The problem is asking you to create a function that checks if a given string is a decimal number with a precision of 2. 

The provided unit test `assert is_decimal('123.11')==True` suggests that the function should return `True` for strings like '123.11' and `False` for strings that are not decimal numbers or have a precision greater than 2.

Here's a Python function that solves the problem:

```
def is_decimal(s):
    try:
        float(s)
        return len(s.split('.')[1]) <= 2
    except ValueError:
        return False
```

This function first tries to convert the string to a float. If the conversion is successful, it splits the string at the decimal point and checks if the length of the second part (i.e., the part after the decimal point) is less than or equal to 2. If the conversion fails (i.e., the string is not a decimal number), the function returns `False`. 

For example, `is_decimal('123.11')` returns `True` because the string is a decimal number with a precision of 2. On the other hand, `is_decimal('123.111')` returns `False` because the string has a precision greater than 2. 

The unit test `assert is_decimal('123.11')==True` also passes with this function. 





```
def is_decimal(s):
    if '.' in s:
        if len(s.split('.')[1]) > 2:
            return False
    try:
        float(s)
        return True
    except ValueError:
        return False
```

This function is a bit more robust, as it checks if the string contains a decimal point before trying to convert it to a float. This way, it can correctly handle strings that are not decimal numbers, even if they don't contain a decimal point. For example, `is_decimal('123abc')` returns `False` because the string is not a decimal number, even though it doesn't contain a decimal point.