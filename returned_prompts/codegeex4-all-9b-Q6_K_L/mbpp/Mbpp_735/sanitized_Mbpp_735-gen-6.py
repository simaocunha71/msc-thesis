def toggle_middle_bits(num):
    # Convert the number to binary
    binary = bin(num)[2:]

    # Toggle the middle bits
    toggled_binary = binary[:1] + ''.join('1' if bit == '0' else '0' for bit in binary[1:-1]) + binary[-1:]

    # Convert the toggled binary back to decimal
    toggled_num = int(toggled_binary, 2)

    return toggled_num