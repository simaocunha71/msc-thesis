```
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x == y + z or y == x + z or z == x + y:
            return True
    return False
```


This function checks if the input values are integers and if one of them is equal to the sum of the other two. If both conditions are met, the function returns True. Otherwise, it returns False. 

The function uses the isinstance() function to check if the input values are integers. It also uses the equality operators (==) to check if one of the values is equal to the sum of the other two. 

Note that the function does not check if the sum is equal to zero, as this is not specified in the problem statement. If you want to exclude the case where the sum is equal to zero, you can add an additional condition to the if statement. 

Here is the updated function:

```
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x != y + z and y != x + z and z != x + y:
            return True
    return False
```


This updated function returns True only if one of the values is equal to the sum of the other two, and all values are integers. It returns False in any other cases. 