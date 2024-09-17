def remove_elements(list_1, list_2):
    # Iterate through list_2
    for elem in list_2:
        # Remove all occurrences of elem in list_1
        while elem in list_1:
            list_1.remove(elem)
    return list_1