```
def min_of_three(a,b,c):
    if(a<b):
        if(a<c):
            return a
        else:
            return c
    else:
        if(b<c):
            return b
        else:
            return c
```

Here is a Python function that finds the minimum of three numbers. It compares the numbers and returns the smallest one. The assert statement is used to check whether the function is working correctly.

To use the function, you can call it with three numbers as arguments. For example, `min_of_three(10, 20, 0)` will return `0`, as `0` is the smallest number in the list.

The function compares the numbers using if-else statements. It first compares `a` and `b`, and if `a` is smaller, it checks if `a` is also smaller than `c`. If `a` is smaller than `c`, it returns `a`. Otherwise, it returns `c`. If `b` is smaller, it returns `b`. This process is repeated for the other combinations of numbers, ensuring that the smallest number is always returned.

By using this function, you can easily find the minimum of three numbers in your Python program.

```python
# Testing the function
assert min_of_three(10, 20, 0) == 0  # True
```

This test case checks whether the function correctly returns the minimum number when given the arguments `10`, `20`, and `0`. The assert statement checks if the function's result is equal to the expected result (`0` in this case). If the function's result is not equal to the expected result, an error will be raised. Otherwise, the test case will pass.

Overall, this function and test case ensure that the function can correctly find the minimum of three numbers in Python.
```

```
