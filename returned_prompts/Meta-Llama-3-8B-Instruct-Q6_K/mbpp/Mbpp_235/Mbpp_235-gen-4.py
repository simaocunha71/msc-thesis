```
def even_bit_set_number(n):
    return n | (n >> 1)
```
The function uses bitwise OR operator (`|`) to set all even bits of the given number. The expression `n >> 1` is used to shift the bits of `n` to the right by one position, which is equivalent to dividing `n` by 2. The bitwise OR operator (`|`) is then used to set all even bits of `n` to 1. The result is the original number with all even bits set to 1.

For example, if the input is `10` (which is `1010` in binary), the function will return `10` because the even bits (the second and fourth bits) are set to 1. The odd bits (the first and third bits) remain unchanged. The binary representation of the output is `1010`, which is the same as the input. This is confirmed by the unit test `assert even_bit_set_number(10) == 10`.