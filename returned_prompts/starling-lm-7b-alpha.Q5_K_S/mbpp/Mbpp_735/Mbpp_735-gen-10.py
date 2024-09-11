Here's a Python function to toggle the bits of the number except the first and the last bit:

```python
def toggle_middle_bits(n):
    # Shift the bits to the left by 1
    n = n << 1
    # Add the original number
    n += n >> 1
    # Toggle the bits
    n ^= n >> 1
    # Shift the bits to the right by 1
    n = n >> 1
    # Return the result
    return n
```

You can verify the function by running the provided assert statement:

```python
assert toggle_middle_bits(9) == 15
```

This will return `True` if the function is correct, and `False` otherwise.

```python
def toggle_middle_bits(n):
    # Shift the bits to the left by 1
    n = n << 1
    # Add the original number
    n += n >> 1
    # Toggle the bits
    n ^= n >> 1
    # Shift the bits to the right by 1
    n = n >> 1
    # Return the result
    return n

assert toggle_middle_bits(9) == 15
```

In this function, we first shift the bits of the number to the left by 1 using the `<<` operator. We then add the original number to the shifted number using the `+` operator. Next, we toggle the bits of the number using the `^` operator. After that, we shift the bits of the number to the right by 1 using the `>>` operator. Finally, we return the result.

The assert statement `assert toggle_middle_bits(9) == 15` checks if the function correctly toggles the bits of the number `9` and returns the expected result of `15`. If the function is correct, the assert statement will return `True`. Otherwise, it will return `False`.

Overall, this function provides a simple and efficient way to toggle the bits of a number except the first and the last bit.

```python
def toggle_middle_bits(n):
    # Shift the bits to the left by 1
    n = n