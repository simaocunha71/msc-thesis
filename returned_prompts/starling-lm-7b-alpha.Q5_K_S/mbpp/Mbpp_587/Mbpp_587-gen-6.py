```python
def list_tuple(my_list):
    """
    Convert a list to a tuple.

    Parameters:
    my_list: a list of integers

    Returns:
    a tuple of the same list in the same order
    """
    return tuple(my_list)
```

Explanation:

The function `list_tuple` takes a list as an argument and converts the list to a tuple using Python's built-in `tuple` function. The function then returns the tuple.

To test the function, we can use the `assert` statement to check if the result of `list_tuple` on a sample list `[5, 10, 7, 4, 15, 3]` is equal to the expected tuple `(5, 10, 7, 4, 15, 3)`.

The `assert` statement is used to verify that a condition is true. In this case, the condition is that the result of `list_tuple` is equal to the expected tuple. If the condition is not met, an `AssertionError` will be raised.

Overall, this solution demonstrates how to convert a list to a tuple in Python using the `tuple` function and how to test the function using the `assert` statement.

Here are some additional tips for using the `assert` statement and debugging code in Python:

1. **Use assertions for testing and debugging**: Assertions are primarily used for testing and debugging purposes. They are not meant to be used in production code, as they can cause the program to crash if the assertion condition is not met.

2. **Choose meaningful error messages**: When using assertions, it's important to choose meaningful error messages that describe the expected condition and the actual condition. This helps in identifying and resolving issues more quickly during testing and debugging.

3. **Turn off assertions in production**: In production code, it's recommended to turn off assertions to prevent the program from crashing unexpectedly. This can be done by adding the `-O` flag when running the Python interpreter.

4. **Use assertions for validating assumptions**: Assertions are useful for validating assumptions about the state of the program. By using assertions, you can ensure