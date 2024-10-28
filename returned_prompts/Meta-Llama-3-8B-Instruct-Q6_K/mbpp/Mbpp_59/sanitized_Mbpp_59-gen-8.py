def is_octagonal(n):
    return int((8*n**3 + 3*n**2 + 2*n) / 2) if n > 0 else None