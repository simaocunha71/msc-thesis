```
def minimum(a, b):
    if a < b:
        return a
    else:
        return b
```


This function takes two numbers as input and returns the smaller one. It does this by comparing the two numbers and returning the one that is less than the other. If the two numbers are equal, it returns the first one. The function is tested with the unit test `assert minimum(1,2) == 1`, which checks if the function returns 1 when given 1 and 2 as input. This test passes because the function correctly returns the minimum value, which is 1 in this case. 