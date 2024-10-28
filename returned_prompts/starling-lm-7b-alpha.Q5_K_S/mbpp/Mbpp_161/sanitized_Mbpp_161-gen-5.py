def remove_elements(list_1, list_2):
    '''
    Remove all elements from a given list present in another list.
    '''
    # Create a new list
    new_list = []

    # Iterate over list_1
    for i in list_1:
        # Check if i is not in list_2
        if i not in list_2:
            # Add i to the new list
            new_list.append(i)

    return new_list