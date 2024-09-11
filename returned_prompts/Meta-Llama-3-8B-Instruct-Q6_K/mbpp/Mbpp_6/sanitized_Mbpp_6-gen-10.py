def differ_At_One_Bit_Pos(a, b):
    while a != b:
        a = (a ^ b) & ((a ^ b) - 1)
        if a == 0:
            return False
    return True