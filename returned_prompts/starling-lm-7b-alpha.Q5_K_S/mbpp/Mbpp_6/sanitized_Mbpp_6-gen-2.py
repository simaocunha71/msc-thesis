def differ_At_One_Bit_Pos(num1, num2):
    xor = num1 ^ num2
    if xor == 0 or xor == 1:
        return True
    else:
        return False