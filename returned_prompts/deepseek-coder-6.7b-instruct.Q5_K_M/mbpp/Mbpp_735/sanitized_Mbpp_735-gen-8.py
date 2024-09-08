def toggle_middle_bits(n):
    if n == 0 or n == 1 or n == 2 or n == 4 or n == 8:
        return n
    else:
        return toggle_middle_bits(n & (n - 1))