def common_in_nested_lists(nested_lists):
    flattened_list = [item for sublist in nested_lists for item in sublist]
    common_elements = set(flattened_list)
    for sublist in nested_lists:
        common_elements &= set(sublist)
    return list(common_elements)