def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if type(element) == list:
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list