def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist if not isinstance(item, list)]