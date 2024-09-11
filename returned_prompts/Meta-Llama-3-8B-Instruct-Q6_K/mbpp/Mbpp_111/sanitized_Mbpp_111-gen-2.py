def common_in_nested_lists(nested_lists):
    return set.intersection(*map(set, nested_lists)) if nested_lists else set()