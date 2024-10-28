def is_polite(n):
    binary = bin(n).replace("0b", "")
    binary = binary[::-1]
    return int(binary, 2) + n