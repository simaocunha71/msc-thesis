def common_in_nested_lists(lst):
    return set(lst[0]).intersection(*lst)