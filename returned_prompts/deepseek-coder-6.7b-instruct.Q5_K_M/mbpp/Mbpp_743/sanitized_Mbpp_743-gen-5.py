def rotate_right(lst, k):
    # We use list slicing to rotate the list
    return lst[-k:] + lst[:-k]