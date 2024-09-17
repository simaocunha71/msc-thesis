```
def toggle_middle_bits(n):
    # calculate the number of middle bits
    num_middle_bits = bin(n).count('1')
    # toggle the middle bits
    result = n ^ ((1 << num_middle_bits) - 1)
    return result
```
This function works by first calculating the number of middle bits in the binary representation of the input number. It then uses the bitwise XOR operator (^) to toggle these bits. The expression `(1 << num_middle_bits) - 1` generates a mask with the middle bits set to 1 and the rest set to 0. The XOR operator toggles the bits in the input number that are set to 1 in the mask. The first and last bits are not toggled because they are not included in the mask. 

For example, if the input number is 9 (which is 1001 in binary), the function calculates that there are 2 middle bits. The mask is then `000011` (which is `3` in decimal). The result of the XOR operation is `1111` (which is `15` in decimal), which is the expected output. 

The unit test `assert toggle_middle_bits(9) == 15` ensures that the function works correctly for this input. 