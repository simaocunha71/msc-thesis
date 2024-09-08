def toggle_middle_bits(n):
    binary_n = bin(n)[2:]
    binary_n = list(binary_n)
    for i in range(1, len(binary_n)-1):
        if binary_n[i] == '1':
            binary_n[i] = '0'
        else:
            binary_n[i] = '1'
    return int(''.join(binary_n), 2)