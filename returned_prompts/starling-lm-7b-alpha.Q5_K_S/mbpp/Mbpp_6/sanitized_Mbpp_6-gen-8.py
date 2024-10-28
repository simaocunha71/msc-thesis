def differ_At_One_Bit_Pos(num1,num2):
    xor = num1^num2
    count = 0
    while xor:
        if xor&1:
            count += 1
        xor >>= 1
    if count == 1:
        return True
    else:
        return False