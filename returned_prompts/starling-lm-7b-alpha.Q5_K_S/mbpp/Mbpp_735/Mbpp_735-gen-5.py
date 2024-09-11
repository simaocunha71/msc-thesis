Here's a Python function to toggle bits of the number except the first and the last bit:

```python
def toggle_middle_bits(n):
    return (n | (n >> 1) | (n >> 2) | (n >> 4) | (n >> 8) | (n >> 16)) ^ (n | (n << 1) | (n << 2) | (n << 4) | (n << 8) | (n << 16))
```

Explanation:
The function `toggle_middle_bits` takes an integer `n` as input and performs bitwise operations to toggle all the bits except the first and the last bit. 

To achieve this, the function uses bitwise OR and bitwise XOR operations. The bitwise OR operation `|` is used to set the bits that are common to both the original number `n` and the shifted versions of `n`. The bitwise XOR operation `^` is used to toggle the bits that are common to both the original number and the shifted versions of `n`. 

The function first shifts the bits of `n` to the right by 1, 2, 4, 8, and 16 positions, and then performs a bitwise OR operation with `n` to set the common bits. Then, it shifts the bits of `n` to the left by 1, 2, 4, 8, and 16 positions, and performs a bitwise OR operation with `n` to set the common bits. 

Finally, the function performs a bitwise XOR operation between the two sets of common bits to toggle the middle bits of the original number `n`. 

The function returns the toggled number as the output. 

In the provided assertion `assert toggle_middle_bits(9) == 15`, the function is tested with the input `9`, and it is expected to return `15`. 

This function can be used to toggle bits of a number while preserving the first and the last bit.

```python
def toggle_middle_bits(n):
    return (n | (n >> 1) | (n >> 2) | (n >> 4) | (n >> 8) | (n