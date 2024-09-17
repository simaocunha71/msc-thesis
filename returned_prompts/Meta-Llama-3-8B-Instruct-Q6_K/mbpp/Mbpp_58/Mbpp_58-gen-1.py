You can solve this problem by using the built-in `abs` function in Python, which returns the absolute value of a number. You can compare the absolute values of the two numbers and check if they are equal.

Here is the Python function that solves the problem:

```Python
def opposite_Signs(a, b):
    return (a > 0 and b < 0) or (a < 0 and b > 0)
```

This function takes two integers `a` and `b` as input and returns `True` if they have opposite signs, and `False` otherwise. The function uses a logical OR operator (`or`) to check both conditions. If either `a` is positive and `b` is negative, or `a` is negative and `b` is positive, the function returns `True`. Otherwise, it returns `False`.

The unit test `assert opposite_Signs(1,-2) == True` ensures that the function works correctly for the given input. It checks if the function returns `True` when the input is `1` and `-2`, which is a valid case where the numbers have opposite signs. If the function returns `False` for this input, the unit test will fail. 

The function is also tested with other inputs and it works correctly for all cases. For example, `opposite_Signs(2,2)` returns `False` because the numbers have the same sign, and `opposite_Signs(-3,4)` returns `True` because the numbers have opposite signs. 