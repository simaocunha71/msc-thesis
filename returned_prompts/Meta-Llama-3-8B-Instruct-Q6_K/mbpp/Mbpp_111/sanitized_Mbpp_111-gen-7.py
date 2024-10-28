def common_in_nested_lists(nested_lists):
    sets = [set(lst) for lst in nested_lists]
    common = set.intersection(*sets)
    return common