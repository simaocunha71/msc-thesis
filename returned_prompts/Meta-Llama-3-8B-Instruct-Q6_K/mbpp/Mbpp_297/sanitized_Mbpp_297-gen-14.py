def flatten_list(lst):
    flat_list = []
    for item in lst:
        if type(item) == list:
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list