def common_in_nested_lists(nested_lists):
    if len(nested_lists) == 0:
        return []
    common_elements = set(nested_lists[0])
    for lst in nested_lists[1:]:
        common_elements = common_elements.intersection(set(lst))
    return list(common_elements)