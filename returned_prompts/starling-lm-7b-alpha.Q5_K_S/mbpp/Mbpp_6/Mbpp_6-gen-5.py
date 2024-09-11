"""
def differ_At_One_Bit_Pos(n1, n2):
    diff = n1 ^ n2
    if diff == 0:
        return False
    for i in range(32):
        if (diff & (1 << i)):
            return True
    return False

"""

