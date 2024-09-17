def toggle_middle_bits(n):
    return int('1' + bin(n)[2:][:-1] + '1', 2)