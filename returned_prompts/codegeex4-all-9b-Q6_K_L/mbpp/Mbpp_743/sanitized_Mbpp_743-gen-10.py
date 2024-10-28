def rotate_right(lst, n):
    n = n % len(lst)  # Ensure n is within the length of the list
    return lst[-n:] + lst[:-n]