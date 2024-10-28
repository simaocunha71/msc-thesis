def even_position(my_list):
    for idx, value in enumerate(my_list):
        if idx % 2 == 0 and value % 2 == 1:
            return False
    return True