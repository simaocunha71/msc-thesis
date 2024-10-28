def common_in_nested_lists(nested_list):
    # Find the common elements in the first list
    common = set(nested_list[0])
    # Iterate over the rest of the lists
    for lst in nested_list[1:]:
        # Update the set of common elements
        common = common & set(lst)
    # Return the set of common elements
    return list(common)