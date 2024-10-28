def common_in_nested_lists(nested_lists):
    return set(item for sublist in nested_lists for item in sublist)