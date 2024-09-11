def left_rotate(n,d):
    '''
    Rotate left bits by d bits a given number. We assume that the number is 32 bit.
    '''
    return ((n<<d)%(2**32)) | (n>>32-d)