def differ_At_One_Bit_Pos(x,y):
    """
    This function will check whether two numbers differ at one bit position or not
    """
    xor = x^y
    while xor != 0:
        if xor % 2 == 1:
            return False
        xor = xor >> 1
    return True
x = 13
y = 9