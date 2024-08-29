def even_position(lst):
    return all(i % 2 == 0 for i in lst[::2])