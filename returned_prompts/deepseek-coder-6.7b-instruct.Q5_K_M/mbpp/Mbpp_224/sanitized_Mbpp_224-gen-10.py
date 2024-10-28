def count_Set_Bits(num):
    binary = bin(num)[2:]
    return binary.count('1')