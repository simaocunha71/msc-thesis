def toggle_middle_bits(n):
    b = bin(n)[2:]
    b = list(b)
    for i in range(1, len(b)-1):
        if b[i] == '1':
            b[i] = '0'
        else:
            b[i] = '1'
    return int(''.join(b), 2)