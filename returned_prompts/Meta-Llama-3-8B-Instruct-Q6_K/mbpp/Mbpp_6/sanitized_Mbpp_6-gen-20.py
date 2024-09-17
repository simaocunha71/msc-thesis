def differ_At_One_Bit_Pos(a, b):
    x = a ^ b
    if x & (x & -x) == 0:
        return True
    return False