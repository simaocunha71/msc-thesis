def rotate_right(lst, num_items):
    return lst[-num_items:] + lst[:-num_items]  # slicing and concatenation