def is_polite(n):
    return n + 2 ** (bin(n).count('1'))