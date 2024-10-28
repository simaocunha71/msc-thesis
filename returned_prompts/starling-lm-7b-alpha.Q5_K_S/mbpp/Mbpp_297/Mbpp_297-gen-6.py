
def flatten_list(lst: list):
    flat_list = []
    for i in lst:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list


