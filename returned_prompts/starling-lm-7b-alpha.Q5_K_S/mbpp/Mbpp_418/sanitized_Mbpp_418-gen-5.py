def Find_Max(my_list):
    if not my_list:
        return None
    max_length = 0
    max_index = 0
    for index, item in enumerate(my_list):
        if len(item) > max_length:
            max_length = len(item)
            max_index = index
    return my_list[max_index]