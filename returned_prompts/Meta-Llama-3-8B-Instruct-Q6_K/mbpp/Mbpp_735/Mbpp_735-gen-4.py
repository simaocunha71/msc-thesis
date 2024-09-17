```
def toggle_middle_bits(n):
    n = bin(n)[2:]  # Convert to binary and remove '0b' prefix
    if len(n) < 3:  # If the number has less than 3 bits, return the number itself
        return n
    n = n[:1] + ''.join('1' if bit == '0' else '0' for bit in n[1:-1]) + n[-1]  # Toggle middle bits
    return int(n, 2)  # Convert back to decimal
```





This function first converts the input number to binary and removes the '0b' prefix. If the number has less than 3 bits, it returns the number itself. Otherwise, it toggles the middle bits (excluding the first and last bit) and converts the binary string back to a decimal number. The unit test `assert toggle_middle_bits(9) == 15` ensures that the function works correctly.