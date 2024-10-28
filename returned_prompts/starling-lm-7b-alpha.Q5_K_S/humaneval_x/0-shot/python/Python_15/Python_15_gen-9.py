
Here's a Python function that takes an integer `n` as input and returns a string containing the numbers from 0 to `n` (inclusive), separated by spaces:

```python
def string_sequence(n: int) -> str:
    return " ".join(map(str, range(n + 1)))
```

This function uses the `range()` function to generate a sequence of numbers from 0 to `n`, and then converts each number to a string using `map()`. The resulting list of strings is joined together with spaces using the `join()` method. The output is the desired string of numbers.

For example, if you call `string_sequence(0)`, it will return the string `'0'`. If you call `string_sequence(5)`, it will return the string `'0 1 2 3 4 5'`.

You can use this function to generate a string representation of any sequence of numbers from 0 to a given integer `n`.

```python
result = string_sequence(5)
print(result)  # Output: '0 1 2 3 4 5'
```

Note: The `join()` method is a built-in Python method that concatenates a list of strings with a specified delimiter. In this case, the delimiter is a space character (' ').

```python
def string_sequence(n: int) -> str:
    return " ".join(map(str, range(n + 1)))
```

This code snippet defines a function called `string_sequence` that takes a single integer argument `n`. The function uses the `map()` function to convert each number in the range from 0 to `n` (inclusive) to a string. The resulting list of strings is joined together with spaces using the `join()` method, and the output is the desired string representation of the sequence of numbers.

You can use this function to generate a string representation of any sequence of numbers from 0 to a given integer `n`. For example, if you call `string_sequence(5)`, it will return the string `'0 1 2 3 4 5'`.

```python
result = string_sequence(5)
