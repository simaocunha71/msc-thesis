def even_position(my_list):
    for index, value in enumerate(my_list):
        if index % 2 == 0 and value % 2 == 1:
            return False
    return True