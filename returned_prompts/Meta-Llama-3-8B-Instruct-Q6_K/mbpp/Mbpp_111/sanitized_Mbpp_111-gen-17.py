def common_in_nested_lists(nested_lists):
    result = set(nested_lists[0])
    for lst in nested_lists[1:]:
        result &= set(lst)
    return result