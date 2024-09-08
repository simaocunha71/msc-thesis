def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list