def common_in_nested_lists(lst):
    common = set(lst[0])
    for sublist in lst[1:]:
        common = common.intersection(sublist)
    return common