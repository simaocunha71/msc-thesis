```
def get_total_number_of_sequences(m, n):
    """
    Finds the number of possible sequences of length n,
    such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
    """
    if n == 1:
        return m
    else:
        return (m - 1) + get_total_number_of_sequences(m, n - 1)
```

Here are some test cases:

```python
assert get_total_number_of_sequences(10, 4) == 4
assert get_total_number_of_sequences(5, 2) == 2
assert get_total_number_of_sequences(3, 2) == 2
```

The function works as follows:

- If `n` is 1, the function returns `m` because there is only one possible sequence of length 1, which is just the number itself.
- Otherwise, the function returns `(m - 1) + get_total_number_of_sequences(m, n - 1)`. Here's why:

  - If the first element of the sequence is `m`, the number of possible sequences of length `n - 1` is `get_total_number_of_sequences(m, n - 1)`.
  - If the first element of the sequence is `m - 1`, the number of possible sequences of length `n - 1` is also `get_total_number_of_sequences(m, n - 1)`.
  - So, the total number of possible sequences is `(m - 1) + get_total_number_of_sequences(m, n - 1)`.

The time complexity of this function is O(n), and the space complexity is O(1).

```python
def get_total_number_of_sequences(m, n):
    """
    Finds the number of possible sequences of length n,
    such that each element is a positive integer and is greater than or equal to twice the previous element but less than or equal to m.
    """
    if