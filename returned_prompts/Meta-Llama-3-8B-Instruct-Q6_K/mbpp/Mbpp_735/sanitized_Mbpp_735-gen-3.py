def toggle_middle_bits(n):
    return ((n & 1) | ((n >> 1) & 1)) << 1 | 1 | ((n >> 1) & (~((n >> 1) | 1)))
    #return ((n & 1) | ((n >> 1) & 1)) << 1 | 1 | ((n >> 1) & (~((n >> 1) | 1)))  #Alternate solution