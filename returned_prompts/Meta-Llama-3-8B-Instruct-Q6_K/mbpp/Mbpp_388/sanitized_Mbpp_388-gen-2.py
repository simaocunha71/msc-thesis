def highest_Power_of_2(n):
    return 2 ** (n.bit_length() - 1) if n > 0 else 0