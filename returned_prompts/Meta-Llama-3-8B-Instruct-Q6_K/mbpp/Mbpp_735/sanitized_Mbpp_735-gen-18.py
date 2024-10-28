def toggle_middle_bits(n):
    n = bin(n)[2:]
    n = list(n)
    n[1] = '1' if n[1] == '0' else '0'
    n = ''.join(n)
    return int(n, 2)