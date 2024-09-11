"""
Here's a simple function that checks if a string represents an integer or not:
"""

def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# test cases
print(check_integer("python"))  # False
print(check_integer("123"))     # True
print(check_integer("123abc"))  # False






"""
In this function, we try to convert the string to an integer using the int() function. If the conversion is successful, it means that the string represents an integer, and the function returns True. Otherwise, if the conversion fails and raises a ValueError exception, it means that the string does not represent an integer, and the function returns False.

We use the try-except block to catch the ValueError exception, which allows us to handle the exception gracefully and return the appropriate result.
"""

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

``