def sort_sublists(input_list):
    '''This function sorts each sublist of strings in a given list of lists.'''
    # Iterate through the list
    for sublist in input_list:
        # Sort the sublist
        sublist.sort()
    return input_list