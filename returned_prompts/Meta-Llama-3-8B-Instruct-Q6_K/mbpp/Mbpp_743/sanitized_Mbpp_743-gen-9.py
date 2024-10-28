def rotate_right(lst, n):
    return lst[-n:] + lst[:-n] if n > 0 else lst[n:] + lst[:n]  # rotate to the right if n > 0, otherwise to the left