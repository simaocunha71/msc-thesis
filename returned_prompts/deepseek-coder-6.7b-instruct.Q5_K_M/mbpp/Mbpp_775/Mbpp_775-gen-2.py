
def odd_position(lst):
    return all(x % 2 != 0 for x in lst[::2])


