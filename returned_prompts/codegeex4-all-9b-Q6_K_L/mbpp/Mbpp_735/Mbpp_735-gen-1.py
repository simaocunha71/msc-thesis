def toggle_middle_bits(n):
    return n ^ (n >> 1) ^ (n << 1)

# or
def toggle_middle_bits(n):
    return n ^ (n ^ (n >> 1) << 1)

# or
def toggle_middle_bits(n):
    return n ^ ((n >> 1) << 1)

