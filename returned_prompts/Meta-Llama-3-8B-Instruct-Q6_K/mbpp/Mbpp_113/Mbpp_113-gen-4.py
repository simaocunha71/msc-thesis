```
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
``` 
The function `check_integer` takes a string `s` as an argument and checks if it can be converted to an integer. If the conversion is successful, it returns `True`; otherwise, it returns `False`. The `try` block attempts to convert the string to an integer using `int(s)`. If this is successful, the function returns `True`. If a `ValueError` is raised during the conversion (which would happen if the string does not represent a valid integer), the `except` block is executed, and the function returns `False`. The unit test `assert check_integer("python")==False` ensures that the function correctly identifies non-integer strings. 

Note: The function does not check if the integer is within a certain range or not. It simply checks if the string can be converted to an integer or not. If you need to check for a specific range, you would need to modify the function accordingly. 

Also, the function does not handle the case where the input string is empty. Depending on your requirements, you might want to add a check for this case and return `False` if the string is empty. 

Finally, the function does not handle the case where the input string is a signed integer (i.e., it starts with a minus sign). Depending on your requirements, you might want to add a check for this case and return `True` if the string is a signed integer. 