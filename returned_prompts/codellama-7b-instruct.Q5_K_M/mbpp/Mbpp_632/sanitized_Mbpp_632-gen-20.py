def move_zero(my_list):
    return [item for item in my_list if item != 0] + [0] * my_list.count(0)