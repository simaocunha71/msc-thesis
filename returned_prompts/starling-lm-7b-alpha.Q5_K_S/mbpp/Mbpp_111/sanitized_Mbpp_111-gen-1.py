from functools import reduce
def common_in_nested_lists(nested_list):
    # Flatten the nested list
    flat_list = reduce(lambda x, y: x + y, nested_list)
    # Convert the flattened list into a set to remove duplicates
    set_list = set(flat_list)
    # Return the set of common elements
    return set_list