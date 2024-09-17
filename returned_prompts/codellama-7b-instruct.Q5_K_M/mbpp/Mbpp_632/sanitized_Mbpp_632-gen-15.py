def move_zero(my_list):
    return [z for z in my_list if z != 0] + [0 for z in my_list if z == 0]