def toggle_middle_bits(n):
    # Convert number to binary string
    binary_str = bin(n)[2:]
    
    # Check if the number has more than 2 bits
    if len(binary_str) > 2:
        # Toggle middle bits
        middle_bits = binary_str[1:-1]
        toggled_middle_bits = ''.join('1' if bit == '0' else '0' for bit in middle_bits)
        
        # Combine first and last bit with toggled middle bits
        result = binary_str[0] + toggled_middle_bits + binary_str[-1]
        
        # Convert binary string back to decimal number
        return int(result, 2)
    else:
        return n