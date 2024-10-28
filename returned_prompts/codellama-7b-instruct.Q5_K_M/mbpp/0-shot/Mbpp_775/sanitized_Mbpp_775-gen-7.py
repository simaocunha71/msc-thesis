def odd_position(my_list):
    for i, v in enumerate(my_list):
        if i % 2 == 0:
            if v % 2 == 0:
                return False
    return True