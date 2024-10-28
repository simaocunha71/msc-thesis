def toggle_middle_bits(n):
    if n < 0 or n > 2**31 - 1:
        raise ValueError("Input number is out of range")
    if n < 2:
        return n
    first_bit = n & 1
    last_bit = n & -1
    middle_bits = n ^ first_bit ^ last_bit
    return middle_bits