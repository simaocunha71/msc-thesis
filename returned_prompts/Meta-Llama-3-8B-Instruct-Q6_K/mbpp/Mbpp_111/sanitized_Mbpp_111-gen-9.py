def common_in_nested_lists(nested_lists):
    common = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common &= set(lst)
    return common