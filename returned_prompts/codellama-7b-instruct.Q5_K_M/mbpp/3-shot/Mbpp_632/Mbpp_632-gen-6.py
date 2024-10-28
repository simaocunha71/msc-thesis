
def move_zero(my_list):
    return [*filter(lambda x: x != 0, my_list), *[0] * my_list.count(0)]


