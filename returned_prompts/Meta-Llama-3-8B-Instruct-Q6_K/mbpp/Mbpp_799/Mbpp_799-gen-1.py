```
def left_rotate(n, d):
    return ((n << d) | (n >> (32 - d)))
```
This function uses bitwise operators to achieve the left rotation. The expression `n << d` shifts the bits of `n` to the left by `d` positions, which is equivalent to rotating the bits of `n` to the left by `d` positions. The expression `n >> (32 - d)` shifts the bits of `n` to the right by `32 - d` positions, which is equivalent to rotating the bits of `n` to the right by `d` positions. The bitwise OR operator `|` is used to combine the two results, effectively rotating the bits of `n` to the left by `d` positions. The result is a 32-bit integer.

The unit test `assert left_rotate(16,2) == 64` ensures that the function works correctly for the given input. It checks that the result of rotating the number 16 to the left by 2 positions is equal to 64. This test passes because the result of the function is indeed 64, which is the correct result for the given input.