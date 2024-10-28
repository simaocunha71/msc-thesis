def differ_At_One_Bit_Pos(a, b):
    diff = a ^ b
    if diff == 0:
        return False
    else:
        return bin(diff).count('1') == 1