
def flatten_list(nested_list):
    flattened_list = []
    for element in nested_list:
        if type(element) == list:
            flattened_list += flatten_list(element)
        else:
            flattened_list.append(element)
    return flattened_list


