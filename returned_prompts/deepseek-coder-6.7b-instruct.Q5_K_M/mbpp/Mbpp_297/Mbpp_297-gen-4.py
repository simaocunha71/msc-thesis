
def flatten_list(nested_list):
    result = []
    for i in nested_list:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result


