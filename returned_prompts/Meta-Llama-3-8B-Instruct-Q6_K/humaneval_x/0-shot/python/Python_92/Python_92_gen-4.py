```
def any_int(x, y, z):
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    if x + y == z or x + z == y or y + z == x:
        return True
    return False
```A:  def any_int(x, y, z):     if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):         return False     if x + y == z or x + z == y or y + z == x:         return True     return False
The function `any_int` checks if the input numbers `x`, `y`, and `z` are all integers. It then checks if one of the numbers is equal to the sum of the other two. If both conditions are met, the function returns `True`. If either condition is not met, the function returns `False`. The `isinstance` function is used to check if the input numbers are integers, and the `+` operator is used to calculate the sum of the numbers. The `or` operator is used to check if any of the conditions are met.