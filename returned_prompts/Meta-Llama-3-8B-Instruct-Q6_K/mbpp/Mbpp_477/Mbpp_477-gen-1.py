You can use the built-in lower() function in Python to convert a string to lowercase. The function name is misleading, as it doesn't check if the string is already in lowercase, it simply converts it to lowercase.

Here's how you can use it:

```Python
def is_lower(s):
    return s.lower()
```

This function will take a string as an input, convert it to lowercase and return the result. The unit test you provided, `assert is_lower("InValid") == "invalid"`, will pass with this function. 

However, based on the function name `is_lower`, I assume you want a function that checks if a string is already in lowercase and returns the same string if it is, and converts it to lowercase otherwise. Here's how you can implement that:

```Python
def is_lower(s):
    if s.islower():
        return s
    else:
        return s.lower()
```

This function will check if the input string `s` is already in lowercase using the islower() function. If it is, the function will return the same string. If it's not, the function will convert the string to lowercase using the lower() function and return the result. The unit test you provided will still pass with this function. 

However, please note that this function name is still misleading, as it doesn't really check if the string is in lowercase, it checks if it's already in lowercase and returns the same string if it is, and converts it to lowercase otherwise. A more accurate name for this function could be `lower_if_necessary` or `to_lowercase_if_needed`. 