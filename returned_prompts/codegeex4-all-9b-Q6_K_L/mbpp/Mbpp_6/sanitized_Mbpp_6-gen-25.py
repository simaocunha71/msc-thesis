def differ_At_One_Bit_Pos(n1, n2):
    n = n1 ^ n2
    return n & (n - 1) == 0 and n != 0