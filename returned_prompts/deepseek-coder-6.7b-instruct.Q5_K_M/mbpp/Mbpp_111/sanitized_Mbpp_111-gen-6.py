def common_in_nested_lists(nested_lists):
    return [item for item in nested_lists[0] if all(item in sublist for sublist in nested_lists)]