"""
def common_in_nested_lists(nested_list):
    common = set()
    for sublist in nested_list:
        common.intersection_update(sublist)
    return common
"""
