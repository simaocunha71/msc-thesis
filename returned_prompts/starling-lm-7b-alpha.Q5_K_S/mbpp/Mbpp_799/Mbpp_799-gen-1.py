```
def left_rotate(num, d):
    return (num << d) | (num >> (32 - d))
```

Explanation:

Here's one way to do it:

```python
def left_rotate(num, d):
    return (num << d) | (num >> (32 - d))
```
This function takes a number `num` and an amount of rotation `d`. It rotates the bits of `num` to the left by `d` places.

To rotate the bits to the left, we use the left shift operator `<<` to shift the bits `d` places to the left. The left shift operator copies each bit into the next position, effectively moving the bits to the left.

However, because of the way bitwise operations work, the leftmost bit that gets shifted out is lost. To account for this, we use the right shift operator `>>` to shift the bits `(32 - d)` places to the right. This brings the leftmost bit that was lost back into its original position.

Finally, we use the bitwise OR operator `|` to combine the shifted bits with the original bits, effectively rotating the bits to the left by `d` places.

The function returns the result of the rotation, which is the original number with its bits rotated to the left by `d` places.

For example, if we call `left_rotate(16, 2)`, it will return `64`, as the leftmost two bits (`00100000`) have been rotated to the left by two places, resulting in `10000000`.

Note that this function assumes that the input number is a 32-bit number. If you are working with a different number of bits, you will need to adjust the calculation accordingly.

Also note that this function only rotates the bits to the left by a specified number of places. If you need to rotate the bits to the right instead, you can simply replace the left shift operator `<<` with the right shift operator `>>`, and vice versa.
```

# Python code to demonstrate the above approach


def left_rotate(num, d):
    return (num << d)