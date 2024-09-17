def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2**(n.bit_length()+ (n & (n-1) == 0))