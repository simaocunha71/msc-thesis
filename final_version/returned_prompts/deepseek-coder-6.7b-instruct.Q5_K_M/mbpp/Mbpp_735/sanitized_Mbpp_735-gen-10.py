def toggle_middle_bits(n):
    bin_num = bin(n)[2:]
    bin_num = list(bin_num)
    for i in range(1, len(bin_num)-1):
        if bin_num[i] == '1':
            bin_num[i] = '0'
        else:
            bin_num[i] = '1'
    return int(''.join(bin_num), 2)