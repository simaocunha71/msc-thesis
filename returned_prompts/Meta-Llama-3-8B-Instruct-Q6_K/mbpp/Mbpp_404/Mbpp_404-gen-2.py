```
def minimum(a, b):
    if a < b:
        return a
    else:
        return b
```


Explanation:
The function takes two numbers a and b as input and returns the minimum of the two. It does this by comparing the two numbers and returning the smaller one. The unit test `assert minimum(1,2) == 1` ensures that the function works correctly. This function is more straightforward and easier to read than the original solution provided in the problem description. It also avoids the use of the built-in min function, as requested in the problem description.