def is_polite(n):
    binary = bin(n)[2:]
    return n + int(binary, 2)