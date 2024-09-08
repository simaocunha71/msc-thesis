def toggle_middle_bits(n):
    binary = bin(n)[2:] # binary representation of n
    middle_bits = list(binary[1:-1]) # excluding first and last bit
    for i in range(len(middle_bits)):
        middle_bits[i] = '1' if middle_bits[i] == '0' else '0' # toggle bits
    binary = binary[0] + ''.join(middle_bits) + binary[-1] # join bits back
    return int(binary, 2) # convert binary back to decimal