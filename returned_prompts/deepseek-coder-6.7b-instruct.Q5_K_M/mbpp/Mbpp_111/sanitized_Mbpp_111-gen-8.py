def common_in_nested_lists(lst):
    common = set(lst[0])
    for l in lst[1:]:
        common = common & set(l)
    return list(common)