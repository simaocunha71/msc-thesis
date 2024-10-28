def common_in_nested_lists(nested_list):
    def flatten_list(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten_list(item))
            else:
                flat_list.append(item)
        return flat_list

    flattened_list = flatten_list(nested_list)
    unique_elements = set(flattened_list)
    return unique_elements