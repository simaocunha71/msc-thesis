
def toggle_middle_bits(n):
    binary = bin(n)[2:]
    middle_bits = list(binary[1:-1])
    for i in range(len(middle_bits)):
        if middle_bits[i] == '1':
            middle_bits[i] = '0'
        else:
            middle_bits[i] = '1'
    new_binary = binary[0] + "".join(middle_bits) + binary[-1]
    return int(new_binary, 2)


