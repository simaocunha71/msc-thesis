def toggle_middle_bits(n):
    n = bin(n)[2:]  # Convert to binary and remove '0b' prefix
    if len(n) < 3:  # If the number has less than 3 bits, return the number itself
        return n
    n = n[:1] + ''.join('1' if bit == '0' else '0' for bit in n[1:-1]) + n[-1]  # Toggle middle bits
    return int(n, 2)  # Convert back to decimal