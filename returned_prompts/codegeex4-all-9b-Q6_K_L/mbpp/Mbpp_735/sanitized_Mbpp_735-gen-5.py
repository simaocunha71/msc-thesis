def toggle_middle_bits(n: int) -> int:
    # Shift right to remove the first bit
    n >>= 1
    # Toggle the bits
    n ^= (n << 1)
    # Shift left to place the bits back in their original positions
    n <<= 1
    # Set the first bit
    n |= 1
    # Set the last bit
    n |= (1 << (n.bit_length() - 1))
    return n