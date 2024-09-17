def convert_list_dictionary(list1, list2, list3):
    # Iterate through each list
    for i in range(len(list1)):
        # Create a new dictionary
        new_dict = {}
        # Create another dictionary to store the values of the second and third list
        inner_dict = {}
        # Append the first list item to the new dictionary
        new_dict[list1[i]] = inner_dict
        # Iterate through the second and third list
        for j in range(len(list2)):
            # Append the second and third list item to the inner dictionary
            inner_dict[list2[j]] = list3[i]
    return new_dict