def count_Set_Bits(n):
    if n == 0:
        return 0
    else:
        return 1 + count_Set_Bits(n & (n - 1))