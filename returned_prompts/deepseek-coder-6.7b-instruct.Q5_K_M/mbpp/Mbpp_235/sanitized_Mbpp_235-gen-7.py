def even_bit_set_number(n):
    binary_n = bin(n)[2:]
    binary_n = binary_n.zfill(len(binary_n)+1)
    binary_list = list(binary_n)
    for i in range(0, len(binary_list), 2):
        binary_list[i] = '1'
    new_number = "".join(binary_list)
    return int(new_number, 2)