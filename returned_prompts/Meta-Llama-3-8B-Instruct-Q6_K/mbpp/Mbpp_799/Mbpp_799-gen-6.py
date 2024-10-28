```
def left_rotate(n, d):
    return ((n << d) | (n >> (32 - d)))
```
This function works by shifting the bits of the number `n` to the left by `d` positions, and then performing a bitwise OR operation with the result of shifting the bits of `n` to the right by `(32 - d)` positions. This effectively rotates the bits of `n` to the left by `d` positions.

For example, if `n` is 16 (which is 10000 in binary) and `d` is 2, then the function will shift the bits of 16 to the left by 2 positions, resulting in 64 (which is 1000000 in binary), and then perform a bitwise OR operation with the result of shifting the bits of 16 to the right by 30 positions (32 - 2), resulting in 64 as well.

The unit test `assert left_rotate(16,2) == 64` confirms that this function works correctly.