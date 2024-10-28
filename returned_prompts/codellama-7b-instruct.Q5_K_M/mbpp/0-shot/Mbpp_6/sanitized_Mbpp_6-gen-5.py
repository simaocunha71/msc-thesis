def differ_At_One_Bit_Pos(num1,num2):
    bit_pos = 0
    while num1>>bit_pos and num2>>bit_pos:
        if num1 & 1 != num2 & 1:
            return True
        num1 >>= 1
        num2 >>= 1
        bit_pos += 1
    return False