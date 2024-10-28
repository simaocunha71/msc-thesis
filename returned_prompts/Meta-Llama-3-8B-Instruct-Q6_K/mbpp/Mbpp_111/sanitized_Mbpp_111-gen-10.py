def common_in_nested_lists(nested_list):
    result = set(nested_list[0])
    for sublist in nested_list[1:]:
        result &= set(sublist)
    return result