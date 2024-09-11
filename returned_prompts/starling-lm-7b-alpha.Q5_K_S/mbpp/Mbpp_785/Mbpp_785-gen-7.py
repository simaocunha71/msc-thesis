```
def tuple_str_int(s):
    return tuple(map(int, s.strip("()").split(",")))
```

Explanation:
To convert a tuple string to an integer tuple, you can follow these steps:
1. Remove the parentheses around the tuple string using the `strip("()")` method.
2. Split the tuple string by commas using the `split(",")` method.
3. Convert each string element to an integer using the `map(int, ...)` method.
4. Finally, use the `tuple()` function to convert the list of integers back to a tuple.

The `tuple_str_int` function in the provided solution follows these steps to convert a tuple string to an integer tuple.

For example, if you call `tuple_str_int("(7, 8, 9)")`, it will return `(7, 8, 9)` as expected.

Note: Make sure that the input tuple string is correctly formatted with parentheses and commas, and that all the elements are integers.




















































































```

```