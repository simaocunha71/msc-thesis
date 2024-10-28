```
def left_rotate(n, d):
    d = d % 32
    mask = (1 << d) - 1
    return ((n << d) | (n >> (32 - d))) & ~mask
```
The function `left_rotate` takes two parameters: `n` (the number to be rotated) and `d` (the number of positions to rotate left).

First, we calculate the remainder of `d` divided by 32, because there are only 32 bits in a 32-bit integer.

Then, we create a mask with `d` bits set to 1. This mask will be used to shift the bits of `n`.

Next, we shift `n` to the left by `d` positions, and then shift it to the right by `32 - d` positions. This effectively rotates the bits of `n` to the left by `d` positions.

Finally, we use the mask to clear the bits that were shifted out of the original position. This ensures that the rotated bits are correctly aligned.

The function returns the rotated number.

For example, if we call `left_rotate(16, 2)`, the function will rotate the bits of 16 to the left by 2 positions, resulting in 64. This is because the binary representation of 16 is `00010000`, and rotating the bits to the left by 2 positions results in `01000000`, which is the binary representation of 64.