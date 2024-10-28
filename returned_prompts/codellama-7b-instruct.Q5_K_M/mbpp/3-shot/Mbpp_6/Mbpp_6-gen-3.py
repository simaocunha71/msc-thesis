
def differ_At_One_Bit_Pos(a, b):
    c = a ^ b
    if c == 0:
        return False
    while c & 1 == 0:
        c >>= 1
    return c == 1


