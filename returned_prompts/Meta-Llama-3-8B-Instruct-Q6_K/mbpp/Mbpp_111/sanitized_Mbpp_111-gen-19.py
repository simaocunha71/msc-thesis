def common_in_nested_lists(nested_lists):
    if not nested_lists:
        return []
    common = [element for elements in zip(*nested_lists) for element in elements if list(elements).count(element) == len(nested_lists)]
    return set(common)