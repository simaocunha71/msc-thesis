```
def opposite_Signs(a, b):
    return ((a > 0) ^ (b > 0))
```


This function uses the bitwise XOR operator (^) to check if the signs of the two integers are opposite. It does this by checking if the sign of the first integer is different from the sign of the second integer. If they are different, it returns True, meaning the signs are opposite. If they are the same, it returns False, meaning the signs are not opposite. The unit test `assert opposite_Signs(1,-2) == True` shows that this function works correctly. 