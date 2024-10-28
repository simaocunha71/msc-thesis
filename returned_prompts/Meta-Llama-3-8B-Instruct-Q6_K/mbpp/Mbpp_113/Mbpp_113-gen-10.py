```
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
```

The provided unit test `assert check_integer("python")==False` suggests that the function should return `False` for non-integer strings. 

The function `check_integer` takes a string `s` as input and tries to convert it to an integer using the `int()` function. If the conversion is successful, the function returns `True`, indicating that the string represents an integer. If the conversion raises a `ValueError` (which it would for non-integer strings), the function returns `False`, indicating that the string does not represent an integer. 