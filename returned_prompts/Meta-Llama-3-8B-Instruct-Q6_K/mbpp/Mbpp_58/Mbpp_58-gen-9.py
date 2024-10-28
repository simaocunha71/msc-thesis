```
def opposite_Signs(a, b):
    return (a>0)^(b>0)
```


The function uses the bitwise XOR operator (^) to check whether the two numbers have opposite signs. The expression (a>0)^(b>0) returns True if the signs are opposite and False if they are the same. 

This solution works because the XOR operator returns 1 if the inputs are different (both 1 or both 0) and 0 if they are the same (1 and 0 or 0 and 1). So, if the signs are opposite, the expression returns True, and if they are the same, it returns False. 

The unit test `assert opposite_Signs(1,-2) == True` also confirms this. When a is positive (1) and b is negative (-2), the function correctly returns True, indicating that the signs are opposite. 