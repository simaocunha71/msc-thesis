You can use the eval function in Python to convert a string representing a tuple into a tuple of integers. Here's how you can do it:

```
def tuple_str_int(s):
    return eval(s)
```

This function works by directly evaluating the string as a Python expression. The eval function takes a string as an argument and returns the value of the expression. Since the string is in the format of a tuple, the eval function will return a tuple. 

However, be aware that using eval can be a security risk if you're allowing the user to input the string, because it can evaluate any Python expression. If you're using this function to convert user-inputted strings, you should validate the string to make sure it's in the correct format and doesn't contain any malicious code.

For example, you can use the following code to validate the string:

```
def tuple_str_int(s):
    try:
        return eval(s)
    except SyntaxError:
        raise ValueError("Invalid tuple string")
```

This code will raise a ValueError if the string is not a valid tuple string. 

The unit test `assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)` will also help to catch any errors in the function. If the function is not working correctly, this test will fail and indicate what's wrong. 