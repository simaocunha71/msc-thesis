def toggle_middle_bits(n):
    bit_length = n.bit_length()
    if bit_length > 2:
        mask = (1 << (bit_length - 2)) - 1
        return n ^ mask
    return n

print(toggle_middle_bits(9))  # 15

Explanation:
The function first calculates the bit length of the number. If the number has more than 2 bits, it calculates a mask that has all bits set from the second bit to the last bit. It then returns the result of the bitwise XOR operation between the original number and the mask.
"""

# Solution 2: Using Python's bitwise operators and built-in function
