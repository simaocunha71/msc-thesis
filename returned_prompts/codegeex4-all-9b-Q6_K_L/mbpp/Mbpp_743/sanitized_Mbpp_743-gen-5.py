def rotate_right(lst, n):
    if not lst:
        return []
    n = n % len(lst)
    return lst[-n:] + lst[:-n]