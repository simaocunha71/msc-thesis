def toggle_middle_bits(n):
    # Shift the bits to the left by 1
    n = n << 1
    # Add the original number
    n += n >> 1
    # Toggle the bits
    n ^= n >> 1
    # Shift the bits to the right by 1
    n = n >> 1
    # Return the result
    return n