def differ_At_One_Bit_Pos(a, b):
    while a != b:
        a = a ^ (a & -a)
        b = b ^ (b & -b)
    return False