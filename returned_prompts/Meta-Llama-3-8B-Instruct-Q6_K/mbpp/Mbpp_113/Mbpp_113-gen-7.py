```
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
```

The function `check_integer(s)` checks if a given string `s` represents an integer or not. It tries to convert the string into an integer using the `int(s)` function. If the conversion is successful, it returns `True`, meaning the string represents an integer. If the conversion fails (which would raise a `ValueError`), it returns `False`, meaning the string does not represent an integer.

The unit test `assert check_integer("python")==False` ensures that the function correctly identifies non-integer strings. In this case, the string "python" is not an integer, so the function should return `False`. The test passes because the function returns `False` for the input "python". 