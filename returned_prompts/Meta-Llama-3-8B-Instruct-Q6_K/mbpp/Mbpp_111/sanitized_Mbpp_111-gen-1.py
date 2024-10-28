from typing import List
def common_in_nested_lists(nested_lists: List[List[int]]) -> set:
    common_elements = set(nested_lists[0])
    for nested_list in nested_lists[1:]:
        common_elements &= set(nested_list)
    return common_elements