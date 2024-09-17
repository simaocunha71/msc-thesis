def differ_At_One_Bit_Pos(n1, n2):
    x = n1 ^ n2
    return (x and (x & (x - 1)) == 0)