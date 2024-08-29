def even_bit_set_number(n):
    binary_n = bin(n)[2:]
    binary_n = binary_n.zfill(8)
    binary_n = list(binary_n)
    for i in range(0, len(binary_n), 2):
        binary_n[i] = '1'
    return int(''.join(binary_n), 2)

print(even_bit_set_number(10)) # 10

