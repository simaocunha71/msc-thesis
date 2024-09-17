```
def opposite_Signs(a, b):
    if ((a > 0 and b < 0) or (a < 0 and b > 0)):
        return True
    else:
        return False
```


The unit test `assert opposite_Signs(1,-2) == True` helps in understanding the problem better. It means the function should return `True` if the signs of the given two integers are opposite, and `False` if they are the same. We can use this to write the function. The function checks whether the given two integers have opposite sign or not by comparing the signs of the numbers. If the signs are opposite, it returns `True`, else it returns `False`. The unit test `assert opposite_Signs(1,-2) == True` passes for this function. 