def toggle_middle_bits(n):
    n = bin(n)[2:]
    n = n[:-1] + '0' + n[-1]
    return int(n, 2)