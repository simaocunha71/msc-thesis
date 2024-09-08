def is_polite(n):
    return bin(n).count('1') == bin(n+1).count('1')

print(is_polite(7))  # 11


