Here is a Python solution that uses a list comprehension to generate the sequence of numbers and then joins them into a string with spaces in between:
```python
def string_sequence(n: int) -> str:
    return ' '.join(str(i) for i in range(n + 1))
```
Here's an explanation of the code:

1. `range(n + 1)`: This generates a sequence of numbers from 0 to `n` inclusive.
2. `str(i) for i in range(n + 1)`: This is a generator expression that converts each number in the sequence to a string.
3. `' '.join(...)`: This joins the strings together with spaces in between using the `join` method.

You can test this function with the examples you provided:
```python
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```A
def string_sequence(n: int) -> str:
    return ' '.join(map(str, range(n + 1)))
```
This solution uses the `map` function to convert each number in the sequence to a string, and then joins the resulting strings together with spaces in between.

Here's an explanation of the code:

1. `range(n + 1)`: This generates a sequence of numbers from 0 to `n` inclusive.
2. `map(str, ...)`: This applies the `str` function to each number in the sequence, converting it to a string.
3. `' '.join(...)`: This joins the strings together with spaces in between using the `join` method.

You can test this function with the examples you provided:
```python
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
```A
def string_sequence(n: int) -> str:
    return ' '.join(map(str, range(n + 1)))
```
This solution uses the `map` function to convert each number in the sequence to a string, and then joins the resulting strings together with spaces in between.

Here's an explanation of the code:

1. `range(n + 1)`: This generates a sequence of numbers from 0 to `n` inclusive.
2. `map(str, ...)`: This applies the `str` function to each number in the sequence, converting it to a string