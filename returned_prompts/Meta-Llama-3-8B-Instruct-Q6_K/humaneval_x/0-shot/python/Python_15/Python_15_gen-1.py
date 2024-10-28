You can solve this problem by using a list comprehension to generate the sequence of numbers and then joining them with spaces to form a string. Here is the solution:

```python
def string_sequence(n: int) -> str:
    return ' '.join(str(i) for i in range(n + 1))
```

Here's how it works:

1. The `range(n + 1)` generates a sequence of numbers from 0 to `n` inclusive.
2. The `str(i) for i in range(n + 1)` is a generator expression that converts each number in the sequence to a string.
3. The `' '.join(...)` method joins the string representations of the numbers with spaces in between.
4. The resulting string is returned by the function.

You can test this function with the examples you provided:

```python
print(string_sequence(0))  # Output: '0'
print(string_sequence(5))  # Output: '0 1 2 3 4 5'
``` 