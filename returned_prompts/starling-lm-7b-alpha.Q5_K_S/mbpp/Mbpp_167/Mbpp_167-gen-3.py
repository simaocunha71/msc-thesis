Here's a Python function that accomplishes this task:

```python
def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2 ** (n - 1).bit_length()
```

To test this function with the given assertion, we can use the following code:

```python
assert next_power_of_2(0) == 1
```

This function works by taking the bit length of `n - 1`, which is the number of bits needed to represent `n` in binary, and then raising 2 to that power. The `bit_length()` method is a built-in Python function that returns the number of bits needed to represent an integer in binary.

For example, if `n` is 0, the bit length of `n - 1` is 1, so the function returns 2 raised to the power of 1, which is 2.

Here's a breakdown of how the function works for different values of `n`:

- If `n` is 0, the bit length of `n - 1` is 1, so the function returns 2 raised to the power of 1, which is 2.
- If `n` is 1, the bit length of `n - 1` is 0, so the function returns 2 raised to the power of 0, which is 1.
- If `n` is 2, the bit length of `n - 1` is 1, so the function returns 2 raised to the power of 1, which is 2.
- If `n` is 3, the bit length of `n - 1` is 2, so the function returns 2 raised to the power of 2, which is 4.
- If `n` is 4, the bit length of `n - 1` is 2, so the function returns 2 raised to the power of 2, which is 4.
- If `n` is 5, the bit length of `n - 1` is 3, so the function returns 2 raised to the power of 3, which is 8.

This pattern continues for all positive values of