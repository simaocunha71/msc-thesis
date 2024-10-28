def differ_At_One_Bit_Pos(x: int, y: int) -> bool:
    return (bin(x^y).count('1') == 1)