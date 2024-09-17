```
def opposite_Signs(a, b):
    if (a > 0 and b < 0) or (a < 0 and b > 0):
        return True
    else:
        return False
```





Python code to check whether the given two integers have opposite sign or not.

The function `opposite_Signs(a, b)` takes two integer arguments `a` and `b`. It checks if one number is positive and the other is negative, or vice versa. If the condition is met, it returns `True`; otherwise, it returns `False`.

The unit test `assert opposite_Signs(1,-2) == True` ensures the function works correctly for the given example.

Here's a breakdown of the code:

1. `if (a > 0 and b < 0) or (a < 0 and b > 0):` This line checks if `a` is positive and `b` is negative, or if `a` is negative and `b` is positive. The `or` operator is used to combine the two conditions.
2. `return True` If the condition is met, the function returns `True`.
3. `else: return False` If the condition is not met, the function returns `False`.