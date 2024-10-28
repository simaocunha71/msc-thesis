def next_power_of_2(n):
    return 2 ** (n - 1).bit_length() if n > 0 else 1