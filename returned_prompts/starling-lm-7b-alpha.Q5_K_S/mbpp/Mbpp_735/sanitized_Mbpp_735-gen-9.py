def toggle_middle_bits(n):
    # Convert the number to binary
    binary = bin(n)[2:]
    
    # Get the length of the binary string
    length = len(binary)
    
    # Toggle all bits except the first and the last bit
    for i in range(1, length-1):
        # Convert the bit at index i to 1 if it's 0 and vice versa
        if binary[i] == '0':
            binary = binary[:i] + '1' + binary[i+1:]
        else:
            binary = binary[:i] + '0' + binary[i+1:]
    
    # Convert the binary string back to an integer
    return int(binary, 2)