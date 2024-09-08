def common_in_nested_lists(nested_lists):
    common_elements = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common_elements.intersection_update(lst)
    return common_elements