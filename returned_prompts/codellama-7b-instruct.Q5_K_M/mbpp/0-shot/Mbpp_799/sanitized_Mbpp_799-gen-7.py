def left_rotate(x,d):
    return (x << d) | (x >> (32-d))