```
def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x == y + z) or (x == z + y) or (y == x + z) or (y == z + x) or (z == x + y) or (z == y + x):
            return True
        else:
            return False
    else:
        return False
```


This function first checks if all three numbers are integers. If they are, it then checks if one of the numbers is equal to the sum of the other two. If it finds a match, it returns True. If it doesn't find a match, it returns False. If any of the numbers are not integers, it returns False.