def common_in_nested_lists(lst: list):
    def flatten(lst):
        return [item for sublist in lst for item in sublist]
    flat = flatten(lst)
    return set(flat)