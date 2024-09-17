def common_in_nested_lists(lst: list) -> set:
    return set.intersection(*map(set, lst))