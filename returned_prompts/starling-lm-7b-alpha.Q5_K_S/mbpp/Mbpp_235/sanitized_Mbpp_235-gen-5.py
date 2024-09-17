def even_bit_set_number(num):
    return bin(num).replace("0b", "")[::-1].zfill(32)[::2]