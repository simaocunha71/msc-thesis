    b_rotated = b[-1:] + b[:-1]
    for _ in range(len(b)):
        if b_rotated in a:
            return True
        b_rotated = b_rotated[-1:] + b_rotated[:-1]
    return False


