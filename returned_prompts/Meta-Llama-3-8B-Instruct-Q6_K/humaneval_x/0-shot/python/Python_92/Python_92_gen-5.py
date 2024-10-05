```
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return x + y == z or x + z == y or y + z == x
    else:
        return False
```


This function first checks if all the input numbers are integers using the `isinstance` function. If they are, it then checks if the sum of any two numbers is equal to the third number. If it finds a match, it returns `True`. If it doesn't find a match, it returns `False`. If the input numbers are not integers, it also returns `False`.