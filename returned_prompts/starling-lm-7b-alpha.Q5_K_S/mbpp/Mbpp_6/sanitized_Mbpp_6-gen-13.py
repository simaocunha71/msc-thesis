def differ_At_One_Bit_Pos(n1: int, n2: int) -> bool:
    return bin(n1^n2).count('1') == 1