def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if type(i) == list:
            flat_list.extend(i)
        else:
            flat_list.append(i)
    return flat_list