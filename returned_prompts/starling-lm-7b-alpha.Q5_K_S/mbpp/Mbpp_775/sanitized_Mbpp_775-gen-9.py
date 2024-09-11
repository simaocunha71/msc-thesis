def odd_position(list):
    return all(i % 2 != 0 for i in list[::2])