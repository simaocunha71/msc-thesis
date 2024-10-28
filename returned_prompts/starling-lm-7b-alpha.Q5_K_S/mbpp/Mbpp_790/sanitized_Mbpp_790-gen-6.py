def even_position(input_list):
    if len(input_list) % 2 != 0:
        return False
    else:
        for i in range(0, len(input_list), 2):
            if input_list[i] % 2 != 0:
                return False
    return True