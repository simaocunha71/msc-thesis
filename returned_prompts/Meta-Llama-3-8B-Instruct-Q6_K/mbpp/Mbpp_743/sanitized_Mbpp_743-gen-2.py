def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]  # slice the list and concatenate the two parts