```
def maximum(a, b):
    return max(a, b)
```


The problem is asking to create a function that finds the maximum of two numbers. The function should take two arguments and return the maximum value.

In Python, the built-in function `max()` can be used to find the maximum of a list of numbers. Since we only need to find the maximum of two numbers, we can use the `max()` function with two arguments.

Here's the solution:
```
def maximum(a, b):
    return max(a, b)
```
This function takes two arguments `a` and `b`, and returns the maximum value between the two. The unit test `assert maximum(5,10) == 10` ensures that the function works correctly. When we call the function with the arguments `5` and `10`, it returns `10`, which is the maximum value.