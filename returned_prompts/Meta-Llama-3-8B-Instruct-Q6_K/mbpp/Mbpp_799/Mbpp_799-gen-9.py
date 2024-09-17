```
def left_rotate(n, d):
    d = d % 32
    return (n << d) | (n >> (32 - d))
```
This function works by using the bitwise left shift operator (`<<`) to shift the bits of the number `n` to the left by `d` bits. Then it uses the bitwise right shift operator (`>>`) to shift the bits that were shifted out of the left side back to the right side. The `% 32` is used to handle the case where `d` is greater than 32.

The unit test `assert left_rotate(16,2) == 64` ensures that the function works correctly for the given example. 

In this case, the number 16 is rotated 2 bits to the left, which results in 64. 

The function can be tested with other inputs to ensure it works correctly for all cases. 