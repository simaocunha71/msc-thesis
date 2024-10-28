```
def left_rotate(n, d):
    d = d % 32
    return ((n << d) | (n >> (32 - d)))
```
The function takes two parameters, n (the number to rotate) and d (the number of bits to rotate). The function first calculates the remainder of d divided by 32 (since 32 is the number of bits in an integer). This is done to handle cases where d is greater than 32.

Then the function performs a left shift operation on n by d bits using the left shift operator <<. This effectively moves the bits of n to the left by d positions.

Finally, the function performs a right shift operation on n by 32 - d bits using the right shift operator >>. This effectively moves the bits of n that were shifted out of the 32-bit integer to the right by 32 - d positions.

The two results of the left and right shift operations are then combined using the bitwise OR operator |. This effectively combines the bits that were shifted out of the 32-bit integer with the bits that were not shifted.

The result is the original number n rotated to the left by d bits. This is tested with the unit test assert left_rotate(16,2) == 64.