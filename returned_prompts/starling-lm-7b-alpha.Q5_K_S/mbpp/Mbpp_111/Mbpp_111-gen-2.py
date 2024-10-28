
def common_in_nested_lists(nested_list):
    return set(x for sublist in nested_list for x in sublist)


