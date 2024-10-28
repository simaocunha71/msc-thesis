def common_in_nested_lists(nested_lists):
    flat_list = [item for sublist in nested_lists for item in sublist]
    common = set(flat_list)
    for sublist in nested_lists:
        common &= set(sublist)
    return list(common)