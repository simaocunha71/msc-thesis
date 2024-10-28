def differ_At_One_Bit_Pos(x, y):
    return bin(x ^ y).count('1') == 1