def flatten_list(nested_list):
    result = []
    for element in nested_list:
        if type(element) == list:
            result.extend(flatten_list(element))
        else:
            result.append(element)
    return result