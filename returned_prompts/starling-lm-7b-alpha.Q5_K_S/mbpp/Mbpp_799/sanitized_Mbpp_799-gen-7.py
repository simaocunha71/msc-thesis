def left_rotate(num, d):
    '''
    Rotate left bits by d bits a given number
    '''
    return ((num << d) & 0xFFFFFFFF) | (num >> (32 - d))