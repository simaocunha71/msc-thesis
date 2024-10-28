def differ_At_One_Bit_Pos(num1, num2):
    binary_num1 = bin(num1)
    binary_num2 = bin(num2)
    if len(binary_num1) != len(binary_num2):
        return False
    count = 0
    for i in range(len(binary_num1)):
        if binary_num1[i] != binary_num2[i]:
            count += 1
        if count > 1:
            return False
    return True

