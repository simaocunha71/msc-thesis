def differ_At_One_Bit_Pos(a, b):
    while a != b:
        a = a & (a ^ b)
        b = b & (a ^ b)
    return False
    # return True if a != b else False