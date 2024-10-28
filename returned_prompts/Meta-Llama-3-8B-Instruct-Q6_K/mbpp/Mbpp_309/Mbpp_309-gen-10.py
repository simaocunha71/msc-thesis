```
def maximum(a, b):
    if a >= b:
        return a
    else:
        return b
```
This function takes two arguments `a` and `b` and returns the maximum of the two. It does this by comparing the two numbers and returning the larger one. The unit test `assert maximum(5,10) == 10` ensures that the function is working correctly. 

Note: This function will return the same value if the input numbers are equal, which may or may not be the desired behavior depending on the specific use case. If you want to return the first input if they are equal, you can modify the function to return `a` instead of `b` in the `else` clause. 

Also, this function does not handle the case where the input is not a number. In a real-world application, you would want to add error checking to handle this case. For example, you could use a `try`/`except` block to catch any `TypeError` exceptions that are raised when the function tries to compare the input values. 

Here's an example of how you could modify the function to handle this case:

```
def maximum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    if a >= b:
        return a
    else:
        return b
``` 