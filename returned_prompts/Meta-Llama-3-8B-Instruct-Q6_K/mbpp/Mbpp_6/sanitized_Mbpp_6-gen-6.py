def differ_At_One_Bit_Pos(num1: int, num2: int) -> bool:
    bin_str1 = bin(num1)[2:]
    bin_str2 = bin(num2)[2:]
    if len(bin_str1) > len(bin_str2):
        bin_str2 = bin_str2.zfill(len(bin_str1))
    elif len(bin_str2) > len(bin_str1):
        bin_str1 = bin_str1.zfill(len(bin_str2))
    for i in range(len(bin_str1)):
        if bin_str1[i] != bin_str2[i]:
            return True
    return False