```
def is_decimal(s):
    try:
        float(s)
        return len(s.split('.')[1]) <= 2
    except ValueError:
        return False
```
This function checks if the given string is a decimal number with a precision of 2. It first tries to convert the string to a float. If this conversion is successful, it then checks if the decimal part of the number has a length of 2 or less. If both checks are successful, it returns True. If the conversion to a float fails (which would happen if the string is not a decimal number), it returns False. 

The unit test `assert is_decimal('123.11')==True` is used to verify the correctness of the function. It checks if the string '123.11' is a decimal number with a precision of 2, which is True. 