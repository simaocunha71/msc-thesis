def differ_At_One_Bit_Pos(num1, num2):
    xor_result = num1 ^ num2
    return xor_result & (xor_result - 1) == 0