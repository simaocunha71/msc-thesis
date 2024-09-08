def toggle_middle_bits(n):
    if n == 0 or n == 1:
        return n
    mask = (2 ** (len(bin(n)) - 3)) - 1
    return n ^ mask