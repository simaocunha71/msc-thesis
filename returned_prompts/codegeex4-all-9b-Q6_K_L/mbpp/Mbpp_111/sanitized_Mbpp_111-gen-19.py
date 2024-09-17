def common_in_nested_lists(nested_lists):
    common = nested_lists[0]
    for lst in nested_lists[1:]:
        common = [x for x in common if x in lst]
    return set(common)