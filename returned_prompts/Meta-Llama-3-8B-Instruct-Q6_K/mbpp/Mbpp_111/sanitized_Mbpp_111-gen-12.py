def common_in_nested_lists(nested_lists):
    if not nested_lists:
        return set()
    flat_list = [item for sublist in nested_lists for item in sublist]
    common = set(flat_list[0])
    for item in flat_list[1:]:
        common &= set(item)
    return common