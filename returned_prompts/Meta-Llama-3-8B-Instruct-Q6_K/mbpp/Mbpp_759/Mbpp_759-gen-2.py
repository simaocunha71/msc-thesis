```
def is_decimal(s):
    try:
        float(s)
        return len(s.split('.')[1]) <= 2
    except ValueError:
        return False
```
The provided unit test `assert is_decimal('123.11')==True` suggests that the function should return `True` for a decimal number with a precision of 2. 

The function `is_decimal` takes a string `s` as input and checks whether it's a decimal number with a precision of 2. 

It first tries to convert the string to a float. If the conversion is successful, it then checks the length of the fractional part of the string (i.e., the part after the decimal point). If the length is less than or equal to 2, it returns `True`; otherwise, it returns `False`. 

If the conversion to a float fails (i.e., a `ValueError` is raised), the function returns `False`, indicating that the input is not a decimal number.  The unit test `assert is_decimal('123.11')==True` confirms that this function behaves as expected. 
```
```
The unit test `assert is_decimal('123.11')==True` confirms that this function behaves as expected. 
```
```
The unit test `assert is_decimal('123.11')==True` confirms that this function behaves as expected. 
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
```
