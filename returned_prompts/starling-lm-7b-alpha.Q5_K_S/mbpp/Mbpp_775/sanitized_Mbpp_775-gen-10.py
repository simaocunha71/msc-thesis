def odd_position(input_list):
    for index, item in enumerate(input_list):
        if index % 2 == 0 and item % 2 == 0:
            return False
    return True