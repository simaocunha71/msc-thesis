def Find_Min(input_list):
    """
    This function will find the sublist with the minimum length from the given list of sublists
    """
    min_len = len(input_list[0])
    min_index = 0
    for index, value in enumerate(input_list):
        if len(value) < min_len:
            min_len = len(value)
            min_index = index
    return input_list[min_index]