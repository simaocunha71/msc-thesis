def differ_At_One_Bit_Pos(num1, num2):
    # XOR operation
    xor = num1 ^ num2
    # Check if there is exactly one bit set
    return xor & (xor - 1) == 0 and xor != 0