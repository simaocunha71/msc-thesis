def left_rotate(n, d):
    d = d % 32
    return ((n << d) | (n >> (32 - d))) & 0xffffffff
    # 0xffffffff is used to ensure the result is a 32 bit integer
    # (n << d) is left shift operation, (n >> (32 - d)) is right shift operation, | is bitwise OR operation
    # the result of the left shift operation is shifted back (32 - d) bits and then bitwise OR with the original number
    # this is equivalent to the left rotation operation. The last operation is to ensure the result is a 32 bit integer.   