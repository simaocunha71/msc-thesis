def highest_Power_of_2(n):
    if n < 2:
        return 0
    else:
        return 2 ** (n.bit_length() - 1)