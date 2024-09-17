def common_in_nested_lists(nested_lists):
    common_set = set()
    for lst in nested_lists:
        common_set |= set(lst)
    return common_set