```
def toggle_middle_bits(n):
    if n < 0 or n > 2**31 - 1:
        raise ValueError("Input number is out of range")
    if n < 2:
        return n
    first_bit = n & 1
    last_bit = n & -1
    middle_bits = n ^ first_bit ^ last_bit
    return middle_bits
```
Explanation:

- The function takes an integer `n` as input.
- It checks if the input number is within the range of 32-bit integer.
- If the input number is less than 2, it returns the number as it is.
- It toggles the middle bits of the number by performing a bitwise XOR operation with the first bit and the last bit.
- The function returns the resulting number.

Test case:
`assert toggle_middle_bits(9) == 15` This test case checks if the function correctly toggles the middle bits of the number 9, which is 1001 in binary, and returns 1111, which is 15 in decimal. 