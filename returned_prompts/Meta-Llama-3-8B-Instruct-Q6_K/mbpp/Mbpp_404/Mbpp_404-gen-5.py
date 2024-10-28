```
def minimum(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a
```


This function takes two numbers as arguments, a and b, and returns the minimum of the two. If a is less than b, it returns a. If b is less than a, it returns b. If a and b are equal, it also returns a. The unit test `assert minimum(1,2) == 1` ensures that the function works correctly.