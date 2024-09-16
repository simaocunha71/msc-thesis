def odd_position(my_list):
    return all(x % 2 != 0 for x in my_list[::2])