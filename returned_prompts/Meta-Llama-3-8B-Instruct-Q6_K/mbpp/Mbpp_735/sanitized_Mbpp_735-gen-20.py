def toggle_middle_bits(n):
    # calculate the number of middle bits
    num_middle_bits = bin(n).count('1')
    # toggle the middle bits
    result = n ^ ((1 << num_middle_bits) - 1)
    return result