
def differ_At_One_Bit_Pos(a, b):
    c = a ^ b
    c = c & (c - 1)
    return c != 0


