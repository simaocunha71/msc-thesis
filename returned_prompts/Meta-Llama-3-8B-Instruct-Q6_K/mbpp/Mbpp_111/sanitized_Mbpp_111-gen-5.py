def common_in_nested_lists(nested_list):
    first_set = set(nested_list[0])
    for sublist in nested_list[1:]:
        first_set &= set(sublist)
    return first_set