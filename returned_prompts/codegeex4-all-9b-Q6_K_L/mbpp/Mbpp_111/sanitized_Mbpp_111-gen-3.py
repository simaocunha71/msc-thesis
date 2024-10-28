def common_in_nested_lists(nested_lists):
    common_elements = set(nested_lists[0])
    for sublist in nested_lists[1:]:
        common_elements &= set(sublist)
    return list(common_elements)