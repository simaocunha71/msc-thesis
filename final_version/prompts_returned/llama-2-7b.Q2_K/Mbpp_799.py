"""
Write a function to that rotate left bits by d bits a given number. We assume that the number is 32 bit.
assert left_rotate(16,2) == 64
"""

def left_rotate(n,d):
    """Rotate right bits on left side of n.
    This function assumes n to be integer type (unsigned or signed),
    and d is the number of bits that need to be rotated to the left.
    16-bit to 24-bits and 32-bit to 16-bits. If we try rotate right side,
    then it will fail to change more than 15 bits.
    Example:
    n = 0b110101010
    d = 8 -> 0b110101010000000
      (not 0b11010101010 because we rotate bits to the left)."""
    n = bin(n)[2:].zfill(d+1)
    return int("".join([c%2 for c in n]),16)