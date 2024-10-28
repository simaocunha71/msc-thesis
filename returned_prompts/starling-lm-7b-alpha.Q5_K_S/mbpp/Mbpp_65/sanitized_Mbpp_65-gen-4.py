def recursive_list_sum(input_list):
    """flatten a list and sum all of its elements"""
    sum = 0
    for elem in input_list:
        if type(elem) == list:
            sum += recursive_list_sum(elem)
        else:
            sum += elem
    return sum