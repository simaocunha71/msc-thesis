def next_power_of_2(n):
    if n == 0:
        return 1
    elif n & (n - 1) == 0:
        return n
    else:
        return 2 ** (n.bit_length() + 1)