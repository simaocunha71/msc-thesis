def common_in_nested_lists(nested_list: list) -> list:
    common_elements = set(nested_list[0])
    for lst in nested_list[1:]:
        common_elements &= set(lst)
    return common_elements