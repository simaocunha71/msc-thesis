```
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        return x + y == z or x + z == y or y + z == x
    else:
        return False
```


Example:
```
print(any_int(5, 2, 7))  # True
print(any_int(3, 2, 2))  # False
print(any_int(3, -2, 1))  # True
print(any_int(3.6, -2.2, 2))  # False
```


This function first checks if all three numbers are integers using the `isinstance` function. If they are, it then checks if one of the numbers is equal to the sum of the other two using the logical or operator (`or`). If the numbers are not all integers, it returns `False`. 

The function will return `True` if one of the numbers is equal to the sum of the other two, and all numbers are integers. Otherwise, it will return `False`. 
Please note that you can also use `abs()` function to make the condition more robust, in case the numbers are negative. For example:
```
return x + y == abs(z) or x + z == abs(y) or y + z == abs(x)
``` 
This will ensure that the function works correctly even if the numbers are negative. 