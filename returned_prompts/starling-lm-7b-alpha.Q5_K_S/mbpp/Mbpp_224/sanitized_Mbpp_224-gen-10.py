def count_Set_Bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count