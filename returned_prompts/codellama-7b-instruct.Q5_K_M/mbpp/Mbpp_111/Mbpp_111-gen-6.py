
def common_in_nested_lists(lists: list) -> set:
    return set(set(lists[0]).intersection(*lists))


