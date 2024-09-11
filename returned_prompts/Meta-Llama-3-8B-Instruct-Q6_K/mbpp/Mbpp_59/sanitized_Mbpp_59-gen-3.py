def is_octagonal(n):
    if n < 1:
        return None
    return int(((8*n-1)**0.5-1)/2)**2