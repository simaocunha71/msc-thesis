
def is_polite(n):
    unset_bit_count = 0
    index = 0
    while unset_bit_count < n:
        if not(n & (1 << index)):
            unset_bit_count += 1
        index += 1
    return n | (1 << (index - 1))


