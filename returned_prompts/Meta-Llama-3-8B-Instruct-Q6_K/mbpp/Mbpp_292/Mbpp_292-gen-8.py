```
def find(a, b):
    return a // b
```


This function uses Python's built-in integer division operator `//` which returns the quotient of the division of `a` by `b`, rounded down to the nearest integer. For example, `10 // 3` returns `3`. 

The provided unit test `assert find(10,3) == 3` ensures that the function is working correctly. 

The function can also handle division by zero by raising a ZeroDivisionError, which is the default behavior in Python. However, it's a good practice to add error handling for such cases to make the function more robust. Here's an example of how you can do it:

```
def find(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b
```


This version of the function will raise a ValueError with the message "Cannot divide by zero" when `b` is zero, instead of the default ZeroDivisionError. This can make the function more user-friendly and easier to debug. 