def even_position(input_list):
    for index, value in enumerate(input_list):
        if index % 2 != 0 and value % 2 == 0:
            return False
    return True