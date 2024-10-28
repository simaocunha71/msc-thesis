def even_bit_set_number(n):
    # 1 is 0000 0001
    # 2 is 0000 0010
    # 4 is 0000 0100
    # 8 is 0000 1000
    # 16 is 0001 0000
    # 32 is 0010 0000
    # 64 is 0100 0000
    # 128 is 1000 0000
    return n | 0xAAAAAAAA

