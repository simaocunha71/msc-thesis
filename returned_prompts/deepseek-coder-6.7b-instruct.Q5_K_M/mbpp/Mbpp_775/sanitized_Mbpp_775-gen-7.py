def odd_position(lst):
    return all(el % 2 == 1 for i, el in enumerate(lst) if i % 2 == 1)