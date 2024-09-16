"""
def differ_At_One_Bit_Pos(x, y):
    if (x & y) == 0:
        return False
    i = 0
    while (x > 0) and (y > 0):
        if (x & 1) != (y & 1):
            return False
        x >>= 1
        y >>= 1
        i += 1
    return True
"""

