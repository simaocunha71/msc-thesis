def move_zero(my_list):
    return [i for i in my_list if i != 0] + [0 for i in my_list if i == 0]
