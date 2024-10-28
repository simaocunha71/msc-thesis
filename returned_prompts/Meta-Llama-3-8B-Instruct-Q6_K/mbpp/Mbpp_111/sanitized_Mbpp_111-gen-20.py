def common_in_nested_lists(nested_lists):
    elements = set()
    for nested_list in nested_lists:
        elements.update(set(nested_list))
    common = set()
    for nested_list in nested_lists:
        common.update(set(nested_list) & elements)
    return common