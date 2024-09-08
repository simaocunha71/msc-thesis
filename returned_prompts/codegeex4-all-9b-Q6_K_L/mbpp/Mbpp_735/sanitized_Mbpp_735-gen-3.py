def toggle_middle_bits(n):
    # Convert the number to binary string
    binary_str = bin(n)[2:]

    # Toggle the middle bits
    toggled_str = ''.join('1' if bit == '0' else '0' for bit in binary_str[1:-1])

    # Convert the toggled binary string back to decimal
    toggled_num = int(toggled_str, 2)

    return toggled_num