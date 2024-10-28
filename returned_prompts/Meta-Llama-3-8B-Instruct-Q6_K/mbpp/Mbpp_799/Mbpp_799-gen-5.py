```
def left_rotate(n, d):
    return ((n << d) | (n >> (32 - d)))
```
This function uses the bitwise left shift operator `<<` to shift the bits of the number `n` to the left by `d` positions. Then it uses the bitwise OR operator `|` to combine the result with the result of the bitwise right shift operator `>>` of `n` by `32 - d` positions. This effectively rotates the bits of `n` to the left by `d` positions. 

The unit test `assert left_rotate(16,2) == 64` suggests that the function should rotate the bits of the number 16 to the left by 2 positions, resulting in 64. 

The time complexity of this function is O(1) because it only involves a constant number of operations and does not depend on the size of the input. The space complexity is also O(1) because it only uses a constant amount of space to store the result. 