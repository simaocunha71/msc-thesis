import math
def count_binary_seq(n):
    # number of sequences where first n bits are 0 and last n bits are 0
    a = 1
    # number of sequences where first n bits are 1 and last n bits are 0
    b = 1
    # number of sequences where first n bits are 0 and last n bits are 1
    c = 1
    # number of sequences where first n bits are 1 and last n bits are 1
    d = 0
    
    for _ in range(n - 1):
        a, b, c, d = a + c, a + d, b, c + d
    
    return a + b