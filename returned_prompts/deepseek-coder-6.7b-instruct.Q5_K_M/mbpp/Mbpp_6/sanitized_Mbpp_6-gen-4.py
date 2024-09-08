def differ_At_One_Bit_Pos(num1,num2):
    binary_num1 = bin(num1)[2:]
    binary_num2 = bin(num2)[2:]
    if abs(len(binary_num1) - len(binary_num2)) > 1:
        return False
    elif len(binary_num1) < len(binary_num2):
        binary_num1 = '0'*(len(binary_num2)-len(binary_num1)) + binary_num1
    elif len(binary_num2) < len(binary_num1):
        binary_num2 = '0'*(len(binary_num1)-len(binary_num2)) + binary_num2
    diff_count = 0
    for i in range(len(binary_num1)):
        if binary_num1[i] != binary_num2[i]:
            diff_count += 1
    if diff_count == 1:
        return True
    else:
        return False