def unique_sublists(lst):
    # Initialize an empty dictionary
    dict_sublists = {}

    # Loop over the list
    for sublist in lst:
        # Convert the sublist to a tuple
        tuple_sublist = tuple(sublist)

        # If the tuple is not in the dictionary, add it with a value of 1
        if tuple_sublist not in dict_sublists:
            dict_sublists[tuple_sublist] = 1

        # If the tuple is already in the dictionary, increment its value by 1
        else:
            dict_sublists[tuple_sublist] += 1

    # Return the dictionary
    return dict_sublists