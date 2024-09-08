def is_polite(n):
    n += 1
    while bin(n).count('1') != bin(n).count('10'):
        n += 1
    return n