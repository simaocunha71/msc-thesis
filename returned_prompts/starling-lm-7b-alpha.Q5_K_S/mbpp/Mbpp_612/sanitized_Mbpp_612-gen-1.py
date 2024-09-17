def merge(lst):
    # Initialize the result
    result = [[], []]
    
    # Iterate through the elements of the list
    for sublist in lst:
        # Add the first element of the sublist to the first list of the result
        result[0].append(sublist[0])
        # Add the second element of the sublist to the second list of the result
        result[1].append(sublist[1])
    
    # Return the result
    return result