def common_in_nested_lists(lists):
    common_elements = set(lists[0])
    for curr_list in lists[1:]:
        common_elements = common_elements & set(curr_list)
    return list(common_elements)