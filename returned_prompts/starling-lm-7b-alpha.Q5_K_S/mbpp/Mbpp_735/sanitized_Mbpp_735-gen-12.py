def toggle_middle_bits(n):
    n = bin(n)[2:]
    n = n[:2] + "0" + "1"*(len(n)-2) + n[-1]
    return int(n, 2)