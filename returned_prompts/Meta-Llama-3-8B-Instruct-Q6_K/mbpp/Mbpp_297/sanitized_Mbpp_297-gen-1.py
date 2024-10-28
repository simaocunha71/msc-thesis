def flatten_list(lst):
    flat_list = []
    for i in lst:
        if type(i) == list:
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list