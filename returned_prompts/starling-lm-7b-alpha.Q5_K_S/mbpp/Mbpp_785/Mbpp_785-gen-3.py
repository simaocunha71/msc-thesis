```
def tuple_str_int(s):
    return tuple(map(int, s.split(',')))
```

Explanation:
The function `tuple_str_int` takes a string `s` as input and uses the `split` method to split the string at each comma, creating a list of strings. Then, the `map` function is used to apply the `int` function to each string in the list, converting them to integers. Finally, the `tuple` function is used to convert the resulting list of integers back into a tuple.

To test the function, you can use the `assert` statement to check if the function returns the expected result when given the string `"(7, 8, 9)"`.

This solution demonstrates how to convert a string representation of a tuple into an actual tuple of integers using Python's built-in functions and methods.

Here's an example of how you can use the `tuple_str_int` function:
```python
result = tuple_str_int("(7, 8, 9)")
print(result)  # Output: (7, 8, 9)
```

This will print the tuple `(7, 8, 9)`, which is the result of converting the string `"(7, 8, 9)"` to a tuple of integers using the `tuple_str_int` function.

Overall, the `tuple_str_int` function provides a convenient way to convert a tuple string to an integer tuple in Python.

```

```

```python
def tuple_str_int(s):
    return tuple(map(int, s.split(',')))
```

This Python function `tuple_str_int` takes a string `s` as input and converts it into a tuple of integers. Here's a step-by-step explanation of how it works:

1. The `split(',')` method is used on the input string `s` to split it at each comma, creating a list of strings. Each string in the list represents an integer in the original tuple. For example, if the input string is `"(7, 8, 9)"` the resulting list