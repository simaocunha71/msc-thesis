def differ_At_One_Bit_Pos(a, b):
    xor = a ^ b
    # check if xor has exactly one bit set
    return xor and (xor & (xor - 1)) == 0