```
def any_int(x, y, z):
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    return (x == y + z) or (x == z + y) or (y == x + z) or (y == z + x) or (z == x + y) or (z == y + x)
```
The function `any_int(x, y, z)` takes three numbers as arguments. It first checks if all the numbers are integers by using the `isinstance` function to check if each number is an instance of the `int` class. If any of the numbers is not an integer, the function returns `False`.

If all the numbers are integers, the function then checks if one of the numbers is equal to the sum of the other two by using a series of `or` conditions. If any of these conditions is true, the function returns `True`. If none of the conditions is true, the function returns `False`. This ensures that the function returns `True` only if one of the numbers is equal to the sum of the other two, and all numbers are integers. Otherwise, it returns `False`.