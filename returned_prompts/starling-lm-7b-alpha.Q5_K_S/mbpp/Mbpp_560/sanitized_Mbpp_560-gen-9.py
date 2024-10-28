def union_elements(t1,t2):
    # Convert tuples to lists
    list1 = list(t1)
    list2 = list(t2)
    # Concatenate the two lists
    combined_list = list1 + list2
    # Sort the combined list
    combined_list.sort()
    # Return the sorted list
    return tuple(combined_list)