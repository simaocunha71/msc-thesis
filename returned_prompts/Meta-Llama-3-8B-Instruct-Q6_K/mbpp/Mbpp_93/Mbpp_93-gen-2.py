```
def power(a, b):
    return a ** b
```



The problem is asking you to create a function that calculates the value of 'a' to the power 'b'. This is a basic mathematical operation that can be achieved using the ** operator in Python.

The unit test provided, `assert power(3,4) == 81`, helps to clarify the problem by showing that the function should return the result of the power operation. For example, `power(3,4)` should return `3 ** 4 = 81`.

Here is a simple Python function that solves the problem:
```
def power(a, b):
    return a ** b
```
This function takes two arguments, `a` and `b`, and returns the result of `a` to the power `b`. For example, `power(3,4)` would return `81`, which is the result of `3 ** 4`. The function can handle any positive integer values for `a` and `b`, but it will raise a `ValueError` if `b` is a negative integer or a non-integer. If you want to handle negative integers or non-integer values, you would need to add additional logic to the function.