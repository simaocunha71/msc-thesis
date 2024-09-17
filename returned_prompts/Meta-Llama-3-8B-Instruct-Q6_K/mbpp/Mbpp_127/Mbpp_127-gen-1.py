```
def multiply_int(a, b):
    return a * b
```


This function takes two integers `a` and `b` as input, and returns their product. The unit test `assert multiply_int(10,20)==200` ensures that the function works correctly for the given inputs. The multiplication operation is implemented using the `*` operator in Python.  This function is a simple and straightforward implementation of the multiplication operation. It does not handle any potential errors, such as division by zero or overflow, which might occur for large input values. In a real-world application, you would need to add error handling to ensure the function behaves correctly in all scenarios.