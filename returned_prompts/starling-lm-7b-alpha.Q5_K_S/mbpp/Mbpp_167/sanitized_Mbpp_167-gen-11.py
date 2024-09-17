def next_power_of_2(n):
    return 2 ** (n.bit_length() + (n & -n != 0))