def even_position(lst):
    return all(elm % 2 == 0 for elm in lst[::2])