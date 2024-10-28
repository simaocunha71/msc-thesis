def toggle_middle_bits(n):
    n = bin(n)[2:]  # convert to binary and remove '0b' prefix
    n = n[1:-1]  # remove first and last bit
    n = ''.join('1' if bit == '0' else '0' for bit in n)  # toggle bits
    return int(n + '1', 2)  # add back the last bit and convert back to integer