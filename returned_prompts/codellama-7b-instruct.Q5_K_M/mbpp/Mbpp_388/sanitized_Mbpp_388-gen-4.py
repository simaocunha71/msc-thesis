def highest_Power_of_2(n):
    # 2**31 - 1 is the maximum value that can be stored in an integer in python3
    # so we don't have to worry about overflows
    i = 1
    while 2**i <= n:
        i *= 2
    return i // 2