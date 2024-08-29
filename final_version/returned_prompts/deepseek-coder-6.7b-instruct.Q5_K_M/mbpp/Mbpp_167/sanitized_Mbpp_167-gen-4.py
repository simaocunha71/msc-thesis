def next_power_of_2(n):
    if (n <= 0):
        return 1
    if (n & (n - 1)):
        return 2 * (n.bit_length() + 1)
    else:
        return n