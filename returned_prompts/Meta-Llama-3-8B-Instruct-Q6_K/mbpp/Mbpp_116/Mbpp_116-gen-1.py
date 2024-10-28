You can use the built-in function `int` to convert the tuple into an integer. Here's a Python function that does this:

```Python
def tuple_to_int(t):
    return int(''.join(map(str, t)))
```
This function works by first converting each integer in the tuple into a string using the `map` function. It then joins these strings together into a single string using the `join` function. Finally, it converts this string into an integer using the `int` function.

The unit test `assert tuple_to_int((1,2,3))==123` ensures that the function works correctly. It checks that the function returns the integer `123` when given the tuple `(1,2,3)`. This test passes because the function correctly converts the tuple into an integer. 