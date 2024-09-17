def toggle_middle_bits(num: int):
    num = bin(num)[2:]
    num = '0'*(4-len(num)) + num
    num = list(num)
    num[1] = '1' if num[1] == '0' else '0'
    num[2] = '1' if num[2] == '0' else '0'
    num[3] = '1' if num[3] == '0' else '0'
    return int(''.join(num), 2)