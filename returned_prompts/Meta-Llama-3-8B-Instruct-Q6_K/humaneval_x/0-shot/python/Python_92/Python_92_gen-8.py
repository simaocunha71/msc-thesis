```
def any_int(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return (x == y + z) or (y == x + z) or (z == x + y)
```


The function `any_int` takes three arguments `x`, `y`, and `z`. It first checks if all three arguments are integers by using the `isinstance` function. If any of the arguments are not integers, it immediately returns `False`.

If all the arguments are integers, it then checks if one of the numbers is equal to the sum of the other two. It does this by checking if `x` is equal to `y + z`, or if `y` is equal to `x + z`, or if `z` is equal to `x + y`. If any of these conditions is true, it returns `True`. If none of these conditions are true, it returns `False`. 

This function will work correctly for all inputs, including the examples provided. It will return `True` for inputs where one of the numbers is equal to the sum of the other two, and all numbers are integers, and `False` for all other cases. 