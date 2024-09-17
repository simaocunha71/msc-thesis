
def common_in_nested_lists(nested_lst):
    return set(nested_lst[0]).intersection(*nested_lst)


