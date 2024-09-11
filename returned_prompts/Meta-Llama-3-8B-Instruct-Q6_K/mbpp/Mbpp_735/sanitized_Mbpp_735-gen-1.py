def toggle_middle_bits(n):
    n = bin(n)[2:]
    n = n[1:-1]
    for i in range(0, len(n)):
        if n[i] == '0':
            n = n[:i] + '1' + n[i+1:]
        else:
            n = n[:i] + '0' + n[i+1:]
    return int(n, 2) | (1 << len(n) - 1)