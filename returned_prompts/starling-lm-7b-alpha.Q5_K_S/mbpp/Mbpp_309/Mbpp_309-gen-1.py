Here's a Python function that finds the maximum of two numbers:

```python
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
```

You can then use the `assert` statement to verify that this function correctly returns the maximum of `5` and `10`:

```python
assert maximum(5, 10) == 10
```

When you run this code, the `assert` statement will check if the expression `maximum(5, 10) == 10` is true. If it is true, the `assert` statement will do nothing. However, if the expression is false, an `AssertionError` will be raised, indicating that there is an error in the code.

In this case, since the function correctly returns the maximum of `5` and `10` as `10`, the `assert` statement will not raise an error.

Here's a step-by-step explanation of the code:

1. The `maximum` function takes two arguments, `a` and `b`. These arguments represent the two numbers for which we want to find the maximum.
2. Inside the function, an `if` statement is used to check if `a` is greater than `b`. If this condition is true, it means that `a` is the maximum number, so the function returns `a`.
3. If the condition in the `if` statement is false, it means that `b` is the maximum number, so the function returns `b`.
4. The `assert` statement is used to verify that the `maximum` function correctly returns the maximum of `5` and `10`. If the expression `maximum(5, 10) == 10` is true, the `assert` statement does nothing. Otherwise, an `AssertionError` is raised, indicating that there is an error in the code.

By using an `assert` statement and testing the function with different inputs, you can ensure that the function is working correctly and returning the expected maximum value.
```

```python
def maximum(a, b):
    if a > b:
        return a
    else:
        return b

assert maximum(5, 10