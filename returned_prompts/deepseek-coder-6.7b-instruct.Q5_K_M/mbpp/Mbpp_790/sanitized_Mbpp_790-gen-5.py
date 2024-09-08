def even_position(lst):
    return all(el % 2 == 0 for i, el in enumerate(lst) if i % 2 == 0)