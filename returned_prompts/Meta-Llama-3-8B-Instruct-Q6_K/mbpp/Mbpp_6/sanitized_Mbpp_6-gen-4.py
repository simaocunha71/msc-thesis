def differ_At_One_Bit_Pos(a, b):
    if a == b:
        return False
    return bin(a ^ b).count('1') == 1