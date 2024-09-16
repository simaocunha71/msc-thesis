
def common_in_nested_lists(nested_lists):
    return list(set(nested_lists[0]).intersection(*nested_lists))
