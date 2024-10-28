def flatten_list(list_struct):
    flat_list = []
    for element in list_struct:
        if type(element) is list:
            flat_list += flatten_list(element)
        else:
            flat_list.append(element)
    return flat_list