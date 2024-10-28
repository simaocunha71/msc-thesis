"""
def common_in_nested_lists(lists):
    return set(reduce(lambda x,y: x.intersection(y), lists, set(lists[0])))
"""
