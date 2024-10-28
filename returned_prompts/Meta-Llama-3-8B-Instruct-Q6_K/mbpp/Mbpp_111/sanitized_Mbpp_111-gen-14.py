def common_in_nested_lists(nested_lists):
    all_elements = set()
    for nested_list in nested_lists:
        all_elements.update(nested_list)
    common_elements = set()
    for nested_list in nested_lists:
        common_elements.update(set(nested_list) & all_elements)
    return list(common_elements)