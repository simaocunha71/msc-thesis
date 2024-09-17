def union_elements(tup1, tup2):
    """
    Finds the union of two tuples and returns the elements in sorted order.
    """
    # Convert both tuples to lists for easier manipulation
    tup1_list = list(tup1)
    tup2_list = list(tup2)

    # Combine the lists
    combined_list = tup1_list + tup2_list

    # Sort the combined list and return it as a tuple
    sorted_list = sorted(combined_list)
    return tuple(sorted_list)