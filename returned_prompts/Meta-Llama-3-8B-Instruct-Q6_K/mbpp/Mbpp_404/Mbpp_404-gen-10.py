```
def minimum(a, b):
    return min(a, b)
```

This function uses the built-in Python function `min()` to find the minimum of two numbers. The `min()` function returns the smallest item in an iterable or the smallest of two or more arguments. In this case, we are passing two arguments, `a` and `b`, to the `min()` function. The function returns the minimum of `a` and `b`. This solution is simple and efficient. 

The unit test `assert minimum(1,2) == 1` ensures that the function returns the correct result for the input values 1 and 2. 

Note: The `min()` function will work correctly even if the input values are not numbers. For example, `min('a', 'b')` will return 'a'. If you want to ensure that the input values are numbers, you can add a type check at the beginning of the function. For example:
```
def minimum(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Input values must be numbers")
    return min(a, b)
```  This will raise a TypeError if the input values are not numbers. 