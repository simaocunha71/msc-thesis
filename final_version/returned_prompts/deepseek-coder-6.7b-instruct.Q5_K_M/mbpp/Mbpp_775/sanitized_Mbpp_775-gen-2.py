def odd_position(lst):
    return all(x % 2 == 1 for x in lst[::2])