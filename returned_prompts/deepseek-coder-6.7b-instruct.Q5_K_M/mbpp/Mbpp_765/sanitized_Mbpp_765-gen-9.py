def is_polite(n):
    return bin(n).count('1') == bin(n+1).count('1')